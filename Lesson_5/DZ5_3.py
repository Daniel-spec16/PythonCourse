import itertools
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#klasses = set(klasses)
#tutors = set(tutors)
klasses = klasses[:(len(tutors))]

tutors_klasses_gen = itertools.zip_longest(tutors, klasses, fillvalue = None)
print(*list(tutors_klasses_gen))


