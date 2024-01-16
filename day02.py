#소수를 판별하는 프로그램
#타입 판별 함수 알기

number=int(input('숫자를 입력하시오 = '))
is_prime=True

if number <2:
    print(f'{number}은 소수가 아닙니다.')
else:
    for i in range(2, number):
        if number%i==0:
           is_prime=False
           break

    if is_prime:
       print(f'{number}은 소수입니다.')
    else:
       print(f'{number}은 소수가 아닙니다.')