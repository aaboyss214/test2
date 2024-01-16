#소수를 판별하는 프로그램
#타입 판별 함수 알기

numbers=input('숫자를 입력하시오 = ').split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2 + 1):
    is_prime=True

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
               is_prime = False
               break
        if is_prime:
            print(number, end=' ')