# 따로따로 생성한 리스트, 튜플의 동일성 판단하기
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print(list1 is list2)
print()

# 리스트, 튜플의 대입
list1 = [1, 2, 3, 4, 5]
list2 = list1
print(list1 is list2)

list1[2] = 9
print(list1)
print(list2)
print()