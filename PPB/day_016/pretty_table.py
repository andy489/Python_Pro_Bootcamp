# Python Package Index: https://pypi.org/

# PyCharm -> Settings..-> Project: {ProjectName} -> Python Interpreter -> +

from prettytable import PrettyTable

table = PrettyTable()

# Row by row...
# table.row = PrettyTable()
# table.row.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.row.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.row.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.row.add_row(["Darwin", 112, 120900, 1714.7])
# table.row.add_row(["Hobart", 1357, 205556, 619.5])
# table.row.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.row.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.row.add_row(["Perth", 5386, 1554769, 869.4])

# Column by column...
table.add_column("City name",
                 ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
table.add_column("Area",
                 [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population",
                 [1_158_259, 1_857_594, 120_900, 205_556, 4_336_374, 3_806_092, 1_554_769])
table.add_column("Annual Rainfall",
                 [600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

# A mix of both!
# table.field_names = ["City name", "Area"]
# table.add_row(["Adelaide", 1295])
# table.add_row(["Brisbane", 5905])
# table.add_row(["Darwin", 112])
# table.add_row(["Hobart", 1357])
# table.add_row(["Sydney", 2058])
# table.add_row(["Melbourne", 1566])
# table.add_row(["Perth", 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# table.add_column("Annual Rainfall", [600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

table.align = "r"
table.align["City name"] = "l"

print(table)
