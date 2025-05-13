
#from functions import get_todos, write_todos
import functions

#import standard modules
import time
now = time.strftime("%b %d, %Y %H:%M:%S")   #get the current date and time
print("It is", now)  

while True:
    user_action = input("Type add, show, edit, complete or exit: ")   #user input
    user_action = user_action.strip()                    #remove whitespace
    
    #match user input
    if user_action.startswith('add'):   #check if the input starts with 'add'
        to_do = user_action[4:]   #slice the string to get the input

        todos = functions.get_todos()   #call the function to get the list
            
        todos.append(to_do + '\n')             #add input to the li   

        functions.write_todos(todos)     #call the function to write the list

    elif user_action.startswith('show'):     
    
        todos = functions.get_todos()                   

        #new_to_dos = [item.strip('\n') for item in todos] #remove whitespace - list comprehension
        
        for index, item in enumerate(todos):    
            item = item.strip('\n')      
            row = f"{index + 1}-{item}"     #format the list
            print(row)                    
                                          
    elif user_action.startswith('edit'):   #check if the input starts with 'edit'
        try:
            number = int(user_action[5:])   #slice the string to get the input
    
            number = number - 1 #convert to 0 ind   
    
            todos = functions.get_todos()                   
    
            new_to_do = input("Enter the new to do: ")
            todos[number] = new_to_do + '\n'       #edit the list   
    
            functions.write_todos(todos)     
        except ValueError:
            print("Your command is not valid!!")   #if the input is not a number
            continue

    elif user_action.startswith('complete'):   #check if the input starts with 'complete'
        try:   
            number = int(user_action[9:])   

            todos = functions.get_todos() 
        
            index = number - 1 #convert to 0 index
            to_do_to_remove = todos[index].strip('\n') #remove whitespace
            todos.pop(index)       #remove the item from the list
    

            functions.write_todos(todos)     

            message = f"Item {to_do_to_remove} was removed from the list"
            print(message)  
        except IndexError:
            print("Item number does not exist")
            continue                  

    elif user_action.startswith('exit'):   
        break 
    else:
        print("Command not found")                          
        
print("Bye!")                          



    