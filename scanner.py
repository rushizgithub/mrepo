import os
import re
import sys

def get_python_version(file_path):
    encodings = ["utf-8", "latin-1", "ascii"]

    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as file:
                content = file.read()

                # Use regular expression to find the Python shebang or version comment
                match = re.search(r"(#!/usr/bin/env\s+python(\d+(\.\d+)*)?|python(\d+(\.\d+)*)?)", content)

                if match:
                    return match.group().replace("#!", "").strip()
        except UnicodeDecodeError:
            pass

    return None

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            python_version = get_python_version(file_path)

            if python_version:
                print(f"File: {file_path}, Python version: {python_version}")
            else:
                print(f"File: {file_path}, Python version not specified")

if __name__ == "__main__":
    folder_path = "util"  # Replace with the actual path to your folder
    process_folder(folder_path)
