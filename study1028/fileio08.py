import pickle

# 바이너리 파일 입력 - 객체 자체를 파일로 저장할 수 있다. (직렬화)

with open(file="study1028/bin.pickle", mode="bw") as file_editor:
    pickle.dump([1, 2, 3], file_editor)
