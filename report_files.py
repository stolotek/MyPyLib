# Merges all text files in a directory and its subdirectories into a single file, excluding specified files and folders.
# Useage:   merge_files(input_directory, output_file, blacklist_file)
import os
def merge_files(input_dir, output_file, blacklist_file):
    """
    Merges all text files in a directory and its subdirectories into a single file,
    excluding specified files and folders.

    Parameters:
    - input_dir (str): The directory to scan for files.
    - output_file (str): The path to the output file.
    - blacklist_file (str): The path to the blacklist file containing files and folders to exclude.
    """
    # Read the blacklist file
    blacklist = set()
    if os.path.exists(blacklist_file):
        with open(blacklist_file, 'r') as bf:
            blacklist = {line.strip() for line in bf if line.strip()}

    # Open the output file for writing
    with open(output_file, 'w') as output:
        # Walk through the directory
        for root, dirs, files in os.walk(input_dir):
            # Skip blacklisted directories
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in blacklist and d not in blacklist]

            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip blacklisted files
                if file in blacklist or file_path in blacklist:
                    print(f"Skipping blacklisted file: {file_path}")
                    continue
                
                try:
                    # Append file content to the output file
                    with open(file_path, 'r') as f:
                        output.write(f"\n\n--- {file_path} ---\n\n")  # Add file header
                        output.write(f.read())
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    print(f"All files merged into {output_file} successfully.")

# Example Usage
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Parent directory (formlab)
input_directory = os.path.join(base_dir)  # Scan formlab and its subdirectories
output_file = os.path.join(base_dir, "docs", "report_output.txt")  # Save output in formlab/docs
blacklist_file = os.path.join(base_dir, "docs", "report_blacklist.txt")  # Blacklist file in formlab/docs

# Run the merge function
merge_files(input_directory, output_file, blacklist_file)
