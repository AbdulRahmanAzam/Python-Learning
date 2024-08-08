def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{i} x {n} = {i * n}\n"

    with open(f"Chapter 9/13yearold/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)