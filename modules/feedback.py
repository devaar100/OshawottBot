def bug(data):
    file = open('bugs.txt','a')
    file.write(data + "\n")
    file.close()
    return "Thanks for the help"


def suggestions(data):
    file = open('suggestions.txt','a')
    file.write(data + '\n')
    file.close()
    return "Thanks for the input"
