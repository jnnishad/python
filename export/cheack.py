import sys, time
import array as arr


option=['EMI','NB','HDFC']
for present in range(len(option)) :
    print (present,")",option[present])


#print(len(option))

num=int(input('Enter your choice : '))
if num == 1:
    print ('You chose', num)

#print ('process No. is :  1', end="")
#for i in range(2,user+1):
 #   #if i%10==0:
 #     print ('\r','process No. is : ', i,end="")
  #    time.sleep(0.1)
    #else:
        #print ('\r','process No. is : ',i,end="")
        #time.sleep(0.1)