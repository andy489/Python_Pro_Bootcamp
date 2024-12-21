# FileNotFoundError
try:
    with open("a_file.txt") as file:
        file.read()
except FileNotFoundError:
    print("No such file")

#KeyError
a_dict = {"key":"value"}
try:
    value = a_dict["non_existing_key"]
except KeyError:
    print("No such key")

#IndexError
fruit_list=["Apple", "Banana", "Pear"]
try:
    fruit = fruit_list[3]
except IndexError:
    print("No such index")

# TypeError
text = "abc"
try:
    print(text / 5)
except TypeError:
    print("Cannot operate with strings like that")

# try: Something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no mater what happens (clean up)

file= None
try:
    file = open("a_file.txt")
    a_dict = {"key":"value", "asd":"asd"}
    print(a_dict["asd"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"That key {error_msg} does not exist.")
else:
    content = file.read()
    print(f"Content: {content}")
finally:
    file.close()
    print("File was closed.")

# raise: Raise an exception

# raise TypeError("This is an error that I made up.")