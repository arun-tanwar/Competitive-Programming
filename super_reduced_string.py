string = input()
result = ''
data = [string[0]]
for i in range(1,len(string)):
    if len(data)>0 and data[-1]==string[i]:
        data.pop(-1)
    else:
        data.append(string[i])
result = 'Empty String'
if len(data):
    result= ''.join(data)

print(result)
