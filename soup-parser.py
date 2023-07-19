with open("prizelist.html") as file:
    contents = file.read()
    contents = contents.splitlines()
    csv = ""
    temp = ""

    for line in contents:
        if line.__contains__("&nbsp;&nbsp;&nbsp;&nbsp;"):
            temp = line.replace("                            &nbsp;&nbsp;&nbsp;&nbsp;", "")
            print(temp)
            # if i % 2 == 1:
            #     temp = "\'" + contents[i-1] + "\', \'" + contents[i] + "\'"
            #     if i != len(contents):
            #         temp += "\n"
            #     csv += temp
# print(csv)
# with open("temp.csv", "w") as f:
#     f.write(csv)