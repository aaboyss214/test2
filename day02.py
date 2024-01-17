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
    ################################짝수로는 나눌 필요없다
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
    ################################여기선 간소화해야한다
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
                i=2
                while i*i < number:  #####계산 과정을 줄인 것 한 번 다시 생각해보자
                    if number % i == 0:
                        is_prime = False
                        break
                    i=i+1
                if is_prime:
                    print(number, end=' ')
        print()
    ################################
    elif input_number == '5':
        print("Program ends")
        break
    ################################
    else:
        print('You choosed wrong number. Choose in 1,2,3,4,5')

# ###6.1
# for i in [3,2,1,0]:
#   print(i)
#
# ###6.2
# guess_me = 7
# number = 1
#
# while 1:
#   if number < guess_me:
#        print('too low')
#    elif number == guess_me:
#        print('found it!')
#    else:
#        print('oops')
#        break
#    number =number+1
# ###6.3
# guess_me = 5
# for number in range(10):
#     if number < guess_me:
#         print('to low')
#     elif number == guess_me:
#         print('found it!')
#         break
#     else:
#         print('oops')
#         break

