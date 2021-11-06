import sys
import time
import random
list1=[['- ',"- ","- "]for _ in range(3)]
row1,row2,row3,s="","","","      "
for i in range(3):
    row1=row1+" "+list1[0][i]#print string row1 
    row2=row2+" "+list1[1][i]
    row3=row3+" "+list1[2][i]
#print position mapping
print("0 "+row1+"\n"+"1 "+row2+"\n"+"2 "+row3+"\n"+"   0  1  2 ")
row1,row2,row3,t,even="","","",9,1    
for i in range(t):
    if even%2!=0:m,n=map(int,input("\n\nPlease Enter the Position in rows and columns \n\n(row) (column) : ").split())
    else:
        while list1[m][n]!="- ":m,n=random.randint(0,2),random.randint(0,2)
    if list1[m][n]=="- ":
        even+=1
        if even%2==0:list1[m][n]="X "
        else:list1[m][n]="O "
        #print updated table
        for z in range(3):
            row1=row1+" "+list1[0][z]
            row2=row2+" "+list1[1][z]
            row3=row3+" "+list1[2][z]
        print("\n"+s+row1+"\n"+s+row2+"\n"+s+row3+"\n")
        #Check winner horizontalluy
        for i in range(3):
            if (list1[i][0]=="X "or list1[i][0]=="O " ) and (list1[i][0]==list1[i][1] and list1[i][1]==list1[i][2]):    
                print("\n"+s+" "+list1[i][0]+"is Winner\n"+"\n"+s+" Game Over\n")
                sys.exit()
        #Check winner vertically
        for i in range(3):
            if (list1[0][i]=="X " or list1[0][i]=="O ")and (list1[0][i]==list1[1][i] and list1[1][i]==list1[2][i]):
                print("\n"+s+" "+list1[0][i]+"is Winner\n"+"\n"+s+" Game Over\n")
                sys.exit()
        #check transversal lines
        if list1[1][1]!="- ":
            if list1[0][0]==list1[1][1] and list1[1][1] == list1[2][2]:
                print("\n"+s+" "+list1[1][1]+"is Winner\n"+"\n"+s+" Game Over\n")
                sys.exit()
            elif list1[0][2]==list1[1][1] and list1[1][1] == list1[2][0]:
                print("\n"+s+" "+list1[1][1]+"is Winner\n"+"\n"+s+" Game Over\n")
                sys.exit()
        #Freeing Previously printed table for next move
        row1,row2,row3="","",""
        #loading time
        a=0
        if(list1[m][n]=="X "):print("Player O plan your next move ")
        else:print("Player X plan your next move ")
        while a<5:    
                a = a + 1 
                b = ("Loading" + "." * a)
                sys.stdout.write('\r'+b)
                time.sleep(1)   
    #Entered in a already printed position    
    else:
        print("\nPlease Enter a new position. \nDon't overwrite \n")
        


