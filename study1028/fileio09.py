import pickle

# 바이너리 파일 출력 - 다시 가져와보면 (역직렬화)

with open(file="study1028/bin.pickle", mode="br") as file_editor:
    my_list = pickle.load(file_editor)

print = (my_list)
