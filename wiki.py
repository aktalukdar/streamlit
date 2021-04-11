import wikipedia
import random
def getData(a):
    result = wikipedia.search(a)
    page = wikipedia.page(result[0], preload= True)
    return page.content