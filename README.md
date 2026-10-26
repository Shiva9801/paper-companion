# Paper Companion

#### Video Demo: https://youtu.be/SZdRpjZF6K0

#### Description:

Paper Companion is a Python command-line application designed to help
users read and organize technical and research papers.

It allows users to search for words or phrases, navigate numbered
sections, maintain a personal glossary, and save notes for individual
papers. It also supports extracting text from PDF documents using
PyMuPDF.

## Features

### 1. Load Research Papers
- Load existing TXT files.
- Open PDF files directly through the application.
- Automatically extract text from PDFs using PyMuPDF.
- Save extracted text as a TXT file in the `extracted_text/` directory.
- Preserve page boundaries using page markers.

### 2. Search for Words and Phrases
- Search for words or phrases within the loaded paper.
- Perform case-insensitive searches.
- Display matching text with surrounding context.

### 3. Read a Section
- Identify numbered section headings using regular expressions.
- Display recognized sections.
- Read a selected section of the paper.

### 4. Manage a Personal Glossary
- Add terms and their meanings.
- View saved glossary entries.
- Store glossary entries in `glossary.json`.
- Prevent duplicate terms from being added.

### 5. Manage Notes
- Add personal notes while reading.
- View previously saved notes.
- Organize notes by paper filename.
- Store notes persistently in `notes.json`.

## Technologies Used

- Python
- PyMuPDF
- JSON
- Regular expressions
- pytest

## Project Structure

    paper-companion/
    ├── project.py               # Main application logic
    ├── test_project.py          # Automated pytest tests
    ├── requirements.txt         # Dependencies (PyMuPDF, pytest)
    ├── README.md                # Documentation
    ├── .gitignore               # Keeps generated files out of Git
    ├── paper/                   # (Optional) Folder for input PDFs
    │   └── Attention-is-all-you-need.pdf  # Example PDF (not submitted)
    ├── extracted_text/          # (Auto-generated) Output folder for TXT files
    ├── glossary.json            # (Auto-generated) Saved glossary terms
    └── notes.json               # (Auto-generated) Saved user notes

- `project.py`: Contains the main application loop, PDF extraction logic, search functionality, section navigation, and JSON storage functions.
- `test_project.py`: Contains the `pytest` automated tests for file loading, glossary operations, and note management.
- `requirements.txt`: Lists the external dependencies (`PyMuPDF` and `pytest`) needed to run the project.
- `README.md`: This documentation file.
- `paper/`: Contains original research papers (example provided).
- `extracted_text/`: Created automatically when a PDF is processed.
- `glossary.json` and `notes.json`: Created automatically to store user data.
## Installation

### Requirements

- Python 3
- PyMuPDF
- pytest (for running tests)

Install the dependencies using:

    python -m pip install -r requirements.txt

If you do not have a `requirements.txt` file yet, it should contain:

    PyMuPDF
    pytest

## How to Run

Start the application from the project directory:

    python project.py

When prompted, enter the path to a PDF or TXT file.

### Example: Opening a PDF

    Enter the PDF or TXT file path: paper/Attention-is-all-you-need.pdf

The application extracts the PDF text, saves it to:

    extracted_text/Attention-is-all-you-need.txt

The extracted content is also loaded directly into Paper Companion.

### Example: Opening a TXT File

    Enter the PDF or TXT file path: extracted_text/Attention-is-all-you-need.txt

The application loads the existing text file without extracting it again.

## Application Menu

After loading a paper, the application provides these options:

    1. Search for a word
    2. Read a section
    3. Manage glossary
    4. Manage Notes
    5. Exit

Choose an option to use the corresponding feature.

## Running the Tests

The project includes automated tests in `test_project.py`.

Run the tests using:

    python -m pytest -v

The tests cover file loading, missing files, Unicode text,
glossary operations, and note management.

## Design Decisions

### Command-Line Interface

A command-line interface keeps the application simple and allows
users to perform research-related tasks without requiring a graphical
interface or web server.

### PDF Text Extraction

PyMuPDF is used to extract text from PDF documents. Integrating
extraction into `project.py` allows users to open PDFs directly
instead of running a separate extraction script.

Extracted text is saved as UTF-8 TXT, with page markers to help
preserve the document's page boundaries.

### JSON Storage

JSON files are used to store glossary entries and notes. This provides
a straightforward way to preserve user information between sessions
without requiring a database.

### Testing

pytest is used to test important functions and verify that expected
behavior is maintained as the project develops.

## Limitations

- Scanned PDFs containing images of text are not automatically
  processed using OCR.
- PDF extraction may not preserve the original layout perfectly.
- Tables, equations, figures, and multi-column layouts may not be
  extracted in their original form.
- Section navigation depends on the heading format recognized by
  the current regular expression.
- Page markers are preserved in the extracted text, but search and
  section navigation are not fully page-aware.
- Extracted text quality depends on the structure of the original PDF.

## Future Improvements

Possible improvements include:

- Better recognition of section headings.
- OCR support for scanned research papers.
- More accurate handling of tables and multi-column documents.
- Search results that include page numbers.
- Improved organization and retrieval of research notes.

## Author

Shivam Kumar

GitHub: [Shiva9801](https://github.com/Shiva9801)

## Project

Paper Companion was developed as a final project for CS50's
Introduction to Programming with Python (CS50P).