"""
file i/o(input / output): 파일 입출력

f = open("file_path", "option")
f.read() / f.write()
f.close()
"""
print()
# 파일 열고 닫기 1

f = open("file.txt", "r")
file = "파일 작업"
f.close()

# ------------------------------------------------------------

# 파일 열고 닫기 2
with open("file.txt", "r") as f:
    file = "파일작업"

# ------------------------------------------------------------

# 파일 문자열 읽기
with open("file.txt", "r") as f:
    contents = f.read()
    # print(contents)

# ------------------------------------------------------------

# 파일 라인 단위 읽기
with open("file.txt", "r") as f:
    while contents:
        contents = f.readline()
        # print(contents)

# ------------------------------------------------------------

# 파일 모든 라인 읽기
contents = None
with open("file.txt", "r") as f:
    contents = f.readlines()
    for content in contents:
        print(content)


# ------------------------------------------------------------

# 파일 이어쓰기
with open("file.txt", "a") as f:
    contents = "a를 사용하면 이어쓰기"
    f.write(contents)

# ------------------------------------------------------------

# 파일 덮어쓰기
with open("file.txt", "w") as f:
    contents = "조재현\n010-1234-5678"
    f.write(contents)

# ------------------------------------------------------------

# 파일 모든 라인 덮어쓰기
with open("file.txt", "w") as f:
    contents = ["cho jaehyeon\n", "010-3262-9198"]
    f.writelines(contents)
