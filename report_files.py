# Merges all text files in a directory and its subdirectories into a single file, specified files and folders can be excluded.
# Useage:  This script, report_fies.py must be located in the docs folder.  Using terminal move to docs folder then generate report
#    cd docs
#    python report_files.py
#
#
#   merge_files Parameters:
#    - input_dir (str): The directory to scan for files.
#    - blacklist (set): A set of files and directories to exclude.
#    - output_file (str): The path to the output file.
#


import os
def merge_files(input_dir, blacklist, output_file):

    # Open the output file for writing
    with open(output_file, 'w') as output:
        # Walk through the directory
        for root, dirs, files in os.walk(input_dir):
            # Skip blacklisted directories
            dirs[:] = [d for d in dirs if d not in blacklist]

            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip blacklisted files
                if file in blacklist or file_path in blacklist:
                    print(f"Skipping blacklisted file: {file_path}")
                    continue
                
                try:
                    # Append file content to the output file
                    with open(file_path, 'r') as f:
                        output.write(f"--------------------------------------")  # Add file header
                        output.write(f"\n {file_path} \n")  # Add file header
                        output.write(f"--------------------------------------\n")  # Add file header
                        output.write(f.read())
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    print(f"All files merged into {output_file} successfully.")

# Embedded blacklist
blacklist = {
    # Excluded directories
    "venv", "__pycache__", "docs", ".git",
    # Excluded files
    ".env", ".gitignore", "env.ps1", "README.md", "temp.ipynb"
}

# Example Usage
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Parent directory (formlab)
input_directory = os.path.join(base_dir)  # Scan formlab and its subdirectories
output_file = os.path.join(base_dir, "docs", "report_output.txt")  # Save output in formlab/docs
merge_files(input_directory, blacklist, output_file)
