from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Change this to a secure secret key

import ibm_db  # Make sure you have ibm_db installed

# Database connection details
db_credentials = {
    "DATABASE": "bludb",
    "HOSTNAME": "ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud",
    "PORT": "31321",
    "UID": "nxf41414",
    "PWD": "ihFzkv0YDegwOQGn",
}

def connect_to_db():
    try:
        conn = ibm_db.connect(
            f"DATABASE={db_credentials['DATABASE']};"
            f"HOSTNAME={db_credentials['HOSTNAME']};"
            f"PORT={db_credentials['PORT']};"
            f"UID={db_credentials['UID']};"
            f"PWD={db_credentials['PWD']};",
            '',
            ''
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None

# ... your other functions ...

if __name__ == '__main__':
    app.run(debug=True)
