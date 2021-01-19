import copy  # deepcopy를 사용하기 위한 copy 모듈을 임포트

x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x)  # x를 y로 깊은 복사
x[0][1] = 9
print(x)  # 대입된 9가 출력됨
print(y)  # y 배열은 영향을 받지 않음
