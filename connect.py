from flask import Flask, render_template, request, session
import ibm_db

app = Flask(__name__)

# Replace with your actual database connection details
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

@app.route('/showall')
def show_all():
    conn = connect_to_db()
    if conn:
        sql = "SELECT * FROM login_details"  # Use correct table name
        stmt = ibm_db.exec_immediate(conn, sql)
        dictionary = ibm_db.fetch_both(stmt)
        while dictionary:
            print("The Name is:", dictionary["NAME"])
            print("The E-mail is:", dictionary["EMAIL"])
            print("The Password is:", dictionary["PASSWORD"])
            print("The confirm Password is:", dictionary["confirm_password"])
            dictionary = ibm_db.fetch_both(stmt)
        ibm_db.close(conn)
    return "Check your console for the printed details."

# Add other routes and functions for inserting, querying, etc.

if __name__ == '__main__':
    app.run(debug=True)
