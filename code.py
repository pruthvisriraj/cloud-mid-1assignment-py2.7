mm = 10
yy = 2020
  
month ={1:u'January', 2:u'February', 3:u'March',  
        4:u'April', 5:u'May', 6:u'June', 7:u'July', 
        8:u'August', 9:u'September', 10:u'October', 
        11:u'November', 12:u'December'} 

day =(yy-1)% 400
day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
day = day % 7
  
nly =[31, 28, 31, 30, 31, 30,  
      31, 31, 30, 31, 30, 31] 
ly =[31, 29, 31, 30, 31, 30,  
     31, 31, 30, 31, 30, 31] 
s = 0
  
if yy % 4 == 0: 
    for i in xrange(mm-1): 
        s+= ly[i] 
else: 
    for i in xrange(mm-1): 
        s+= nly[i] 
  
day += s % 7
day = day % 7
   
 
space =u'' 
space = space.rjust(2, u' ') 
  

print month[mm], yy 
print u'Su', u'Mo', u'Tu', u'We', u'Th', u'Fr', u'Sa' 
  
if mm == 9 or mm == 4 or mm == 6 or mm == 11:  
    for i in xrange(31 + day): 
          
        if i<= day: 
            print space, 
        else: 
            print u"{:02d}".format(i-day), 
            if (i + 1)% 7 == 0: 
                print 
elif mm == 2: 
    if yy % 4 == 0: 
        p = 30
    else: 
        p = 29
          
    for i in xrange(p + day): 
        if i<= day: 
            print space, 
        else: 
            print u"{:02d}".format(i-day), 
            if (i + 1)% 7 == 0: 
                print  
else: 
    for i in xrange(32 + day): 
          
        if i<= day: 
            print space, 
        else: 
            print u"{:02d}".format(i-day), 
            if (i + 1)% 7 == 0: 
                print 
