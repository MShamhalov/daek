from workspace import *

from conf import initconfig
initconfig()

while True:
    command = input('> ')
    if (command == 'exit') or (command == 'quit'): break
    else: executor(command)
