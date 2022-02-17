import os

# opening the file
try:
    file_location = input("Whats the location of the file?\n")
    my_file = open(file_location, "r")

except IOError:
    print("The given file name / path is incorrect.")
finally:
    pass

# showing the contents of the file
print("Contents of the file:\n", my_file.read())
file1 = open("my_file.txt").read().splitlines()


# creating the second file and converting F to C
file2 = open("my_file2.txt", "w", encoding='utf8')
try:
    for line in file1:
        if "F" in line:
            file2.write(line + '\n')
        else:
            file2.write(str(((float(line[:-1]) * 9) / 5) + 32) + 'F' + '\n')
    file2.close()
except ValueError:
    print("Incorrect format of the file.")

