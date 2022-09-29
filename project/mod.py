file_data = ""
file = "./apk_list_zh60.txt"
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n') + " 0 1\n"
        file_data += line
with open(file, "w", encoding="utf-8") as f:
    f.write(file_data) 