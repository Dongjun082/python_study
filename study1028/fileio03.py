
# readline() 파일의 내용을 한줄씩 가져온다.

file_editor = open(file="study1028/test.txt", mode="r", encoding="utf-8")

text = file_editor.read()
text1 = file_editor.read()

file_editor.close()

print(text)
print(text1)
