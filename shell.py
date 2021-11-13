from workspace import *

while True:
    command = input('> ')

    if (command == 'exit') or (command == 'quit'):
        break
    else: 
        executor(command)
    
    #command = input('_check_ > ')
    #checker(command)
