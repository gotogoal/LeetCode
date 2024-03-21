def youxioa(s):
    res = []
    dict_match = {'(':')', '{':'}', '[':']'}
    for each in s:
        if each in dict_match:
            res.append(each)
        else:
            if not res:
                return False
            else:
                if dict_match[res[-1]] == each:
                    res.pop()
                else:
                    return False
    
    if not res:
        return True
    else:
        return False

s = "()[]{}"
print(youxioa(s))