import os 
choice = 0
filename = '' 
def menu(): 
    global choice 
    print('Menu\n 1.0pen Calculator\n 2.0pen Notepad\n 3.Open bluestacks\n 4.Exit ')
    choice = input('Select Menu :')  
    
def opennotepad(): 
    filename = 'C:\\Windows\\SysWOW64\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Calculate Number %s' %filename) 
    os. system(filename)

def openbluestacks():
    filename = 'C:\\Programs Flies\\BlueStacks\\Bluestacks.exe'
    print('Calculate Number %s' %filename) 
    os. system(filename)  

while True: 
    menu()
    if choice == '1': 
        opencalculator() 
    elif choice == '2': 
        opennotepad()
    elif choice == '3':
        openbluestacks()
    else: 
        break
Aa