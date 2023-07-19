indicator = "                            &nbsp;&nbsp;&nbsp;&nbsp;"

def dump_relevant_lines(file, indicator):
    temp = []
    with open(file) as file:
        contents = file.read()
        contents = contents.splitlines()

        for line in contents:
            if line.__contains__(indicator):
                temp.append(line.replace(indicator, ""))
    return temp

def convert_to_csv(temp):
    csv = ""
    for i in range(0,len(temp)):
        if i % 2 == 1 or i == 1:
            csv += "\'" + temp[i-1] + "\', \'" + temp[i] + "\'"
            if i < len(temp) - 1:
                csv += "\n"
    return csv

csv = convert_to_csv(dump_relevant_lines("prizelist.html", indicator))

print(csv)

with open("prizelist.csv", "w") as f:
    f.write(csv)