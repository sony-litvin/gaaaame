x=960
y=640
x1=x/2
y1=y/2
y2=y1
y3=y1
y4=y1
y5=y1
y6=y1
x2=x1-490
x3=x1-450
x4=x1-480
x5=x1-455
x6=x1-475
x1=x1-460
a=900
b=320
c=300
d=100
speed=10
dim=80
dy=100
r=53.0
x0=a
y0=b
t=1000
t1=-2000
h=False
lose=False
i=0
c0=t
c1=t
c2=t
c3=t
c4=t
c5=t
c6=t
c7=t
d0=t
d1=t
d2=t
d3=t
d4=t
d5=t
d6=t
d7=t


def setup():
    size(x,y)
    global r1,bg,h1,cosmo1,s,l,i0,i1,i2,i3,i4,i5,i6,i7,rr1,bbb,wdsa
    bg = loadImage("sky_pixel.png")
    r1 = loadImage("pixel_r.png")
    h1 = loadImage("pixel_h.png")
    cosmo1 = loadImage("pixel_cosmo.png")
    s = loadImage("s.jpg")
    l = loadImage("lose.jpg")
    i0 = loadImage("0.jpg")
    i1 = loadImage("1.jpg")
    i2 = loadImage("2.jpg")
    i3 = loadImage("3.jpg")
    i4 = loadImage("4.jpg")
    i5 = loadImage("5.jpg")
    i6 = loadImage("6.jpg")
    i7 = loadImage("7.jpg")
    rr1 = loadImage("1r.jpg")
    bbb = loadImage("bbb.jpg")
    wdsa = loadImage("wdsa.jpg")

def keyReleased():
    global dy,h
    if key == ' ':
        dy=dy-19
    if key == ' ':
        h=True
      
   
        
def keyPressed():
    global a,b,x0,y0,c0,c1,c2,c3,c4,c5,c6,c7,d0,d1,d2,d3,d4,d5,d6,d7,speed
    
    #это управление
    if key == 'w':
        b=b-speed
    if key == 's':
        b=b+speed
    if key == 'a':
        a=a-speed
    if key == 'd':
        a=a+speed
    
    #а это старт иры
    if key == ' ' :
        x0=a-speed
        y0=b-speed 
        
    #показываем результаты
    if key == '1' :
        if i==0:
            c0=445
            d0=320
        if i==1:
            c1=445
            d1=320
        if i==2:
            c2=445
            d2=320
        if i==3:
            c3=445
            d3=320
        if i==4:
            c4=445
            d4=320
        if i==5:
            c5=445
            d5=320
        if i==6:
            c6=445
            d6=320
        if a==t:
            c7=445
            d7=320
    #назад в меню
    if key == 'b':
        h=False

def draw():
    imageMode(CENTER)
    image(bg,x/2,y/2,x,y)
    global x0,x1,x2,x3,x4,x5,x6,y0,y1,y2,y3,y4,y5,y6,a,b,dy,bg,h1,cosmo1,r1,s,h,l,lose,t,t1,i,c0,c1,c2,c3,c4,c5,c6,c7,d0,d1,d2,d3,d4,d5,d6,d7,wdsa
    
    #так нужно чтобы фигуры двигались
    x1=x1+0.8
    x2=x2+0.8
    x3=x3+0.8
    x4=x4+0.8
    x5=x5+0.8
    x6=x6+0.8
    
    #это можно назвать меню
    noStroke()
    image (s,445,250,250,80)
    image (rr1,445,340,250,80)
    image (bbb,445,430,250,80)
    image (wdsa,445,500,250,40)
    #наш геймплей
    if h==True:
        #двигаем фигуры на красивом фоне
        imageMode(CENTER)
        image(bg,x/2,y/2,x,y)
        if x1<-dim/2:
            x1=width-dim/2
        if x1>width+dim/2:
            x1=dim/2
        if y1+dy > height-dim/2+1:
            dy=-0.5*dy
            y1=y1+dy
        image(r1,x1,y1-250,60,60)
    
        if x2<-dim/2:
            x2=width-dim/2
        if x2>width+dim/2:
            x2=dim/2
        if y2+dy > height-dim/2+1:
            dy=-0.5*dy
            y2=y2+dy
        image(r1,x2,y2-160,53,53)
    
        if x3<-dim/2:
            x3=width-dim/2
        if x3>width+dim/2:
            x3=dim/2
        if y3+dy > height-dim/2+1:
            dy=-0.5*dy
            y3=y3+dy
        image(r1,x3,y3-70,70,70)
    
        if x4<-dim/2:
            x4=width-dim/2
        if x4>width+dim/2:
            x4=dim/2
        if y4+dy > height-dim/2+1:
            dy=-0.5*dy
            y4=y4+dy
        image(r1,x4,y4+40,60,60)
    
        if x5<-dim/2:
            x5=width-dim/2
        if x5>width+dim/2:
            x5=dim/2
        if y5+dy > height-dim/2+1:
            dy=-0.5*dy
            y5=y5+dy
        image(r1,x5,y5+150,45,45)
    
        if x6<-dim/2:
            x6=width-dim/2
        if x6>width+dim/2:
            x6=dim/2
        if y6+dy > height-dim/2+1:
            dy=-0.5*dy
            y6=y6+dy
        image(r1,x6,y6+240,53,53)
        
        #добавляем игрока
        if a>0 :
            rectMode(CENTER)
            image(cosmo1,a,b)
        
        #добавляем снаряды
        x0=x0-50
        image(h1,x0,y0,45,45) 
    
        #так выглядит наша тактика убийств
        if y0==y1-250 or x0==x1:
            y1=t
            x1=t
            i=i+1
        if y0==y2-160 or x0==x2:
            y2=t
            x2=t
            i=i+1
        if y0==y3-70 or x0==x3:
            y3=t
            x3=t
            i=i+1
        if y0==y4+40 or x0==x4:
            y4=t
            x4=t
            i=i+1
        if y0==y5+150 or x0==x5:
            y5=t
            x5=t
            i=i+1
        if y0==y6+240 or x0==x6:
            y6=t
            x6=t
            i=i+1
        
        #а это стены
        fill(200,30,200)
        rect(840,320,5,-t)
        rect(960,320,5,-t)
        rect(900,3,120,5)
        rect(900,637,120,5)
        #они ваc не пропустят дальше
        if a<870 or a>920:
            a=t
            b=t
        if b>600 or b<35:
            a=t
            b=t
        
        #на случай если какую-либо фигуру не убьют
        if x1>820:
            x1=t
            y1=t
        if x2>820:
            x2=t
            y2=t
        if x3>820:
            x3=t
            y3=t
        if x4>820:
            x4=t
            y4=t
        if x5>820:
            x5=t
            y5=t
        if x6>820:
            x6=t
            y6=t
          
        if i<5 :
            lose=True
        if i==6:
            lose=False
      
        #результаты
        image(i0,c0,d0,c,d)
        image(i1,c1,d1,c,d)
        image(i2,c2,d2,c,d)
        image(i3,c3,d3,c,d)
        image(i4,c4,d4,c,d)
        image(i5,c5,d5,c,d)
        image(i6,c6,d6,c,d)
        image(i7,c7,d7,c,d)
    
