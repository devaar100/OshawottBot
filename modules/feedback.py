def bug(data):
    file = open('bugs.txt','a')
    file.write(data)
    file.close()
    return "Thanks for your input"

def suggestions(data):
    file = open('suggestions.txt','a')
    file.write(data)
    file.close()
    return "Thanks for the input"