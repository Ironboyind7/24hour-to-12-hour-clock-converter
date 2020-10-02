def to12hr(strtime):
    lis = strtime.split(":")
    lis[0] = int(lis[0])
    if lis[0] > 12:
        lis[0] -=12
        lis = f"{lis[0]}:{lis[1]}:{lis[2]}.PM"
        print(lis)
    else:
        lis = f"{lis[0]}:{lis[1]}:{lis[2]}.AM"
        print(lis)
        
to12hr("12:0:0")
