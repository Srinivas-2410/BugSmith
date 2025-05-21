from flask import Flask, render_template, request, send_file
from utils.ai_engine import generate_bug_report
from utils.pdf_generator import create_pdf
import os
from github.issue_creator import create_github_issue

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        bug_description = request.form['bug_description']
        severity = request.form.get('severity', 'Medium')
        environment = request.form.get('environment', 'Not specified')

        result = generate_bug_report(bug_description, severity, environment)
    
    return render_template('index.html', result=result)

@app.route('/export', methods=['POST'])
def export_pdf():
    data = request.form.to_dict()
    file_path = create_pdf(data)
    return send_file(file_path, as_attachment=True)



@app.route('/create_issue', methods=['POST'])
def create_issue():
    report_text = request.form['ai_report']
    title = request.form.get('title', 'AI-Generated Bug Report')
    result = create_github_issue(title, report_text)
    return f"<p>{result}</p><a href='/'>Back</a>"

if __name__ == '__main__':
    os.makedirs('static/reports', exist_ok=True)
    app.run(debug=True)