Testcase = int(input())


 

while Testcase!=0:

    seat_number = int(input())

    s=seat_number%12

    if s==0:

        print(seat_number-11,'WS')

    elif s==1:

        print(seat_number+11,'WS')

    elif s==2:

        print(seat_number+9,'MS')

    elif s==3:

        print(seat_number+7,'AS')

    elif s==4:

        print(seat_number+5,'AS')

    elif s==5:

        print(seat_number+3,'MS')

    elif s==6:

        print(seat_number+1,'WS')

    elif s==7:

        print(seat_number-1,'WS')

    elif s==8:

        print(seat_number-3,'MS')

    elif s==9:

        print(seat_number-5,'AS')

    elif s==10:

        print(seat_number-7,'AS')

    elif s==11:

        print(seat_number-9,'MS')

 

    Testcase=Testcase-1
