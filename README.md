FinPipe - Smart Accounting Web App
FinPipe is a client-side web application designed to streamline personal accounting. It allows users to upload their bank transaction records (in .xlsx or .csv format), automatically categorizes transactions using a combination of a Large Language Model (LLM) and learned user preferences, and syncs the cleaned data to a specified Google Sheet.

This project is built with modern web technologies and demonstrates a practical application of AI in personal finance management.

✨ Features
File Upload: Easy drag-and-drop or button-click file uploader for .xlsx and .csv files.

Smart Categorization:

LLM-Powered: Utilizes the Google Gemini API to intelligently categorize unknown transactions based on their description.

Recurring Payee Learning: The app learns and remembers your manual category corrections. The next time the same transaction description appears, it's automatically categorized according to your preference, saving API calls and personalizing the experience.

Dynamic Category Fetching: Automatically reads category lists from your "Summary" tab in the target Google Sheet, ensuring the AI and UI always use your personalized categories.

Column Mapping: An intuitive interface to map columns from your uploaded file (e.g., "Transaction Date", "Details") to the application's required fields ("Date", "Description", "Amount").

Inline Transaction Notes: Ability to add notes to individual transactions before exporting.

Google Sheets Integration: Securely syncs the processed and categorized data to a specified Google Sheet using OAuth 2.0.

Persistent Memory: Remembers your API keys and column mapping preferences locally in your browser for convenience.

Retro UI: A unique, retro-themed user interface built with Tailwind CSS.

🚀 Setup
To run this application, you need to obtain API credentials from Google.

Step 1: Get a Google Gemini API Key
Go to Google AI Studio.

Sign in with your Google account.

Click on "Get API key" and then "Create API key in new project".

Copy the generated API Key.

Step 2: Get a Google Sheets OAuth 2.0 Client ID
Go to the Google Cloud Console.

Create a new project or select an existing one.

In the search bar, find and enable the "Google Sheets API".

Go to "APIs & Services" > "Credentials".

Click "+ CREATE CREDENTIALS" and select "OAuth client ID".

If prompted, configure the "OAuth consent screen":

Select "External" for the user type.

Fill in the required fields (App name, User support email, Developer contact).

Under "Test users", add the Google account email you will be using to test the app.

Create the OAuth Client ID:

Application type: "Web application".


Click "Create" and copy the generated Client ID.

Step 3: Prepare Your Google Sheet
Create a copy of the template sheet or use your own.

Copy the Spreadsheet ID from the URL. It's the long string of characters between /d/ and /edit.

Example: .../spreadsheets/d/THIS_IS_THE_ID/edit

Ensure you have a tab named "Summary" where your expense and income categories are listed (specifically in ranges C29:C42 and I29:I42).

Note the name of the tab where you want to record transactions (e.g., "Transactions"). This is your Target Sheet Name.

💻 How to Run Locally
Create the folder structure as described (fin-pipe/frontend/).

Place the index.html file inside the frontend folder.

If you are using Visual Studio Code, install the Live Server extension.

Right-click the index.html file and select "Open with Live Server".

The application will open in your browser.

Click the settings icon (⚙️) in the top-right corner.

Paste the API keys and IDs you obtained into the corresponding fields.

Save the settings and start using the app!