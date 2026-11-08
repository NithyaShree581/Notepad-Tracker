
from pathlib import Path


class FileService:

    def __init__(self, workspace):
        self.workspace = Path(workspace).resolve()
        self.workspace.mkdir(parents=True, exist_ok=True)

    def resolve_path(self, filename):
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("Filename is required")

        path = (self.workspace / filename).resolve()

        if not path.is_relative_to(self.workspace):
            raise ValueError("File must be inside the workspace")

        if path.suffix.lower() != ".txt":
            raise ValueError("Only .txt files are supported")

        return path

    def save_file(self, filename, content):
        path = self.resolve_path(filename)

        if not isinstance(content, str):
            raise ValueError("Content must be text")

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

        return {"message": "File saved successfully", "filename": filename}

    def open_file(self, filename):
        path = self.resolve_path(filename)

        if not path.is_file():
            raise FileNotFoundError("File not found")

        return {
            "filename": filename,
            "content": path.read_text(encoding="utf-8")
        }
