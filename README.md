# jsonvalidator

This JSON validator is a basic python script for checking if a file is of JSON format or not
1) The code first requires the user to input the file along with the file path
2) It checks if it is a valid file path with os.path.isfile(file_path) and only then proceeds to checking if it is JSON
3) The file is then opened and read into a string
4) This string is then checked for JSON,  json.loads(ini_string) which basically parses a JSON string. 
(refer: https://pynative.com/python-json-load-and-loads-to-parse-json/)

Alternatively instead of reading the file into a string, We can directly use json.load(text_file).
