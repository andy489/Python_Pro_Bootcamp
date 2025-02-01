# FileNotFoundError
file = None
try:
    file = open("b_file.txt")
    a_dict = {"key": "value"}
    # value = a_dict["non_existing_key"]
except FileNotFoundError:
    file = open("b_file.txt", "w")
except KeyError as error_msg:
    print(f"The key {error_msg} key does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
