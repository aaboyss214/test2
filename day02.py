#(섭씨°C × 9/5) + 32 = 화씨°F
#(화씨°F − 32) × 5/9 = 섭씨°C
#Celsius
#Fahrenheit
#소수를 판별하는 프로그램
#타입 판별 함수 알기
def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True 아니면 False
    """
    if n < 2:
        return False
    else:
        i=2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


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
        if isprime(RandonNumber):
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

            if isprime(number):
                print(number, end=' ')
        print('')
    ################################
    elif input_number == '5':
        print("Program ends")
        break
    ################################
    else:
        print('You choosed wrong number. Choose in 1,2,3')
