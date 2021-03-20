def get_key_by_key(key, needed_dict):



    for key, value in needed_dict.items():
        if key == key:
            return key



def get_key_by_val(val, needed_dict):

    for key, value in needed_dict.items():
        if val == value:
            return key


def get_name_dict(needed_list):
    name_dict = {}
    for person in needed_list:
        name_dict[person[0]] = []
    for person in needed_list:
        name_dict[person[0]].append(person)
    return name_dict


def thesaurus_adv(args):

    name_dict = {}


    for person in args:
          person = person.split()
          name_dict[person[1][0]] = []

    for key, value in name_dict.items():
        for person in args:
              person = person.split()
              full_name= " "
              if person[1][0] == key:
                name_dict[person[1][0]].append(full_name.join(person))

    print(name_dict)

    for key,val in name_dict.items():
        name_dict[key] = get_name_dict(name_dict[key])






    return name_dict

print(thesaurus_adv(["Anatoliy Gorbachev", "Bodrey Grebnitskiy", "Afanasiy Igorevich", "Zuzya Molochkova"]))
