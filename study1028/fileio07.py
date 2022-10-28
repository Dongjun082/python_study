
# 바이너리 파일 실행

with open(file="study1028/bin.txt", mode="bw") as file_editor:
    file_editor.write(b"aa")

# 확장자 중요한게 아닌 안에 확장자가 중요
# 오픈할때는 encoding을 넣으면 안됨
