def decapitalize(word):
    if word is not None:
        return word[0].lower() + word[1:]


def num_translate_adv(num):
    num_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре",
                "Five": "Пять", "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь",
                "Nine": "Девять", "Ten": "Десять"}

    try:
      if num == num.capitalize():
       return num_dict[num]
      else:
        num = num.capitalize()
        return decapitalize(num_dict[num])

    except KeyError:
        return "Enter a valid key"



print(num_translate_adv("Nine"))


