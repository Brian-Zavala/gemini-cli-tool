from functions.get_files_info import get_files_info

def test_get_files_info():
    # Test with a valid directory
    result = get_files_info('calculator', '.')
    print(result)  # Expected to list files in the current directory

    result = get_files_info('calculator', 'pkg')
    print(result)  # Expected to return an error message
    
    result = get_files_info('calculator', '/bin')
    print(result)

    result = get_files_info('calculator', '../')  # Assuming empty_dir exists and is empty
    print(result)  

test_func = test_get_files_info
test_func()