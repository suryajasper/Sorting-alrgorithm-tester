from graphics import *
import random
import time

maxX = 800
maxY = 800
w = GraphWin("Sorting Algorithm tester", maxX, maxY, autoflush = False)
size = 5
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
numin = Entry(Point(maxX/2, maxY/2), int(maxX/40))
t1.draw(w)
numin.draw(w)
b = button(3*maxX/4,maxY/2, "Enter", "red")
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
        for i in range(num):
            arr.append(i-1)
        random.shuffle(arr)
        break

##########################################################################

def drawRect(x,l):
    r = Rectangle(Point(x*floatsize, maxY), Point((x+1)*floatsize, (l+1)*floatsize))
    r.setFill("red")
    r.setWidth(1)
    r.draw(w)
def visuals(com, boolean):
    comp = Text(Point(maxX/2, 20), ("(Bubble sort) comparisons " + str(com)))
    comp.setSize(20)
    comp.draw(w)
    for k in range(num):
        drawRect(k,arr[k])
    w.autoflush = True
    for k in range(6):
        r = Rectangle(Point(0,0), Point(5,5))
        r.setWidth(0)
        r.setFill("white")
        r.draw(w)
    w.autoflush=False
    if boolean == True:
        for item in w.items[:]:
            item.undraw()
        w.update()
    else:
        w.autoflush = True
        for item in w.items[:]:
            item.setFill("green")
            w.update()
        w.autoflush = False
        w.getMouse()

##########################################################################

def bubblesort():
    global comparisons
    comparisons = 0
    n = len(arr)
    for i in range(n):
        visuals(comparisons, True)
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
    global comparisons
    if low < high: 
        pi = partition(low,high)
        visuals(comparisons, True)
        quickSort(low, pi-1) 
        quickSort(pi+1, high)

##########################################################################

b.undraw()
t1.undraw()
numin.undraw()
rand.undraw()
ordered.undraw()
size = int(floatsize)
print("num ", num, " size ", size)
bubblesort()
visuals(comparisons, False)
comparisons = 0
quickSort(0,num-1)
visuals(comparisons, False)
