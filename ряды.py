"""
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5 
"""
rows = int(input("сколько вывести рядов? "))
current_row = 0
while current_row < rows:
    print("1" * current_row)
    current_row += 1