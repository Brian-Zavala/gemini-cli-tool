from functions.get_files_info import get_files_info, get_file_content, write_file, run_python_file

# def test_get_files_info():
#     # Test with a valid directory
#     result = get_files_info('calculator', '.')
#     print(result)  # Expected to list files in the current directory

#     result = get_files_info('calculator', 'pkg')
#     print(result)  # Expected to return an error message
    
#     result = get_files_info('calculator', '/bin')
#     print(result)

#     result = get_files_info('calculator', '../')  # Assuming empty_dir exists and is empty
#     print(result)  

# test_func = test_get_files_info
# test_func()

# def test_get_file_content():
#     # Test with main.py and calculator.py
#     result = get_file_content('calculator', 'main.py')
#     print(result)  # Expected to return the content of lorem.txt

#     result = get_file_content('calculator', 'pkg/calculator.py')
#     print(result)  # Expected to return the content of calculator.py

#     result = get_file_content('calculator', '/bin/cat')
#     print(result)  # Expected to returjn an error message

# test_get_file_content()

# def test_write_file():
#     result = write_file('calculator', 'lorem.txt',"wait, this isn't lorem ipsum")
#     print(result)  # Expected to return a success message

#     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print(result)  # Expected to return an error message

#     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print(result)  # Expected to return an error message

# test_write_file()

def test_run_python_file():
    # Test with main.py
    result = run_python_file('calculator', 'main.py')
    print(result)  # Expected to return the output of the main.py script

    result = run_python_file('calculator', 'tests.py')
    print(result)  # Expected to return the output of the calculator.py script

    result = run_python_file('calculator', '../main.py')
    print(result)  # Expected to return an error message

    result = run_python_file('calculator', 'nonexistent.py')
    print(result)  # Expected to return an error message

test_run_python_file()