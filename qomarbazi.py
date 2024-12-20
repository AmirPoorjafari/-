import random
initial_value=10
bet_amount=1
best_amount=bet_amount
order=0
order_1=0



for bet_amount in range(1,initial_value+1):
   initial_value=10
   order=0
   while(initial_value>0):
         order+=1
         chance=random.randrange(0,2)
         
         if(chance==0):
           
           if(initial_value-bet_amount >0):
              initial_value-=bet_amount
           else:
              initial_value=0 
         
         if(chance==1):
              initial_value+=bet_amount
         print("order=",order,initial_value)
   
   
   
   
   if(order>order_1):
         order_1=order
         best_amount=bet_amount



print("best_amount=",best_amount)