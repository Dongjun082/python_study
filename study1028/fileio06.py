
# with() 에디터를 일일이 close 하기 어려울 경우 with를 사용한다.(객체를 제거한다.)

with open(file="study1028/test.txt", mode="r", encoding="utf-8") as file_editor:
    text = file_editor.read()

print(text)
