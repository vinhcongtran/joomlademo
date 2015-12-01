def ptb2(a,b,c):
    print a,b,c
    import math
    delta = b*b - 4*a*c
    if (delta < 0):
        print " phuong trinh vo nghiem"
    elif (delta == 0):
        x1= (-b)/(2*a)
        print "phuong trinh bac 2 co 1 nghiem :", x1        
    else:
        x1 = (-b + math.sqrt(delta))/ (2*a)
        x2 = (-b - math.sqrt(delta))/ (2*a)
        print "phuong trinh bac 2 co 2 nghiem :", x1 , x2
ptb2(2, 9, 6);