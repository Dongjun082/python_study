# range 함수

# temp = list(range(10))

# print(temp)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# temp = list(range(5, 10))

# print(temp)

# [5, 6, 7, 8, 9]

# temp = list(range(3, 30, 3))

# print(temp)

# [3, 6, 9, 12, 15, 18, 21, 24, 27]


# temp = list(range(1, 10))

# for item in temp:
#     print("안녕")

# temp = [item for item in range(0, 10)]
# temp = {"안녕" for item in range(0, 10)} set의 경우 1번만 출력
# {'안녕'}
temp = ["안녕" for item in range(0, 10)]
# ['안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕']

print(temp)
