def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    formatter_f_name = f_name.title()
    formatter_l_name = l_name.title()

    return f"{formatter_f_name} {formatter_l_name}"


print(format_name("andrey", "STOEV"))
