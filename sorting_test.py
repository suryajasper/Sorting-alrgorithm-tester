from graphics import *
import random
import time

maxX = 800
maxY = 800
w = GraphWin("Sorting Algorithm tester", maxX, maxY, autoflush = False)
#w.setBackground("blue")
size = 5
global num
num = int(maxX/size)
arr = []
global comparisons
global invert
invert = False

##########################################################################

def button(x,y, text, color):
    b = Rectangle(Point(x, y), Point(x+len(text)*10, y+30))
    b.setFill(color)
    text = Text(Point(x+(len(text)*5), y+15), text)
    text.setTextColor("white")
    text.setSize(13)
    b.draw(w)
    text.draw(w)
    return b
def inside(point, rectangle):
    ll = rectangle.getP1() 
    ur = rectangle.getP2()  
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

##########################################################################

t1 = Text(Point(maxX/2, maxY/4), "Please enter the number of values you would like to sort.")
if maxX/50 <= 36:
    t1.setSize(int(maxX/30))
else:
    t1.setSize(36)
global floatsize, rand, ordered, numin, b
floatsize = maxX/num

def menu():
    global floatsize, rand, ordered, num, numin, b
    print ("First", num)
    for item in w.items[:]:
        item.undraw()
    w.update()
    numin = Entry(Point(maxX/2, maxY/2), int(maxX/40))
    b = button(3*maxX/4,maxY/2, "Enter", "red")
    t1.draw(w)
    numin.draw(w)
    while True:
        if inside(w.getMouse(),b):
            if (num<=0 or num>(maxX/2)):
                print("invalid")
                continue
            else:
                num = int(numin.getText())
                break
    floatsize = maxX/num
    rand = button(maxX/4, 3*maxY/4, "Random", "red")
    ordered = button(3*maxX/4, 3*maxY/4, "Ordered", "red")
    while True:
        k = w.getMouse()
        if (inside(k, rand)):
            for i in range(num+1):
                arr.append(random.randint(1,num))
            break
        elif (inside(k, ordered)):
            print(num)
            for i in range(num):
                arr.append(i-1)
            random.shuffle(arr)
            break
menu()

##########################################################################

global backbutton

def drawRect(x,l):
    global floatsize
    r = Rectangle(Point(x*floatsize, maxY), Point((x+1)*floatsize, (l+1)*floatsize))
    r.setFill("red")
    r.setWidth(1)
    r.draw(w)
    return r
def clear():
    for item in w.items[:]:
        item.undraw()
    w.update()

global rectarr, firstvisuals, speedchange, speednum, speed, speedup, speeddown

speednum = 6
#speed = Text(Point(maxX*9/10, maxY/10-40), "Speed: " + str(speednum))
#speedup = button(maxX*9/10-20, maxY/10-10, " + ", "green")
#speeddown = button(maxX*9/10+20, maxY/10-10, " - ", "red")


firstvisuals = True
speedchange = False

rectarr = []
for i in range(num):
    rectarr.append(0)

def visuals(com, boolean, sorttype):
    global speednum, firstvisuals, speedchange, speed, speedup, speeddown, num
    if firstvisuals or speedchange:
        speed = Text(Point(maxX*9/10, maxY/10-40), "Speed: " + str(speednum))
        speed.setSize(18)
        speed.setTextColor("blue")
        speed.draw(w)
        if speedchange:
            speedchange = False
    speedup = button(maxX*9/10-20, maxY/10-10, " + ", "green")
    speeddown = button(maxX*9/10+20, maxY/10-10, " - ", "red")
    k = w.checkMouse()
    if k != None:
        print("Not none")
        if (inside(k, speedup) and speednum <= 20):
            speednum += 1
            speedchange = True
            print("+")
        elif (inside(k, speeddown) and speednum >= 2):
            speednum -= 1
            speedchange = True
    
    comp = Text(Point(maxX/2, 20), ("(" + sorttype + " sort) comparisons " + str(com)))
    comp.setSize(20)
    comp.draw(w)
    for k in range(num):
        rectarr[k] = (drawRect(k,arr[k]))
    w.autoflush = True
    for k in range(5):
        r = Rectangle(Point(0,0), Point(5,5))
        r.setWidth(0)
        r.setFill("white")
        r.draw(w)
        r.undraw()
    w.autoflush=False
    if boolean == True:
        if firstvisuals:
            for item in w.items[:]:
                item.undraw()
            speed.draw(w)
            firstvisuals = False
        else:
            for rec in rectarr:
                rec.undraw()
            if speedchange:
                print("there is one")
                speed.undraw()
            comp.undraw()
            w.update()
    else:
        w.autoflush = True
        for r in rectarr:
            r.setWidth("0.02")
            r.setFill("green")
            w.update()
        w.autoflush = False
        backbutton = button(maxX*4/5, maxY/5, "Go Back", "red")
        while True:
            if inside(w.getMouse(), backbutton):
                break

