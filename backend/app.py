from flask import Flask, request, jsonify
import pandas as pd
from collections import defaultdict
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS
from datetime import datetime, date

app = Flask(__name__)
CORS(app) 
UPLOAD_FOLDER = "temp_upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SHEET_ID = "13570nVTtolSe2iatWWhEYDsePYts_WTn75Itwwk8duA"
SHEET_NAME = "收支表"

def get_gspread_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("money-pipe-109eeb88f0cd.json", scope)
    return gspread.authorize(creds)

@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    file = request.files["file"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)
    df = pd.read_csv(filepath)
    payee_col = next((col for col in df.columns if "payee" in col.strip().lower()), None)
    if not payee_col:
        return jsonify({"error": "Payee column not found in CSV."}), 400

    payees = df[payee_col].dropna().unique().tolist()
    return jsonify({"payees": payees, "csv_path": filepath})

@app.route("/submit_categories", methods=["POST"])
def submit_categories():
    """Receives category mappings and writes processed data to Google Sheets."""
    data = request.json
    mapping_from_frontend = data["mapping"]
    csv_path = data["csv_path"]

    cleaned_mapping = {key.strip(): value for key, value in mapping_from_frontend.items()}

    df = pd.read_csv(csv_path)

    # ✅ 關鍵修正：明確指定日期的格式為 "月/日/年"
    df["Posted Date"] = pd.to_datetime(df["Posted Date"], format="%m/%d/%Y", errors="coerce")
    
    # 丟棄任何日期解析失敗的行
    df = df.dropna(subset=["Posted Date"])
    

    records = []
    for _, row in df.iterrows():
        if pd.isna(row["Payee"]):
            continue
            
        payee_from_csv = str(row["Payee"]).strip()
        posted_date_str = row["Posted Date"].strftime("%Y/%m/%d")
        note = payee_from_csv
        category = cleaned_mapping.get(payee_from_csv, "Uncategorized")
        
        amount = pd.to_numeric(row.get("Amount"), errors='coerce')

        record = None
        if pd.notna(amount):
            if amount < 0:
                record = ["", posted_date_str, "Expense", "", "", category, abs(amount), note]
            elif amount > 0:
                record = ["", posted_date_str, "Income", category, abs(amount), "", "", note]


        if record:
            records.append(record)

    # --- Write data to Google Sheets ---
    try:
        client = get_gspread_client()
        sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
        
        if not records:
            return jsonify({"status": "success", "rows_written": 0, "message": "No valid records to write."})

        sheet.append_rows(records, value_input_option='USER_ENTERED')
        return jsonify({"status": "success", "rows_written": len(records)})
        
    except Exception as e:
        print(f"Error writing to Google Sheets: {e}")
        return jsonify({"error": f"Failed to write to Google Sheets: {str(e)}"}), 500



print("🧭 註冊的 route 有：")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule.methods} -> {rule}")

if __name__ == "__main__":
    app.run(debug=True, port=5050)

