prompt = raw_input("Which math module would you like to use? \nRefer to functions.txt to see the available list. Would you like to see the functions?")

if prompt.lower() == "yes":
    textfile = open("functions.txt", "r")
    print textfile.read()
    prompt = raw_input("Which math module would you like to use?")

else:
    prompt = raw_input("Which math module would you like to use?")


if prompt.lower() == "quadratic":
    import quad
if prompt.lower() == "area":
    import area
if prompt.lower() == "calculator":
    import calculator
if prompt.lower() == "average":
    import report
if prompt.lower() == "grapher" or prompt.lower() == "graph":
    import grapher
