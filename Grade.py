# IF GRADE
# 91~100 = A
# 81~90 = B
# 71~80 = C
# 61~70 = E
# 0~60 = F
# <0 OR >100 = ERROR, GRADE NOT POSSIBLE 

GRADE = 60 

if GRADE > 91 and GRADE <= 100:
    print('The grade is A')
elif GRADE > 81 and GRADE <= 90:
    print('The grade is B')
elif GRADE > 71 and GRADE <= 80:
    print('The grade is C')
elif GRADE > 61 and GRADE <= 70:
    print('The grade is E')
elif GRADE > 0 and GRADE <= 60:
    print('The grade is F')
else:
    print('ERROR, GRADE NOT POSSIBLE')
