import re
# from itertools import cycle

def filt(test):


    print(" ")

    print( " Notification :  " + test)
    test1 = test.replace(',',' ').replace('/', ' ')
    res = test1.split()
    print(res)
    # rec=cycle(res)
    # res = test.split(", ")
    # print(" Filtered string is : " + str(res))
    # n = len(res)
    #print(" ")

    prog = ["B.Tech", "B.Arch", "B.Des", "M.Tech", "MCA", "M.Arch", "M.Plan","MBA","BHMCT"]
    sem = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
    type=["(R)","(S)","(R"]

    l=[]
    program=""
    semm=""
    ctype=""
    kk=0

    for x in res:
        for g in type:
            if x==g:
                kk=1
    #Notification containing (R,S)       
   
    if kk==1:          
        for x in res:
            for y in prog:
                if x==y:
                    program = x
                    # dy={}
                    # dy["program"]=program
                    print(" Program  = " + x)  

            for z in sem:
                if x==z:
                    semm = z
                    print(" Sem      = " + z)
                    # dy={}
                    # dy["program"]=program
                    # dy["semester"]=semm
                    # l+=[dy]
                    # print(dy)
                
            for g in type:
                    if x==g:
                        ctype=g
                        print("Type = "+g)
                        dy={}
                        dy["program"]=program
                        dy["semester"]=semm
                        if(g=="(R"):
                            dy["ptype"]="(R,S)"
                        else:
                            dy["ptype"]=ctype
                        l+=[dy]
        # if kk==1:
        #     dy={}
        #     dy["program"]=program
        #     dy["semester"]=semm
        #     dy["ptype"]="(R)"
        #     l+=[dy]
    else:
        for x in res:
            for y in prog:
                if x==y:
                    program = x
                    dy={}
                    dy["program"]=program
                    print(" Program  = " + x)  

            for z in sem:
                if x==z:
                    semm = z
                    print(" Sem      = " + z)
                    dy={}
                    dy["program"]=program
                    dy["semester"]=semm
                    dy["ptype"]="(R)"
                    l+=[dy]
                    # print(dy)
                


    # print(l)
    print(" ")
    return l
    # print(" - - - - - - - - - - - - - - - -  ")  

# filt(a1)
# filt(b)
# filt(c)     