##########################################################################

def bubblesort():
    global comparisons, speednum
    speednum = 1
    comparisons = 0
    s = 0
    n = len(arr)
    for i in range(n):
        s+=1
        if s > speednum:
            visuals(comparisons, True, "bubble")
            s = 0
        for j in range(0, n-i-1):
            comparisons+=1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def partition(low,high):
    global comparisons
    i = low-1
    pivot = arr[high]
    for j in range(low , high):
        comparisons += 1
        if arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 ) 
def quickSort(low,high):
    random.shuffle(arr)
    global comparisons, speednum
    if low < high:
        pi = partition(low,high)
        visuals(comparisons, True, "quick")
        quickSort(low, pi-1) 
        quickSort(pi+1, high)
def selectionsort():
    global comparisons, speednum
    s = 0
    speednum = 5
    for i in range(len(arr)):
        s += 1
        if s > speednum:
            s = 0
            visuals(comparisons, True, "selection")
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons+=1
            if arr[min_idx] > arr[j]: 
                min_idx = j    
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def shellSort():
    s = 0
    global comparisons, speednum
    speednum = 10
    n = len(arr) 
    gap = int(n/2)
    while gap > 0:
        for i in range(gap,n):
            comparisons += 1
            first = True
            s+=1
            if s > speednum:
                visuals(comparisons, True, "shell")
                s = 0
            temp = arr[i] 
            j = i 
            while j >= gap and arr[j-gap] > temp:
                if first == False:
                    comparisons+=1
                first = False
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp 
        gap = int(gap/ 2)
def insertionSort():
    global comparisons, speednum
    s = 0
    speednum = 5
    for i in range(1, len(arr)):
        s+=1
        if s >= speednum:
            visuals(comparisons, True, "insertion")
            s = 0
        first = True
        comparisons+= 1
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] :
            if first == False:
                comparisons+=1
            first = False
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 
def bogoSort():
    global comparisons, speednum
    comparisons = 0
    while True:
        comparisons+=1
        stop = button(maxX*7/10, maxY/10, "STOP", "red")
        k = w.checkMouse()
        if k != None:
            if (inside(k, stop)):
                break
        random.shuffle(arr)
        visuals(comparisons, True, "bogo")
##########################################################################

b.undraw()
t1.undraw()
numin.undraw()
rand.undraw()
ordered.undraw()
size = int(floatsize)
print("num ", num, " size ", size)

while True:
    back2menu = button(maxX/2, maxY/8, "Go Back to the Menu", "green")
    shellb = button(maxX/5, maxY/4, "Shell sort", "green")
    bubbleb = button(maxX*2/5, maxY/4, "Bubble sort", "blue")
    selectionb = button(maxX*3/5, maxY/4, "Selection sort", "red")
    quickb = button(maxX*4/5, maxY/4, "Quick sort", "black")
    bogob = button(maxX/5, maxY/2, "Bogo sort", "purple")
    insertb = button(maxX*2/5, maxY/2, "Insertion sort", "orange")
    comparisons = 0
    k = w.getMouse()
    if inside(k, back2menu):
        for i in range(len(arr)):
            arr.pop(0)
        for i in range(len(rectarr)):
            rectarr.pop(0)
        menu()
        for i in range(num):
            rectarr.append(0)
    elif inside(k, shellb):
        shellSort()
        visuals(comparisons, False, "shell")
    elif inside(k, bubbleb):
        bubblesort()
        visuals(comparisons, False, "bubble")
    elif inside(k, selectionb):
        selectionsort()
        visuals(comparisons, False, "selection")
    elif inside(k, bogob):
        bogoSort()
    elif inside(k, insertb):
        insertionSort()
        visuals(comparisons, False, "insertion")
    elif inside(k, quickb):
        quickSort(0,num-1)
        visuals(comparisons, False, "quick")
        speednum = 6
    firstvisuals = True
    random.shuffle(arr)
    clear()
