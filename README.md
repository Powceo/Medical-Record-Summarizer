# Medical Record Summarizer

A desktop application for summarizing medical records from PDFs using Google's OCR API for better handling of medical and handwritten documents.

## Features

- PDF document upload and processing
- Google Cloud Vision OCR for accurate text extraction from medical documents
- Support for handwritten text recognition
- Medical terminology extraction and summarization
- User-friendly desktop interface
- Export summaries to various formats

## Requirements

- Python 3.8+
- Google Cloud Vision API credentials
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository:
```
git clone https://github.com/Powceo/Medical-Record-Summarizer.git
cd Medical-Record-Summarizer
```

2. Create a virtual environment and activate it:
```
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Set up Google Cloud Vision API:
   - Create a project in Google Cloud Console
   - Enable the Cloud Vision API
   - Create a service account and download the JSON credentials file
   - Save the credentials file as `google_credentials.json` in the project directory

## Usage

1. Run the application:
```
python src/main.py
```

2. Use the interface to upload PDF medical records
3. Process the documents using Google OCR
4. View and export the summarized medical information

## Project Structure

```
Medical-Record-Summarizer/
├── src/                    # Source code
│   ├── main.py             # Application entry point
│   ├── ui/                 # UI components
│   ├── core/               # Core functionality
│   └── utils/              # Utility functions
├── resources/              # Application resources
├── tests/                  # Test files
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## License

MIT