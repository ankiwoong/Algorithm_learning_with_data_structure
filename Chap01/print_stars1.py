# * 를 n 개 출력하되 w개마다 줄바꿈하기 1

print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈할까요?: "))

for i in range(n):  # n 번 반복
    print("*", end="")
    if i % w == w - 1:  # n 번 판단
        print()  # 줄바꿈

if n % w:  # 1번 판단
    print()  # 줄바꿈
