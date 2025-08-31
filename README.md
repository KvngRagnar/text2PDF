# Text to PDF Converter

A simple web application that converts text to PDF files using Flask and FPDF.

## Features

- Clean, modern user interface with gradient backgrounds and animations
- Simple text input area for content
- Instant PDF generation
- Easy download option
- Responsive design that works on all devices

## Requirements

- Python 3.x
- Flask
- FPDF
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KvngRagnar/text2PDF.git
cd text2PDF
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter or paste your text in the input area
4. Click "Generate PDF"
5. Download your PDF file

## Project Structure

```
text2pdf-main/
│
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
│
└── templates/
    ├── index.html     # Main page template
    ├── result.html    # Download page template
    │
    └── static/
        └── css/
            └── style.css  # Stylesheet
```

## License

This project is open source and available for anyone to use and modify.

## Author

- KvngRagnar

## Contributing

Contributions, issues, and feature requests are welcome!
