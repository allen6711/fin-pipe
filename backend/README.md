FinPipe - Backend Showcase
This directory contains a simple Flask server that demonstrates the Python-based data processing capabilities of the FinPipe project, as mentioned in the project's resume.

Purpose
The primary goal of this backend is to showcase proficiency with Python, Flask, and the Pandas library for data manipulation, specifically for parsing and normalizing data from .xlsx files.

In the live, interactive version of the FinPipe application, all data processing is handled on the client-side (in the browser) using JavaScript. This approach was chosen for the live demo to provide a faster, serverless user experience that does not require hosting a backend server. This Flask application serves as a proof-of-concept for how the same logic would be implemented in a Python backend environment.

Tech Stack
Python: Core programming language.

Flask: A lightweight web framework for creating the server and API endpoints.

Pandas: The primary library used for powerful and efficient data analysis and manipulation, including reading Excel files.

openpyxl: A required dependency by Pandas for reading and writing .xlsx files.

Setup and Installation
To run this server locally, you'll need to set up a Python virtual environment.

Navigate to this directory:

cd fin-pipe/backend

Create a Python virtual environment:

On macOS/Linux:

python3 -m venv venv

On Windows:

py -m venv venv

Activate the virtual environment:

On macOS/Linux:

source venv/bin/activate

On Windows:

.\venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

How to Run
Once the setup is complete, you can run the Flask development server with the following command:

flask run

You will see output indicating that the server is running, typically on http://127.0.0.1:5000. You can visit this URL in your browser to see a confirmation message.