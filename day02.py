#(섭씨°C × 9/5) + 32 = 화씨°F
#(화씨°F − 32) × 5/9 = 섭씨°C
#Celsius
#Fahrenheit



while 1:
    input_number = input(' Choose The Option 1)Celsius to Fahrenheit 2)Fahrenheit to Celsius 3)Prime number reader 4)Prime number reader by section 5)Quit Program ')
    if input_number=='1':
        Celsius=float(input('Celsius = '))
        print(f'Fahrenheit = {float((Celsius* 9/5)+ 32)}°F')
    ################################
    elif input_number=='2':
        Fahrenheit = float(input('Fahrenheit = '))
        print(f'Celsius = {float((Fahrenheit-32)*5/9)}°C')
    ################################
    elif input_number=='3':
        RandonNumber = int(input('Input number'))

        is_prime2 = True

        if RandonNumber < 2:
            print('This is not prime number')
        else:
            for a in range(2, RandonNumber):
                if RandonNumber % a == 0:
                    is_prime2 = False
                    break
            if is_prime2:
                print('This is prime number')
            else:
                print('This is not prime number')
    ################################
    elif input_number == '4':
        section = input('input numbers').split()
        n1 = int(section[0])
        n2 = int(section[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                continue
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=' ')
        print('')
    ################################
    elif input_number == '5':
        print("Program ends")
        break
    ################################
    else:
        print('You choosed wrong number. Choose in 1,2,3')
