number = input("원하는 숫자를 ,로 구분하여 입력 : ").split(",")
total=[]
for i in range(len(number)):
    if int(number[i-1])%2==0:
        total.append(int(number[i-1]))
print(f'짝수는 {total}')