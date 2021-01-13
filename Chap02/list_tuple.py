# 리스트의 기초
# 기본 사용
list01 = []  # 빈 리스트
list02 = [1, 2, 3]
list03 = ["A", "B", "C"]
print(list01)
print(list02)
print(list03)
print()

# 다양한 자료형 객체 사용
list04 = list()  # 빈 리스트
list05 = list("ABC")
list06 = list([1, 2, 3])  # 리스트로부터
list07 = list((1, 2, 3))  # 튜플로부터
list08 = list({1, 2, 3})  # 집합으로부터
print(list04)
print(list05)
print(list06)
print(list07)
print(list08)
print()

# 특정 범위 사용
list09 = list(range(7))
list10 = list(range(3, 8))
list11 = list(range(3, 13, 2))
print(list09)
print(list10)
print(list11)
print()

# None 사용
list12 = [None] * 5  # 원소가 5개이면서 원소값이 없는 리스트
print(list12)
print()

# 튜플의 기초
# 기본 사용
tuple01 = ()
tuple02 = (1,)
tuple03 = (1,)
print(tuple01)
print(tuple02)
print(tuple03)
print()

# 결합 연산자 생략
tuple04 = 1, 2, 3
tuple05 = (
    1,
    2,
    3,
)
tuple06 = (1, 2, 3)
tuple07 = (
    1,
    2,
    3,
)
tuple08 = "A", "B", "C"
print(tuple04)
print(tuple05)
print(tuple06)
print(tuple07)
print(tuple08)
print()

# 단일 값을 갖는 변수의 예
v01 = 1
v02 = 1
print(v01)
print(v02)
print()

# tuple() 사용
tuple09 = tuple()  # 빈 튜플
tuple10 = tuple("ABC")
tuple11 = tuple([1, 2, 3])  # 리스트로부터
tuple12 = tuple({1, 2, 3})  # 집합으로부터
print(tuple09)
print(tuple10)
print(tuple11)
print(tuple12)
print()

# 특정 범위 사용
tuple13 = tuple(range(7))
tuple14 = tuple(range(3, 8))
tuple15 = tuple(range(3, 13, 2))
print(tuple13)
print(tuple14)
print(tuple15)
print()

# 리스트와 튜플 풀어내기(Unpack)
x = [1, 2, 3]  # 리스트 x 선언
a, b, c = x  # x를 언팩하여 변수 a, b, c에 대입
print(a, b, c)
print()

# 인데스식 사용하기
x = [11, 22, 33, 44, 55, 66, 77]
print(x[2])  # 앞에서 3번재 원소 출력
print(x[-3])  # 뒤에서 3번째 원소 출력
print()
x[-4] = 3.14  # 뒤에서 4번째 원소에 새로운 값을 대입
print(x)
# print(x[7])  # IndexError: list index out of range
# print(x[7] = 3.14)        # IndexError: list assignment index out of range
print()

# 슬라이식으로 원소 꺼내기
s = [11, 22, 33, 44, 55, 66, 77]
print(s[0:6])  # 0번째 원소 ~ 5번째 원소 출력
print(s[0:7])  # 0번째 원소 ~ 6번재 원소 출력
print(s[0:7:2])  # 0번째 원소 ~ 6번째 원소 중 2씩 건너뛰며 출력
print(s[-4:-2])  # 뒤에서 4번째 원소 ~ 뒤에서 2번째 원소 출력
print(s[3:1])  # j값이 i값보다 작지만 오류는 안남
print()

# 뮤터블과 이뮤터블의 대입
n = 5  # n에 int형 정수값 5 대입
print(id(n))  # 식별 번호 출력
n = "ABC"  # n에 str형 문자열 'ABC' 대입
print(id(n))  # 식별 번호 출력
print()

# 변수 여러 값을 한꺼번에 대입
a, b, c = 1, 2, 3  # a, b, c에 1, 2, 3을 대입하여 변숫값을 출력
print(a)
print(b)
print(c)
print()

# 응용
x = 6
y = 2
x, y = y + 2, x + 3  # x에 (y+2)를 대입하고 y에 (x+3)을 대입
print(x)
print(y)
print()

# 누적 대입으로 변수 값 증가
n = 12
print(id(n))  # 식별 번호 출력
n += 1  # n 값을 1 증가
print(id(n))  # 식별 번호 출력
print()

# 대입 기호 =
x = 0
print(type(x + 17))  # <class 'int'>
# print(type(x=17))  # TypeError: type() takes 1 or 3 arguments
print()

# len() 함수로 배열의 원소 수 구하기
x = [15, 64, 7, 3.14, [32, 55], "ABC"]
print(len(x))
print()

# 비교 연산자로 배열의 대소 또는 등가 관계 판단하기
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] < [1, 2, 4])  # True
print([1, 2, 3, 4] <= [1, 2, 3, 4])  # True
print([1, 2, 3] < [1, 2, 3, 5])  # True
print([1, 2, 3] < [1, 2, 3, 5] < [1, 2, 3, 5, 6])  # True / and 결합
print()

# 내포 표기 생성
numbers = [1, 2, 3, 4, 5]
twise = [num * 2 for num in numbers if num % 2 == 1]  # 리스트 numbers의 홀수 원소값을 +2한 리스트 생성
print(twise)
print()