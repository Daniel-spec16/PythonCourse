procent = input()
list = list(map(int, str(procent)))
procenT = [1]
procentA = [2,3,4]
procentOV = [5,6,7,8,9,0]

if list[len(list)-1] in procenT:
    print(procent, "Процент")
elif list[len(list)-1] in procentA and list[len(list)-2] in procenT:
    print(procent, "Процентов")
elif list[len(list)-1] in procentA:
    print(procent, "Процента")
elif list[len(list)-1] in procentOV:
    print(procent, "Процентов")
