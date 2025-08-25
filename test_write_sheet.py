# test_write_sheet.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# === Google Sheets 基本設定 ===
SHEET_ID = "13570nVTtolSe2iatWWhEYDsePYts_WTn75Itwwk8duA"
SHEET_NAME = "收支表"

# === 授權憑證位置 ===
CREDENTIAL_PATH = "money-pipe-109eeb88f0cd.json"  # 確保這是你下載的那個檔案名稱

def get_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIAL_PATH, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    return sheet

if __name__ == "__main__":
    sheet = get_sheet()
    # 寫入測試內容到 A1
    sheet.update("A1", [["✅ 成功連線！來自 Python 寫入"]])
    print("✅ 成功寫入 Google Sheet！")
