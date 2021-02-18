p=input()
a=p.count('(')
b=p.count(')')
stack=[]

for i in p[1:-1]:
    if i=='(':
        stack.append(i)
    if i==')':
        stack.pop()

if not stack:
    print ("empty")

if stack:
    print("not empty")