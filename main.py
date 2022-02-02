import os

# opening the file
try:
    my_file = open("my_file.txt", "r")

except IOError:
    print("The given file name / path is incorrect.")
finally:
    pass

# asking the user if he wants to know the file path
choice = True
while choice:
    x = input("Do you want to know the location of the file? \n y/n \n")
    if x == "y":
        print("The path of the file is: ", os.path.abspath("my_file.txt"))
        choice = False
    elif x == "n":
        print("Ok. Moving forward...")
        choice = False
    else:
        pass

# showing the contents of the file
print("Contents of the file:\n", my_file.read())
file1 = open("my_file.txt").read().splitlines()


# creating the second file and converting F to C
file2 = open("my_file2.txt", "w")

for line in file1:
    if "F" in line:
        file2.write(line + '\n')
    else:
        file2.write(str(((float(line[:2]) * 9) / 5) + 32) + 'F' + '\n')
print(file2.readlines())
file2.close()

