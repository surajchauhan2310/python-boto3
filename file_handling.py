# import os

# # with open("readme.txt", 'a') as file:
# #     file.write("\n" + "hello from python!")

# # with open("readme.txt", 'r') as file:
# #     print(file.read())

# # os.remove("readme.txt")

# def write_file(file_name, content):
#     with open(file_name, 'w') as file:
#      file.write(content)

# fileName = input("please provide the file name ")

# userInput = input("write 'w' to write the file, type 'a' to append the file, type 'r' to read the file, type 'd' to delete the file.")


# if userInput == 'w':
# # if userInput == 'w':
#     userContent = input("please provide the content..")
#     write_file(fileName, userContent)

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def delete_file(file_name):
    import os
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file does not exist.")

fileName = input("Please provide the file name: ")

userInput = input("Write 'w' to write the file, 'a' to append the file, 'r' to read the file, 'd' to delete the file: ")

if userInput == 'w':
    userContent = input("Please provide the content to write: ")
    write_file(fileName, userContent)
elif userInput == 'a':
    userContent = input("Please provide the content to append: ")
    append_file(fileName, userContent)
elif userInput == 'r':
    print("File contents:")
    print(read_file(fileName))
elif userInput == 'd':
    delete_file(fileName)
else:
    print("Invalid option!")
