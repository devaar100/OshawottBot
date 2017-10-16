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


def getBugData():
    file = open("bugs.txt",'r')
    txt = file.read()
    file.close()
    return txt

def getSuggestionData():
    file = open("suggestions.txt",'r')
    txt = file.read()
    file.close()
    return txt