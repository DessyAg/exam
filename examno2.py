def tickets(peopleInLine):
    uang = 0

    for i in peopleInLine:
        if i < 25: 
            return 'no'
        if i == 25:
            uang += i
        elif i > 25:
            if (uang - i) < 0:
                return 'no'
            else: 
                uang +=i
    return 'yes'

print(tickets([25,100,25]))