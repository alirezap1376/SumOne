from drs import drs
import random 
import numpy as np 

number = 5
length = 10
low = 0.1
up = 0.4

y=np.zeros( (length,1)  )
    
df = drs(number, 1,  [up for i in range(number)] , [low for i in range(number)])
    
for i in range(0 , len(df) ):
     df[i] = round( df[i]  ,2)
        
if sum(df) < 1 :
        df[-1] = df[-1] + round( 1-sum(df)   ,3)
elif sum(df) > 1 :
        df[-1] = df[-1] + round( 1-sum(df)   ,3)
    
choice = random.sample(  list(range(0, length)) ,  number     )

for i in range( len(choice ) ) :
        y[   choice[i]  ][0] = df[i]