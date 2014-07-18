def rankStr(texts, d):
    s = texts
    strLen = len(s)
    for i in range(2 * (d + 1)): s += "一"
    for i in range(strLen):
        Str = ""
        for j in range(d + 1):
            Str += s[i + j]
        dic[Str] = i;
    sorted(dic)
    pos = [];
    for key, val in dic:
        pos.append(val)
    return pos
}


    
