#소수를 판별하는 프로그램
#타입 판별 함수 알기

number=input('숫자를 입력하시오 = ')
is_prime=True
if type(number)==int:
    print(f'{number}은 소수가 아닙니다.')
else:
    if number <2:
        print(f'{number}은 소수가 아닙니다.')
    else:
        a=2
        while a<number:
            if number%a==0:
               is_prime=False
               break
            a=a+1


        if is_prime:
           print(f'{number}은 소수입니다.')
        else:
           print(f'{number}은 소수가 아닙니다.')