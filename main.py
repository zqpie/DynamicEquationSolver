import turtle
t = turtle.Turtle()
###### BUGSSS
""""
Y-Intercepts of 10-20 cause the function drawGraph() to fail to scale 
perportions and intervals...
"""
######

#=================Settings
#graphSize = 150 ## must be divisable by graphSpaces
#graphSpaces = 10 
t.speed(0)
graphSize = 200

#=================Gather Data
print("please enter two points on a 2 demention graph: (up to 40)")  
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
#===========================================================Process Data
changeY = y2 - y1
changeX = x2 - x1
m = changeY / changeX
b = -1 * (m*x1) + y1
if (m % 2) == 0:
  m = int(m)
else:
  foo = 0
if (b % 2) == 0:
  b = int(b)
else:
  foo = 0
equation = ("Y=" + str(m)+"X +"+str(b))
print equation
#=================Determine static values, currently just --graphSpaces--
if True: ## dynamic graphsizing
  if b >= 0 and b <= 10: ## zero through ten
    graphSpaces = 10
  elif b > 10 and b <= 20: ## ten through twenty
    graphSpaces = 20
  elif b >20 and b <=30: ## twenty through thirdy
    graphSpaces = 30
  elif b >30 and b <= 40: ## thirdy through fourty
    graphSpaces = 40
  else:
    graphSpaces = 50
#graphSpaces = int((round(b/10)*10) + 10)
#========================================================== Draw Graph

interval = graphSize / graphSpaces
def drawGraph(x,y):
  """
   push the coordinates of the grids N,P corner.
  the grid will be build off of the graphSize variable
  """
  t.penup()
  t.goto(x,y)
  t.pendown()
  for i in range(graphSpaces/2):
    t.forward(graphSize)
    t.right(90)
    t.forward(interval)
    t.right(90)
    t.forward(graphSize)
    t.left(90)
    t.forward(interval)
    t.left(90)
  t.left(90)
  for i in range(graphSpaces/2):
    t.forward(graphSize)
    t.right(90)
    t.forward(interval)
    t.right(90)
    t.forward(graphSize)
    t.left(90)
    t.forward(interval)
    t.left(90)

  t.forward(graphSize)
  t.penup()
  t.goto(x,y-graphSize)
  t.pendown()
  t.goto(x + graphSize,y - graphSize)
  t.penup()

  t.goto(0,0)
  t.right(90)
def createOutlines(mode):
  if mode == "center_cross":
    t.penup()
    t.color("black")
    t.pensize(3)
    t.goto(-graphSize,0)
    t.pendown()
    t.goto(graphSize,0)
    t.penup()
    t.goto(0,graphSize)
    t.pendown()
    t.goto(0,-graphSize)
    t.color("black")
  elif mode == "title":
    t.penup()
    t.goto(0,graphSize + (graphSize / 4))
    t.write("Graph of Y=" + str(m) + "X +" + str(b))
tableSpaces = 30
def drawTable():                       ## table
  t.penup()
  t.goto(graphSize + (graphSize /2) , graphSize ) ## top left of graph
  t.color("blue")
  t.pendown()

  t.goto(graphSize + (graphSize) , graphSize ) ## top rifght of graph
  t.goto(graphSize + (graphSize * .75) , graphSize ) ## center of graph
  t.right(90)
  for i in range (20):
    t.forward(graphSize /graphSpaces )
    t.goto(t.xcor()+20, t.ycor())
    t.goto(t.xcor()-40,t.ycor())
    t.goto(t.xcor()+20,t.ycor())
  t.penup()
  midLeft = (.5 * ((3 * graphSize) - (graphSize / 2) + (graphSize * .75))) + 5
  midRight = (.5 * (graphSize + (graphSize * .75) + graphSize) + (graphSize /2)) - 10
  t.goto(midLeft, graphSize + 10)
  t.write("X")
  t.goto(midLeft, graphSize)
  for i in range (20):
    t.forward(graphSize /graphSpaces)##
    t.write(i)
  t.penup()
  t.goto(midRight, graphSize + graphSpaces)##
  t.write("Y")
  t.goto(midRight, graphSize)
  for i in range (20):
    t.forward(graphSize /graphSpaces) ##
    t.write((m*i) + b)
  t.goto(1000,1000)

  
    

#=================Draw Data to Graph
def drawLine():
  t.penup()
  t.pensize(1)
  t.goto(0,b * interval)
  t.pendown()


  while t.ycor() >= (-1 * graphSize) - interval and t.ycor() <= graphSize - interval and t.xcor() >= (-1 * graphSize) - interval  and t.xcor() <= graphSize - interval :
    t.goto(t.xcor()+ (changeX * interval) , t.ycor() + (changeY * interval))

  t.goto(0,b* interval)
  while t.ycor() >= (-1 * graphSize) and t.ycor() <= graphSize and t.xcor() >= (-1 * graphSize) and t.xcor() <= graphSize:
    t.goto(t.xcor()- (changeX * interval) , t.ycor() - (changeY * interval))




#=================Main code
drawGraph(0,graphSize)          ##TR
drawGraph(-graphSize,graphSize) ##TL
drawGraph(-graphSize,0)          ##BR
drawGraph(0,0)                   ##BL 
createOutlines("center_cross")
createOutlines("title")
drawLine()
drawTable()
