import os

def create_python_file_for_new_directory(directory):

    file_name = directory.split()[0] + '.py' 

    if not os.path.exists(file_name):  
        open(file_name, 'w').close()  
        print(f"Created file: {file_name}")
    else:
        print(f"File {file_name} already exists.")

def process_new_directory(directory_path):

    directory_name = os.path.basename(directory_path)  
    create_python_file_for_new_directory(directory_name)

if __name__ == "__main__":
    current_directory = os.getcwd()  
    process_new_directory(current_directory)
