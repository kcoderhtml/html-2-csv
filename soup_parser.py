# return lines mathing indicator
def dump_relevant_lines(file, indicator):
    temp = []
    with open(file) as file:
        contents = file.read()
        contents = contents.splitlines()

        for line in contents:
            if line.__contains__(indicator):
                temp.append(line.replace(indicator, ""))
    return temp

# convert array to csv
def convert_to_csv(temp):
    csv = ""
    for i in range(0,len(temp)):
        if i % 2 == 1 or i == 1:
            csv += "\"" + temp[i-1] + "\", \"" + temp[i] + "\""
            if i < len(temp) - 1:
                csv += "\n"
    return csv

# deduplicate string
def dedup(data):
    newdata = []
    data = data.splitlines()
    for i in range(0, len(data)):
        if (data.count(data[i]) == 1 & newdata.count(data[i]) < 1):
            newdata.append(data[i])
        elif (newdata.count(data[i]) < 1):
            newdata.append(data[i])
    return newdata

# add new lines and convert arrayy to string
def array_to_str(array):
    string = ""
    for i in range(0,len(array)):
        string += array[i]
        if i < len(array) - 1:
            string += "\n"
    return string