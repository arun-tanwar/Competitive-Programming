tc=int(input())
call_ord=lst = [int(i) for i in input().split(' ')][:tc]
ide_ord=lst = [int(i) for i in input().split(' ')][:tc]
count=0
while len(call_ord):
        if((call_ord[0])==(ide_ord[0])):
            call_ord.pop(0)
            ide_ord.pop(0)
            count +=1
        else:
            ele=call_ord.pop(0)
            call_ord.append(ele)
            count +=1
print(count)
