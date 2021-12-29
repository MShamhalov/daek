from workspace import *
from conf import *
initconfig()

print('daek v 0.0.3, active modules: ', len(getModules()))
while True:
    command = input('> ')
    if (command == 'exit') or (command == 'quit'): break
    else: executor(command)
