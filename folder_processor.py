import os
import argparse

def process_file(file_path):
    # Implement your file processing logic here
    # For example, you could read the file contents, perform some operations, etc.
    print(f"Processing file: {file_path}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            process_file(file_path)

def main():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Process all files in a folder and its subfolders.")
    parser.add_argument("folder", help="Path to the folder containing files to process.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the specified folder exists
    if not os.path.exists(args.folder):
        print(f"Error: Folder '{args.folder}' does not exist.")
        return

    # Process the folder and its subfolders
    process_folder(args.folder)

if __name__ == "__main__":
    main()
