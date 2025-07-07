import os

def get_files_info(working_dir, directory=None):
   
    # step 1: get absolute path of the working directory
    working_abs_path = os.path.abspath(working_dir)

    # step 2: Build the full path to the directory
    full_path = os.path.join(working_dir, directory)

    # step 3: Get the absolute path of the rquested directory
    target_abs_path = os.path.abspath(full_path)

    # step 4: Check if the target directory exists
    if not target_abs_path.startswith(working_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # step 5: if directory arg is not a directory, return an error
    if not os.path.isdir(target_abs_path):
        return f'Error: "{directory}" is not a directory'
    
    # step 6: Build a string representing contents of the directory
    try:
        file_content = []

        # GEt all items in the directory (files and subdirectories)
        items = os.listdir(target_abs_path)
        
        for item in items:
                file_path = os.path.join(target_abs_path, item)
                file_size = os.path.getsize(file_path)
                is_dir = os.path.isdir(file_path)
                formatted_line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"    
                file_content.append(formatted_line)

        return "\n".join(file_content) 
    except Exception as e:
        return f"Error: {str(e)}"