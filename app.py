from flask import Flask, render_template, request, send_file, jsonify
from fpdf import FPDF
import os

app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate PDF
@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        text = request.form.get('text')

        if not text or text.strip() == "":
            return jsonify({"success": False, "error": "No text provided"}), 400

        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)

        filename = "output.pdf"
        pdf.output(filename)

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

