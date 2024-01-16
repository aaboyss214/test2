#(섭씨°C × 9/5) + 32 = 화씨°F
#(화씨°F − 32) × 5/9 = 섭씨°C
#Celsius
#Fahrenheit



while 1:
    input_number = input(' Choose The Option 1)Celsius to Fahrenheit 2)Fahrenheit to Celsius 3)Quit Program')
    if input_number=='1':
        Celsius=float(input('Celsius = '))
        print(f'Fahrenheit = {float((Celsius* 9/5)+ 32)}°F')
    elif input_number=='2':
        Fahrenheit = float(input('Fahrenheit = '))
        print(f'Celsius = {float((Fahrenheit-32)*5/9)}°C')
    elif input_number=='3':
        print("Program ends")
        break
    else:
        print('You choosed wrong number. Choose in 1,2,3')
