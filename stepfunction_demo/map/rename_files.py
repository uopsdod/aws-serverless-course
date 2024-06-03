import os

def rename_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort the files to maintain a consistent order
    files.sort()
    
    # Rename each file
    for i, filename in enumerate(files, start=1):
        # Create the new filename
        new_filename = f"pangolin_{i:03}.png"  # Adjust the extension as needed
        
        # Get the full paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{filename}' to '{new_filename}'")

# Specify the folder path
folder_path = '/Users/stsai/Davinci/AWS_Serverless_2024/aws_serverless_正式/step_function_map_1000_images_002'

# Call the function to rename files
rename_files_in_folder(folder_path)
