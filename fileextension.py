# Write a Python program to accept a filename from the user and print the extension of that.

filename = input("Input the Filename: ")
file_extension = filename.split(".")
print("The extension of the file is : " + repr(file_extension[-1]))
