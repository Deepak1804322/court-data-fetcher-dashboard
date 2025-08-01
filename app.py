from flask import Flask, request, render_template
import sqlite3
from scraper import fetch_case_details

app = Flask(__name__)

DB_NAME = "queries.db"

def log_query(case_type, case_number, year, raw_response):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_type TEXT, case_number TEXT, year TEXT,
                    raw_response TEXT
                )''')
    c.execute("INSERT INTO queries (case_type, case_number, year, raw_response) VALUES (?, ?, ?, ?)",
              (case_type, case_number, year, raw_response))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        year = request.form['year']

        data = fetch_case_details(case_type, case_number, year)
        if data:
            log_query(case_type, case_number, year, str(data))
            return render_template('result.html', data=data)
        else:
            return render_template('result.html', error="Unable to fetch case details. Please try again.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
