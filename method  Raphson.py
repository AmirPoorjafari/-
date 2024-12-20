import sympy as sp
n=100
x0=1.0
a=0
tolerance=1e-7
x = sp.symbols('x')



def F(x):
    return ((x**4)+(x**3)+(x**2)+(x))-30
F_P = sp.diff(F(x), x)



for i in range(1,n+1):
    x1=x0-(F(x0)/F_P.subs(x,x0))
    if abs(x1-x0) < tolerance:
      if( F(x1) < tolerance ):
          print("STEP",i,":root=",x1,"F(x1)=",F(x1))    
          a=1
          break
    x0=x1



if(a==0):
    print('It has no roots') 