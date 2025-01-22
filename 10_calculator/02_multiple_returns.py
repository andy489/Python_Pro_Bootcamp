def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formatter_f_name = f_name.title()
    formatter_l_name = l_name.title()

    return f"Result: {formatter_f_name} {formatter_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
