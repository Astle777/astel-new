def pal():
   s="Apple  Malayalam  Mom  Knife"
   n=len(s)
   m=s[n::-1]
   if(s==m):
      print(s,"is palidrome")
   else:
    print(s,"is not palidrome")
pal()   