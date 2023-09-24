from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squitle", "Water"],
        ["Bulbasaur", "Grass"],
        ["Charmander", "Fire"],
        ["Eevee", "Normal"],
    ]
)
table.align = "l"
print(table)
