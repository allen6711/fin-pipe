# FinPipe - Showcase Backend
# This is a simple Flask server to demonstrate the backend capabilities
# described in the project resume, specifically parsing Excel files with Pandas.
# For the live demo, this logic is handled on the client-side for a faster,
# serverless user experience.

import os
import pandas as pd
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

def process_spreadsheet(file_path):
    """
    This function demonstrates how to read an Excel or CSV file using Pandas,
    process it, and return it as a list of dictionaries.
    
    In a fully integrated system, this function would be called by an API endpoint.
    """
    try:
        # Check the file extension and use the appropriate pandas function
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            return {"error": "Unsupported file type"}

        # --- Data Processing Demonstration ---
        # 1. Drop rows with any missing values for demonstration
        df.dropna(inplace=True)

        # 2. Convert known date columns to datetime objects (if any)
        # Example: If there's a column named 'Transaction Date', you'd uncomment the next line
        # df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

        # 3. Normalize column names (e.g., lowercase and replace spaces with underscores)
        df.columns = df.columns.str.lower().str.replace(' ', '_')

        # Convert the processed DataFrame to a list of dictionaries
        processed_data = df.to_dict(orient='records')

        return processed_data

    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def index():
    """
    Root endpoint to confirm the server is running.
    """
    return "<h1>FinPipe Backend Server</h1><p>This server is a showcase for Python/Pandas data processing.</p>"

# Example of how to use the processing function (for demonstration only)
# To test this, you would place a sample file in the backend directory
# and call this function from within a Python environment.
if __name__ == '__main__':
    # This part is for demonstration and won't run when using 'flask run'
    
    # Create a dummy excel file for testing if it doesn't exist
    if not os.path.exists("sample_data.xlsx"):
        dummy_data = {
            'Date': ['2025-01-10', '2025-01-11'],
            'Description': ['Sample Coffee Shop', 'Sample Book Store'],
            'Amount': [-5.00, -25.00]
        }
        dummy_df = pd.DataFrame(dummy_data)
        dummy_df.to_excel("sample_data.xlsx", index=False)
        print("Created 'sample_data.xlsx' for demonstration.")

    print("\n--- Demonstrating Pandas Processing ---")
    processed_result = process_spreadsheet('sample_data.xlsx')
    print("Processed Data:")
    import json
    print(json.dumps(processed_result, indent=2))
    print("-------------------------------------\n")
    
    # To run the web server, use the command: flask run
    # The server will be available at http://127.0.0.1:5000
    app.run(debug=True)
