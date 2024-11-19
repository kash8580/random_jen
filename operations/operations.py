def rev(s):
    return s[::-1]

def palin(s):
    s.lower().replace(' ','')
    return s==s[::-1]
