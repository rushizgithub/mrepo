import os
import glob
import argparse

def process_file(file_path):
    # Implement your file processing logic here
    # For example, you could read the file contents, perform some operations, etc.
    print(f"Processing file: {file_path}")

def process_folder(folder_path):
    # Get a list of all files in the folder using glob
    file_list = glob.glob(os.path.join(folder_path, "*"))

    # Process each file in the folder
    for file_path in file_list:
        process_file(file_path)

def main():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Process all files in a folder.")
    parser.add_argument("folder", help="Path to the folder containing files to process.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the specified folder exists
    if not os.path.exists(args.folder):
        print(f"Error: Folder '{args.folder}' does not exist.")
        return

    # Process the folder and its files
    process_folder(args.folder)

if __name__ == "__main__":
    main()
