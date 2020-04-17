def calc(a, b, operator):
  if operator == 'add':
      ans=float( a+ b)
      return ans
  elif operator == 'subtract':
      ans=float( a- b)
      return ans
  elif operator == 'division':
      if(b==0):
          print("zero division error ...will lead to infinite")
          return;
      ans = float(a / b)
      return ans
x=float(input("enter first no. for operation"))
y=float(input("enter second no. for operation"))
z=input("enter mode of operation")
result=calc(x,y,z)
print("result is "+str(result))
