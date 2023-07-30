def dump_relevant_lines(file, indicator):
    """
    Given a file and an indicator string, returns a list of lines from the file that contain the indicator string.

    Args:
    - file (str): the path to the file to read
    - indicator (str): the string to search for in the file

    Returns:
    - list: a list of lines from the file that contain the indicator string
    """
    temp = []
    with open(file) as file:
        contents = file.read()
        contents = contents.splitlines()

        for line in contents:
            if line.__contains__(indicator):
                temp.append(line.replace(indicator, ""))
    return temp

def convert_to_csv(temp):
    """
    Given a list of strings, returns a CSV-formatted string with every two strings in the list as a row.

    Args:
    - temp (list): a list of strings

    Returns:
    - str: a CSV-formatted string with every two strings in the list as a row
    """
    csv = ""
    for i in range(0,len(temp)):
        if i % 2 == 1 or i == 1:
            csv += "\"" + temp[i-1] + "\", \"" + temp[i] + "\""
            if i < len(temp) - 1:
                csv += "\n"
    return csv

def dedup(data):
    """
    Given a string, returns a list of unique lines from the string.

    Args:
    - data (str): the string to deduplicate

    Returns:
    - list: a list of unique lines from the string
    """
    newdata = []
    data = data.splitlines()
    for i in range(0, len(data)):
        if (data.count(data[i]) == 1 & newdata.count(data[i]) < 1):
            newdata.append(data[i])
        elif (newdata.count(data[i]) < 1):
            newdata.append(data[i])
    return newdata

def array_to_str(array):
    """
    Given a list of strings, returns a string with each string on a new line.

    Args:
    - array (list): a list of strings

    Returns:
    - str: a string with each string on a new line
    """
    string = ""
    for i in range(0,len(array)):
        string += array[i]
        if i < len(array) - 1:
            string += "\n"
    return string
