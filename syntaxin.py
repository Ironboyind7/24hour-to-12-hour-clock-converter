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
def from12hrto24(strtime):
    lis = strtime.split(":")
    l1 = strtime.split(".")
    if l1[-1] =="PM":
        lis[0] = int(lis[0])+12
        lis = lis[::-3]
        return ":".join(lis)
    else:
        lis = lis[::-3]
        return lis
    
print(to12hr("12:0:0"))
print(from12hrto12("7:27:12.PM"))
