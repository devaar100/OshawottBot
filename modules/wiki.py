import wikipedia


def get_wiki(data):
    try:
        return wikipedia.summary(data, sentences=4)
    except wikipedia.exceptions.DisambiguationError:
        return "Please be more specific"

