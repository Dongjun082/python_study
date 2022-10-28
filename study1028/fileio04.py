
# readlines() 파일을 한줄씩 리스트로 가져온다.

file_editor = open(file="study1028/test.txt", mode="r", encoding="utf-8")

text_list = file_editor.readlines()

file_editor.close()

print(text_list)
