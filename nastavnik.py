lst = [5,2,7,4,0,9,8,6]
def sorttomax(originlist):
    n = 0
    while n in range(len(originlist)):
        for i in range(len(originlist)):
            if originlist[i] > originlist[i + 1]:
                originlist[i], originlist[i + 1] = originlist[i + 1], originlist[i]
                n += 1
                return (range(len(originlist[i])))
    print(sorttomax(lst))
    print(lst)
