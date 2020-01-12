import winreg

def DecodeKey(key):
    chars = 'BCDFGHJKMPQRTVWXY2346789'
    result = ''
    offset = 52
    
    for i in range(24,-1, -1):
        temp = 0
        for j in range(14,-1,-1):
            temp *= 256
            temp += strToInt(key[j+ offset])
            if temp / 24 <= 255:
                key[j+ offset] = temp/24
            else:
                key[j+ offset] = 255
            temp = int(temp % 24)
        result = chars[temp] + result
        
    for i in range(5,len(result),6):
        result = result[:i] + '-' + result[i:]
    return result

def strToInt(x):
    if isinstance(x, str):
        return ord(x)
    return x

def getProductKey():
    path = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
    value = 'DigitalProductID'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,path)
    result, type = winreg.QueryValueEx(key, value)
    return list(result)

print(DecodeKey(getProductKey()))
