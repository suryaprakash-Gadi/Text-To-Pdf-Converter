import os
from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, text)
    pdf_file = 'converted.pdf'
    pdf.output(pdf_file)
    return render_template('result.html', pdf_file=pdf_file)

@app.route('/download/<filename>')
def download_pdf(filename):
    return send_file(os.path.abspath(filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
