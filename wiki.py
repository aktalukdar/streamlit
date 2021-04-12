import wikipedia
import random
def getData(a):
    if(a==""):
        return "Please enter any input."
    try:
        wiki_topic = wikipedia.search(a)
        page = wikipedia.page(title=wiki_topic,auto_suggest=True,redirect=True, preload=False)
        return page.content
    except wikipedia.exceptions.PageError as error:
        return "No Page could be found with the topic you entered!"
    except wikipedia.exceptions.DisambiguationError as e:
        return "Please be more specific with your search query as there are a couple of other options meaning the same."
