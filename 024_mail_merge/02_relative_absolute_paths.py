with open("/Users/stoevand/Workspace/my/Python_Pro_Bootcamp/24_mail_merge/new_file.txt") as file:
    content = file.read()
    print(f"1: {content}")

with open("new_file.txt") as file:
    content = file.read()
    print(f"2: {content}")

with open("./../24_mail_merge/new_file.txt") as file:
    content = file.read()
    print(f"3: {content}")