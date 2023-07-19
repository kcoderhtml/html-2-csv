with open("prizelist.txt") as file:
    contents = file.read()
    contents = contents.splitlines()

    csv = ""
    for i in range(0, len(contents)):
        if i % 2 == 1:
            temp = "\'" + contents[i-1] + "\', \'" + contents[i] + "\'"
            if i != len(contents):
                temp += "\n"
            csv += temp
print(csv)
with open("prizelist.csv", "w") as f:
    f.write(csv)