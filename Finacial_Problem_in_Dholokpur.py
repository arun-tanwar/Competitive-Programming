for _ in range(int(input())): 
   n = int(input()) 
   price = list(map(int, input().split())) 
   span = [1] 
   stack = [0] 
   for i in range(1, len(price)): 
       if price[i] < price[stack[-1]]: 
           span.append(1) 
       else: 
           while len(stack) != 0 and price[i] >= price[stack[-1]]: 
               stack.pop() 
           if len(stack) == 0: 
               span.append(i+1) 
           else: 
               span.append(i - stack[-1]) 
       stack.append(i) 
   print(*span)
