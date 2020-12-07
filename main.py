import os

print("Type 'help' to get help")
while True:
    user_input = input(": ")
    if "cd" in user_input:
        input_cd = user_input[3:]
        print(input_cd)
    elif "mkdir" in user_input:
        input_mkdir = user_input[6:]
        print("mkdir:", input_mkdir)
    elif "touch" in user_input:
        input_touch = user_input[6:]
        print(input_touch)
    elif user_input == "pwd":
        print("pwd")
    elif user_input == "help":
        print("All commands need to be followed by a space before you enter the name, except for commands that don't"
              "\nuse any names followed by a command. For example, this is correct: 'touch filename.txt'. "
              "\nThis is NOT correct, touchfilename.txt. And commands like 'pwd' does not take any arguments, example;"
              "\nthis is correct, 'pwd'. This is NOT correct, 'pwd home'. ")
        print("\nEnter 'ls' to see directories and files in current working directory")
        print("Enter 'cd' followed by the directory name to go to that directory.")
        print("Enter 'cd' followed by '..' to go up a directory.")
        print("Enter 'mkdir' followed by the desired name to create a directory with the given name.")
        print("Enter 'touch' followed by the desired name to create a file with the given name.")
        print("Enter 'pwd' to see your current working directory")
    else:
        print("Invalid input")