#Decomposition of an Address string
#Programmer: Jarrod Gertig
#Date: Sept. 4, 2020
#

print("Use decomp() with an address string like '1234 Rainbow Rd, Albuquerque, NM, 87123' as the input parameter.")

#Main function
def decomp(addy):              
    global numb,road,city,stat,post
    numb=get_numb(addy)
    road=get_road(addy)
    city=get_city(addy)
    stat=get_stat(addy)
    post=get_post(addy)
    thelist=[numb,road,city,stat,post]
    print(thelist)

def get_numb(addy):
    numbs=[]
    my_list=list(addy)
    for i in range(8):
        try:
            if int(my_list[i])<11:
                numbs.append(int(my_list[i]))
        except:
            continue
    strings=''
    for i in range(len(numbs)):
        strings+=str(numbs[i])
    return strings

def get_road(inp):
    global numb
    addy=inp.replace(numb+' ','')
    roads=''
    for i in range(len(addy)):
        if addy[i]!=',':
            roads+=addy[i]
        else:
            break
    return roads

def get_city(inp):
    global numb,road
    addy=inp.replace(numb+' '+road+', ','')
    my_list=list(addy)
    citys=''
    for i in range(len(addy)):
        if addy[i]!=',':
            citys+=addy[i]
        else:
            break
    return citys

def get_stat(inp):
    global numb,road,city
    addy=inp.replace(numb+' '+road+', '+city+', ','')
    my_list=list(addy)
    stats=''
    for i in range(len(addy)):
        if addy[i]!=',':
            stats+=addy[i]
        else:
            break
    return stats

def get_post(inp):
    global numb,road,city,stat
    return inp.replace(numb+' '+road+', '+city+', '+stat+', ','')

