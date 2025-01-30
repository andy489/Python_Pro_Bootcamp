# file = open("quote.txt")
#
# contents = file.read()
# print(contents)
# file.close()

# with open("quote.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("quote.txt", mode="a") as file:
#     file.write("\n\nProgramming is learned by writing programs.\n― Brian Kernighan")

with open("new_file.txt", mode="w") as file:
    file.write("New text.")