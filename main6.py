def printing():
    fruits=["pomme","cerise","orange"]
    print(["pomme","cerise","orange"])
    return(fruits)

def printing2():
    fruits=["pomme","cerise","orange"]
    return(fruits[1])

def fruitmelon():
    fruits=["pomme","cerise","orange"]
    fruits.append("Melon")
    fruits.insert(0,"papa")
    return(fruits)

def fruitagemax():
    fruits = ["pomme", "cerise", "orange","melon"]
    fruits.insert(2, "mangue")
    return (fruits)


def fruitagemax2():
    fruits = [5,6,7,8,9]
    fruits[3] = int(fruits[2] + fruits[4])
    return(fruits[1],fruits,fruits[-1])


def fruitagemax3():
    fruits = [5,6,7,8,9]
    tempfruit=fruits.copy()
    temp0=tempfruit[0]
    templ=tempfruit[-1]
    fruits[0]=templ
    fruits[-1]=temp0
    return(fruits)

def fruitagemax4():
    count=0
    L = [8, 24,48,2,16]
    for i in L:
        if i%3==0:
            count+=1
        else:
            continue
    return(count)

def fruitagemax5():
    summary=0
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    for i in L:
        if i%2==0:
            summary+=i
        else:
            continue
    return(summary)

def fruitagemax6():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    min=L[0]
    max=L[0]
    for i in range(len(L)):
        if L[i] >= max:
            max = L[i]
    for i in range(len(L)):
        if L[i] <= min:
            min = L[i]
    return(min,max)

def fruitagemax7():
    summary=[]
    summarygot=0
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    for i in L:
        if 25<=i<=90:
            summary.append(i)
        else:
            continue
    summarygot=summary[0]
    for i in range(1,len(summary)):
        summarygot=summarygot*summary[i]


    return(summarygot)


def fruitagemax8():
    L = [7, 11, 42, 39, 2]
    for i in range(len(L)):
        L[i]+=1
    return(L)

def trieca(L):
    tri=[]
    while L:
        min = L[0]
        for i in L:

            print(i,min)
            if i<=min:
                min=i
        tri.append(min)
        L.remove(min)
    return(tri,min,L)

def nodoublon(L):
    Lcompare=L.copy()
    for i in L:
        gym=i
        if i in Lcompare:
            for j in Lcompare:
                if j==gym:
                    Lcompare.remove(j)
            Lcompare.append(gym)
    return Lcompare

def phraso(digit,text):
    count1=0
    count2=0
    lengo=0
    output=[]
    datalst=text.split(" ")
    for i in datalst:
        count1+=1

    for j in range(0,count1):
        for k in datalst [j]:
            print(k)
            count2+=1
        if count2>=digit:
            output.append(datalst[j])
        count2=0
    return output

def thelastone(L):
    rounded=[]
    tri = []
    for i in L:
        i=str(i)
        datago=i.split(".")
        rounded.append(int(datago[0]))
    while rounded:
        min=rounded[0]
        for i in rounded:
            if i <= min:
                min=i
        tri.append(min)
        rounded.remove(min)
    return(tri,rounded)










print(thelastone([22.4, 4.0, 16.22,
9.10, 11.00, 12.22, 14.20, 5.20, 17.50]))

#print(phraso(2,"je n'ai pas d'enfants"))


