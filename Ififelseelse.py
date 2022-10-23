num = int(input('enter any number:'))


if(num >= 90 and num <= 100): 
    print(f'Nilai {num} mendapatkan A')
elif(num >= 80 and num <= 89):
    print(f'Nilai {num} mendapatkan B')
elif(num >= 70 and num <= 79):
    print(f'Nilai {num} mendapatkan C')
elif(num >= 60 and num <= 69):
    print(f'Nilai {num} mendapatkan D')
elif(num <= 59):
    print(f'Nilai {num} mendapatkan F')
else:
    print("error")

