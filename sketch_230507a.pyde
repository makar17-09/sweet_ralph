b = 0
c=0
a=0
x_eda=400
y_eda=410
timer=random(10*50,30*50)
def setup():
    size(1000, 550)
    global b
    b = loadImage("ra.jpg")

def draw():
    global b,c,x_eda,y_eda,timer
    
    #eda
    image(b, 0, 0)
    if c==0:
        rand=random(1,10)
        if rand>=6:
            c=loadImage("pancacke1.png")
        else:
            c=loadImage("kokteil1.png")
    image(c,x_eda,y_eda,160,120)
    
    #move eda
    if mousePressed and abs(x_eda-mouseX)<100 and abs(y_eda-mouseY)<100:
        x_eda=mouseX
        y_eda=mouseY
    
    #eat
    if (x_eda<=250 and y_eda>=300) or (x_eda>=750 and y_eda>=300):
        c=0
        x_eda=400
        y_eda=410
    
    timer-=1
    if timer==0:
      a=loadImage("unnamed.png")
      image(a,0,0)
      noLoop()
