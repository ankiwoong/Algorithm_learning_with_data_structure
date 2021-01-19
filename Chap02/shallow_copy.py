x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()  # x를 y로 얕은 복사
x[0][1] = 9
print(x)
print(y)