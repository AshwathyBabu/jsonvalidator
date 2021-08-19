import json
import os
# ask for input file name to be tested
print("Please input the file to be checked:")
file_path=input()

# check if file is present
if os.path.isfile(file_path):
    # open text file in read mode
    text_file = open(file_path, "r")

    # read whole file to a string
    ini_string = text_file.read()

    # close file
    text_file.close()

    # checking if the string is JSON or not
    try:
        json_object = json.loads(ini_string)
        print(file_path+", is a valid JSON file")
    except ValueError as e:
        print(file_path+", is NOT a valid JSON file")

# If file is not present in the path
else:
    print(file_path + "-> File does not exist")
