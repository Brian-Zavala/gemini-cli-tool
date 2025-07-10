import os
import subprocess
from config import max_chars
from google.genai import types


def get_files_info(working_dir, directory=None):
    """
    get_files_info retrieves information about files and directories within a specified working directory.
    It returns a string
    """

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


def get_file_content(working_directory, file_path):
    """
    get_file_content retrieves the content of a file within a specified working directory.
    """
    working_abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    target_abs_path = os.path.abspath(full_path)
    if not target_abs_path.startswith(working_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_abs_path, "r") as file:
            content = file.read()
            if len(content) > max_chars:
                content = (
                    content[:max_chars]
                    + " "
                    + '[...File "{file_path}" truncated at 10000 characters]'
                )
            return content
    except Exception as e:
        return f"Error: {str(e)}"


def write_file(working_directory, file_path, content):
    """
    write_file writes content to a file within a specified working directory.
    """
    working_abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    target_abs_path = os.path.abspath(full_path)

    if not target_abs_path.startswith(working_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_abs_path, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {str(e)}"


def run_python_file(working_directory, file_path):
    """
    run_python_file executes a Python file within a specified working directory.
    """
    working_abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    target_abs_path = os.path.abspath(full_path)

    if not target_abs_path.startswith(working_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_abs_path):
        return f'Error: File "{file_path}" not found'
    if not target_abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    try:
        run_file = subprocess.run(
            ["python3", target_abs_path], capture_output=True, text=True, timeout=30
        )

        if run_file.stdout:
            return f"STDOUT: {run_file.stdout.strip()}"
        if run_file.stderr:
            return f"STDERR: {run_file.stderr.strip()}"
        if run_file.returncode != 0:
            return f"Process exited with code {run_file.returncode}"
        if not run_file.stdout:
            return "No output produced"

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=" get_file_content retrieves the content of a file within a specified working directory.",
            ),
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="run_python_file executes a Python file within a specified working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "content": types.Schema(
                type=types.Type.STRING,
                description="write_file writes content to a file within a specified working directory.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Text content that will be written to the file.",
            ),
        },
    ),
)
