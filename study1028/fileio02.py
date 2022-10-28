
# 파일 읽기- read() 파일 내용을 하나의 문자열에 담는다.

file_editor = open(file="study1028/test.txt", mode="r", encoding="utf-8")

text = file_editor.read()

file_editor.close()

print(text)
