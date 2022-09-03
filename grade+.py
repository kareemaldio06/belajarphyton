math = 'math grade is', 60 
science = 'science grade is', 51
Civic = 'Civic Grade is', 87
English = 'English grade is', 92

GRADE = [math, science, Civic , English ]

for X in GRADE:
    if X > 91 and X <= 100:
        print(X, 'is A')
        continue
    elif X > 81 and X <= 90:
        print(X, 'is B')
        continue
    elif X > 71 and X <= 80:
        print(X, 'is C')
        continue
    elif X > 61 and X <= 70:
        print(X, 'is D')
        continue
    elif X > 0 and X <=60:
        print(X, 'is F')
        continue
    else:
        print('ERROR')


