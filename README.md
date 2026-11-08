  # Notepad Tracker

Notepad Tracker is a web-based text editor built using **Python and Flask** that allows users to create, open, edit, and save text files through a simple browser interface.

The application is designed to combine traditional text editing with Git-based version control, enabling automatic tracking of file changes and maintaining a history of modifications.

## Features

- **Text Editor:** Write and edit text directly through a browser-based interface.
- **File Creation:** Create new text files.
- **File Management:** Open and save existing text files.
- **Workspace Management:** Store files within a configured workspace directory.
- **File Validation:** Validate filenames and restrict file access to the configured workspace.
- **Git Integration:** Designed to support automatic commits and version tracking of file changes.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Editor interface |
| CSS | User interface styling |
| JavaScript | Frontend interactions and API communication |
| Git | Version control |
| GitPython | Python integration with Git |
| Pytest | Application testing |

## Project Structure

```text
Notepad-Tracker/
│
├── app/
│   ├── controllers/
│   ├── services/
│   │   └── file_service.py
│   ├── models/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── editor.js
│   ├── __init__.py
│   └── routes.py
│
├── tests/
├── workspace/
├── config.py
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/NithyaShree581/Notepad-Tracker.git
cd Notepad-Tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python run.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Load the text editor |
| POST | `/api/files` | Create or save a text file |
| GET | `/api/files?filename=notes.txt` | Open an existing text file |

### Sample Save Request

**POST** `/api/files`

```json
{
    "filename": "notes.txt",
    "content": "Hello! This is my first Notepad Tracker file."
}
```

### Sample Response

```json
{
    "message": "File saved successfully",
    "filename": "notes.txt"
}
```

## Application Architecture

The application follows a modular structure:

- **Routes:** Define application URLs and handle HTTP requests.
- **Services:** Handle file creation, reading, writing, and path validation.
- **Templates:** Provide the browser-based text editor interface.
- **Static Files:** Contain CSS styling and JavaScript functionality.
- **Configuration:** Defines the application's workspace directory.

## Git Integration

Git is intended to provide version control for files managed by the application.

The planned workflow is to detect when a user stops editing, save the updated file, and automatically create a Git commit. This will allow users to maintain a history of changes and retrieve previous versions.

## Author

Developed as part of a Python and Flask application development assignment.

**GitHub Repository:** https://github.com/NithyaShree581/Notepad-Tracker
