import random

def get_jokes(amount):

    """
    get_jokes принимает int - количество шуток
    Собирает шутки из 3 листов в предложения без повторений слов

    """
    for joke in range(0, amount):
        sentence = " "
        noun = nouns.pop(random.randint(0, len(nouns)-1))
        adverb = adverbs.pop(random.randint(0, len(adverbs)-1))
        adjective = adjectives.pop(random.randint(0, len(adjectives)-1))
        joke_list = [noun, adverb, adjective]
        joke = sentence.join(joke_list)
        print(joke)



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



get_jokes(5)








