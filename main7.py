def draw_rectangle(width,height):
    for i in range(height):
        if i==0:
            print(" "+"-"*height)
        elif i==height-1:
            print(" "+"-"*height)
        else:
            print("|"+" "*height+"|")

def draw_rectangle2(width,height):
    return ("|"+"-"*width+"|"+("\n"+"|"+" "*height+"|")*(int(height)-2)+"\n"+"|"+"-"*width+"|")

print(draw_rectangle2(5,5))

def drawtriangle(height):
    for i in range(height):
        d=height-i
        if i == height-1:
            print(" " * d + "/" + "__" * i + "\\")
        else:
            print(" "*d+"/"+"  "*i+"\\")
drawtriangle(5)

def tapis(n):
    total=n
    print("+"+"-"*(n+1)+"+")
    for i in range(n+1):
        d=n+1-i
        na=total-i
        nb=total-na
        print("|"+"#"*na+" "+"#"*nb+"|")
    print("+"+"-"*(n+1)+"+")
tapis(5)


def cesarcode(mot,decalage):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    d=0
    nmot=[]
    for i in range(len(mot)):
        for j in range(len(alphabet)):
            if alphabet[j]==mot[i]:
                decalmoi=j+decalage
                if decalmoi>26:
                    decalmoi=decalmoi-26
                nmot.append(alphabet[decalmoi])
    nmot="".join(nmot)
    return nmot

print(cesarcode("papa",25))

def gardientoilette(marches,hauteurmarches):
    dist=((10*marches*hauteurmarches)*7)/100
    return f"Pour {marches} marches de {hauteurmarches} cm, le gardien parcourt {dist} m par semaine."
print(gardientoilette(51,50.4))


def mathprof(listenotes):
    arrondis=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    listefini=[]
    for i in range(len(listenotes)):
        for j in range(len(arrondis)):
            jam=listenotes[i]-arrondis[j]
            diff=5-jam
            if jam<5:
                diff=5-jam
                if diff<=3:
                    listefini.append(listenotes[i]+diff)
                    break
                else:
                    listefini.append(listenotes[i])
                    break
    return listefini


print(mathprof([16,17,26,29]))

def mysort(lst):
    copyme=lst.copy() #copie de la liste pour eviter de potentiels conflits
    for j in lst: #pour les elements de la liste
        for i in range(len(lst)-1): #pour i allant de 0 a la taille de la liste moins un
            copyme = lst.copy() #mise a jour de la copie de la liste pour qu'elle reste identique a celle-ci et que les echanges puisse se faire correctement
            if lst[i]<lst[i+1]: # comparaison entre l'element i et l'element i+1 de la liste
                continue
            else:
                lst[i]=copyme[i+1]
                lst[i+1]=copyme[i] # echange si l'element n'est pas bien trié
    return lst


print(mysort([10,9,8,72,55,88,52,36]))



