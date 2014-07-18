def rankStr(texts, d):
    s = texts
    strLen = len(s)
    for i in range(2 * (d + 1)): s += "."
    dic = {}
    for i in range(strLen):
        Str = s [i : (i + d + 1)]
        dic[Str] = i
    keyList = sorted(dic)
    print(keyList)
    pos = []
    for key in keyList:
        pos.append(dic[key])
    return pos


print(rankStr('四是四十是十十四是十四四十是四十', 5))

