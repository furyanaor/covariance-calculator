# covariance of 2 list calculator
    
x1 = [2,3,4,10,22,55,7.5]
x2 = [0.2,0.3,6,3,21,33,10]

print "list x1: ", x1
print "list x2: ", x2

avg_x1 = sum(x1) / len(x1)
avg_x2 = sum(x2) / len(x2)

print "average of x2: ", avg_x1
print "average of x2: ", avg_x2

i = 0
covariance_x1_x2 = 0
while i < len(x1):
    covariance_x1_x2 += (avg_x1-x1[i])*(avg_x2-x2[i]) 
    i+=1;
covariance_x1_x2 = covariance_x1_x2 / len(x1)

print "covariance of x1&x2: ", covariance_x1_x2
