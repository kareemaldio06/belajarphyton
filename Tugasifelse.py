numMATH = int(input('MATH score:'))
numENG = int(input('ENG score:'))
numINDO = int(input('INDO score:'))
numCIV = int(input('CIV score:'))
numBIO = int(input('BIO score:'))
numPHY = int(input('PHY score:'))

average = (numMATH + numENG + numINDO + numCIV + numBIO + numPHY) / 6

if(average >= 90 and average <= 100): 
    print(f'Nilai {average} mendapatkan A')
elif(average >= 80 and average <= 89):
    print(f'Nilai {average} mendapatkan B')
elif(average >= 70 and average <= 79):
    print(f'Nilai {average} mendapatkan C')
elif(average >= 60 and average <= 69):
    print(f'Nilai {average} mendapatkan D')
elif(average <= 59):
    print(f'Nilai {average} mendapatkan F')
else:
    print("error")




