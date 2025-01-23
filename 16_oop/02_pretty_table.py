from prettytable import PrettyTable

# pypi.org
# https://pypi.org/project/prettytable/

table = PrettyTable()
table.add_column("City name", ["Varna", "Plovdiv", "Burgas"])
table.add_column("Population", [f"{332_394:,}", f"{342_048:,}", f"{198_593:,}"])

table.align["City name"] = "l"
table.align["Population"] = "r"

print(table)
