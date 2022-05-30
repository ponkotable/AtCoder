sa = input()
sb = input()
sc = input()
table = {'a':sa, 'b':sb, 'c':sc}
person = 'a'
while True:
    if len(table[person]) == 0:
        print(person.upper())
        exit()
    tmp_p = person
    person = table[person][0]
    table[tmp_p] = table[tmp_p][1:]
