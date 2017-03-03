def main():
    f = open("nat", 'r')
    a = []
    b = []
    for line in f:
        line_list = line.strip().split(" ")  # strip():忽略空格和换行符
        a.append(line_list[4])
        a.append(line_list[6])
        b.append(a)
        a = []
    f.close()
    # print(b[0][1])
    new = open("new-nat", 'w')
    for i in b:
        if '58.83' in i[0] and ('10.1.19' in i[1] or '10.1.18' in i[1] or '10.1.20' in i[1]):  # 取出含有58.83的行，放入新文本
            temp = i[0] + "                  " + i[1] + "\n"
            new.write(temp)
        else:
            pass
    new.close()
    return


main()
