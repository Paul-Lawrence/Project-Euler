s = ''
i = 1
while len(s)<1000000:
    s = s + f'{i}'
    i+=1
print(s[0])
print(int(s[0])*int(s[0])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999]))