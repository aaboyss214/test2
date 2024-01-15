#(섭씨°C × 9/5) + 32 = 화씨°F
#(화씨°F − 32) × 5/9 = 섭씨°C
#Celsius
#Fahrenheit

input_number='1'
Celsius = 0.0
Fahrenheit = 0.0  #변수 초기화

while input_number in {'1','2'}:
    input_number = input(' Choose The Option 1)Celsius to Fahrenheit 2)Fahrenheit to Celsius 3)Quit Program')
    if input_number=='1':
        Celsius=float(input('Celsius = '))
        Fahrenheit=float((Celsius* 9/5)+ 32)
        print(f'Fahrenheit = {Fahrenheit}°F')
    elif input_number=='2':
        Fahrenheit = float(input('Fahrenheit = '))
        Celsius=float((Fahrenheit-32)*5/9)
        print(f'Celsius = {Celsius}°C')
    elif input_number=='3':
        print("Program ends")
        break
    elif (input_number in {'1','2','3'})==0:
        print('You choose wrong number. Choose in 1,2,3')
