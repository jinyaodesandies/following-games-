import random
import time
dif=int(input("hi, this is KOSF(knock off street fighters).do you want to register for light weight(easy,1),midweight(medium,2),or heavy weight(hard,3)? (to choose, type the letter than type enter.)"))
if dif==1:
    ply_hea=30
    com_hea=20
elif dif==2:
    com_hea=20
    ply_hea=20
elif dif==3:
    com_hea=30
    ply_hea=15
dif=int(input("choose your charecter by 1,2,or3(\n1 is joe,he has 5 shoulder attack,9 belly attak,and 15head attack.\n2 is leela, she has 3 shoulder attack,7 belly attack, and 19 head attack.\n3 is kanji,his shoulder attack is 10,belly attack is 11, and head attack is 13."))
if dif==1:
    l=5
    m=9
    h=15
elif dif==2:
    l=3
    m=7
    h=14
elif dif==3:
    l=7
    m=11
    h=13
else:
    print("this is not a valid entry")
while ply_hea>0 and com_hea>0:
    choice=input("\nwelcome to KOSF,you are fighing a computer, and you should press 1,2,or 3.\n(one is attacking the shoulder,you can not give that much damage,but it's easy to retrieve to dodge damage.\ntwo is attack the belly,and you can still do some blocking.\nThree is hard punching on the head, but you can't defend at all\nfour if overhead throw,but it can only operate at a very lucky condition.)")         
    if choice=="1":
        ply_sco=random.randint(1,l)
        com_sco=random.randint(1,5)
    if choice=="2":
        ply_sco=random.randint(1,m)
        com_sco=random.randint(1,9)
    if choice=="3":
        ply_sco=random.randint(1,h)
        com_sco=random.randint(1,15)
    if choice=="4" and com_hea<11:
        death=random.randint(1,3)
        if death==1:
            ply_sco=1000
        else:
           com_sco=random.randint(1,15)
           print("you fall on the floor. you get beat up.")
        
    else:
        print("this is not a valid entry.or you have won.")
    print("player got a "+str(ply_sco)+" and com got a "+str(com_sco)+" .")        
    if ply_sco>com_sco:
        end_att=ply_sco-com_sco
        com_hea-=end_att
        print("player won by "+str(end_att)+" .")
    elif com_sco>ply_sco:
        end_att=com_sco-ply_sco
        ply_hea-=end_att
    elif com_sco==ply_sco:
        print("you tied! no one loses health")
    print("player currently has "+str(ply_hea)+" of health left, computer currently has "+str(com_hea)+" health left.")
        
if ply_hea>0:
    print("horray! you beat the computer!")
else:
    ("sorry,you lost.")
