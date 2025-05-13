FILEPATH = "todos.txt"  #constant variable


def get_todos(filepath=FILEPATH):   #default value for the parameter
    with open(filepath, 'r') as file:         #open the file to read
        todos_local = file.readlines()
    return todos_local 

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:         #open the file to write
        file.writelines(todos_arg)                  #write the list to the file


#excludes the code when functions file is imported and ran in the main file
if __name__ == "__main__":
    print("hello from functions")