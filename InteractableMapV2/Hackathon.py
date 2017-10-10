#Nick Almeder
#New Student Stuff


import graphics
from tkinter import *

#root = Tk()

# def key(event):
#     root.event_generate('<Motion>', warp=True, x=50, y=50)

Rectangles = []

building = []
X1s = []
X2s = []
Y1s = []
Y2s = []
dT = graphics.Text(graphics.Point(1000,40), "no")

x=0
y=0
instant_x = 0
instant_y = 0



def motion(event):                                                 #It's right here
   # print('motion {}, {}'.format(event.x, event.y))
    global x
    global y
    x = event.x
    y = event.y
    global dT

    p = 0
    z = len(X1s) - 1
    while z > -1:
        if(X1s[z] > x and x > X2s[z] and Y1s[z] > y and y > Y2s[z]):
            #
            dT.undraw()
            dT = graphics.Text(graphics.Point(1050, 40), building[z])
            dT.draw(BSUmapimage.Map)
        z -= 1








class BSUmapimage():
    #960x540
    #anchor point in direct center

    Map = graphics.GraphWin("BSU Campus", 1160,540)
    BSUimage = graphics.Image(graphics.Point(480,270), "BSU.gif")
    BSUimage.draw(Map)


    global dT



    Map.bind('<Motion>', motion)




#  ----------------Fix this later maybe I don't care-----------------------



def CH():
    x1, x2, y1, y2 = 608, 550, 391, 338

    CH = graphics.Rectangle(          #Crimson Hall
        graphics.Point(x1,y1),
        graphics.Point(x2,y2)
    )

    CH.setOutline("yellow")
    CH.draw(BSUmapimage.Map)


    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Crimson Hall")

def DH():
    x1, x2, y1, y2 =615,572,318,276
    DH = graphics.Rectangle(        #Dinardo Hall
        graphics.Point(x1,y1),
        graphics.Point(x2,y2)
    )

    DH.setOutline("Yellow")
    DH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Dinardo Hall")

def WH():
    x1, x2, y1, y2 =672,612 ,496, 422
    WH = graphics.Rectangle(        #Weygard Hall
        graphics.Point(x1,y1),
        graphics.Point(x2,y2)
    )

    WH.setOutline("Yellow")
    WH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Weygard Hall")

def ECC():
    x1, x2, y1, y2 =671,628 ,353 ,305
    ECC = graphics.Rectangle(       #East Campus Commons
        graphics.Point(x1,y1),
        graphics.Point(x2,y2)
    )

    ECC.setOutline("Yellow")
    ECC.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("East Campus Commons")

def SD():
    x1, x2, y1, y2 =844,791 ,395 ,322
    SD = graphics.Rectangle(          #SheaDurg
        graphics.Point(844,395),
        graphics.Point(791,322)
    )

    SD.setOutline("Yellow")
    SD.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Shea/Durgin Hall")

def TC():
    x1, x2, y1, y2 =866,813 ,157 ,84
    TC = graphics.Rectangle(        #Tinsley Center
        graphics.Point(866,157),
        graphics.Point(813,84)
    )

    TC.setOutline("Yellow")
    TC.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Tinsley Center")

def HART():
    x1, x2, y1, y2 =552,509 ,116 ,78
    Hart = graphics.Rectangle(      #Hart Hall
        graphics.Point(552,116),
        graphics.Point(509,78)
    )

    Hart.setOutline("Yellow")
    Hart.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Hart Hall")

def BURNELL():
    x1, x2, y1, y2 =637,569 ,80 ,9
    Burnell = graphics.Rectangle(       #Burnell Hall
        graphics.Point(637,80),
        graphics.Point(569,9)
    )

    Burnell.setOutline("Yellow")
    Burnell.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Burnell Hall")

def KG():
    x1, x2, y1, y2 =296,243 ,276 ,223
    KG = graphics.Rectangle(           #Kelly Gymnasium
        graphics.Point(296,276),
        graphics.Point(243,223)
    )

    KG.setOutline("Yellow")
    KG.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Kelly Gymnasium")

def ML():
    x1, x2, y1, y2 = 242,189,329,276
    ML = graphics.Rectangle(        #Maxwell Library
        graphics.Point(242,329),
        graphics.Point(189,276)
    )

    ML.setOutline("Yellow")
    ML.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Maxwell Library")

def DMF():
    x1, x2, y1, y2 = 278,202,202,167
    DMF = graphics.Rectangle(       #Dana Mohler Faria
        graphics.Point(278,202),
        graphics.Point(202,167)
    )

    DMF.setOutline("Yellow")
    DMF.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Dana Mohler-Faria")

def RCC():
    x1, x2, y1, y2 = 167,86,280,214
    RCC = graphics.Rectangle(        #Rondilieu Campus Center
        graphics.Point(167,280),
        graphics.Point(86,214)
    )

    RCC.setOutline("Yellow")
    RCC.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Rondilieu Campus Center")

def SH():
    x1, x2, y1, y2 = 107,77,359,300
    SH = graphics.Rectangle(        #Scott Hall
        graphics.Point(107,359),
        graphics.Point(77,300)
    )

    SH.setOutline("Yellow")
    SH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Scott Hall")

def WWH_HaH():
    x1, x2, y1, y2 = 31,0,412,318
    WWH_HaH = graphics.Rectangle(   #Woodward Hall and Harrington Hall
        graphics.Point(31,412),
        graphics.Point(0,318)
    )

    WWH_HaH.setOutline("Yellow")
    WWH_HaH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Woodward Hall and Harrington Hall")

def THH():
    x1, x2, y1, y2 = 57,0,261,211
    THH = graphics.Rectangle(       #Hunt Hall
        graphics.Point(57,261),
        graphics.Point(0,211)
    )

    THH.setOutline("Yellow")
    THH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Hunt Hall")

def AC():
    x1, x2, y1, y2 = 40,5,185,154
    AC = graphics.Rectangle(        #Art Center
        graphics.Point(40,185),
        graphics.Point(5,154)
    )

    AC.setOutline("Yellow")
    AC.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Art Center")

def MH():
    x1, x2, y1, y2 = 640,599,279,248
    MH = graphics.Rectangle(        #MIles Hall
        graphics.Point(640,279),
        graphics.Point(599,248)
    )

    MH.setOutline("Yellow")
    MH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Miles Hall")

def MC():
    x1, x2, y1, y2 = 547,506,154,123
    MC = graphics.Rectangle(        #Moakley Center
        graphics.Point(547,154),
        graphics.Point(506,123)
    )

    MC.setOutline("Yellow")
    MC.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Moakley Center")

def PH():
    x1, x2, y1, y2 = 134,83,174,122     #Popehall
    PH = graphics.Rectangle(
        graphics.Point(134,174),
        graphics.Point(83, 122)
    )

    PH.setOutline("Yellow")
    PH.draw(BSUmapimage.Map)

    X1s.append(x1)
    X2s.append(x2)
    Y1s.append(y1)
    Y2s.append(y2)
    building.append("Pope Hall")

#--------------------------------------------------------------------------

class Filter():
    Legend = graphics.Rectangle(
        graphics.Point(344,529),
        graphics.Point(14,421)
    )
    Legend.setFill("White")
    Legend.setOutline("Black")
    Legend.draw(BSUmapimage.Map)




def main():
    BSUmapimage()


    CH() #1
    DH()    #2
    HART()  #3
    BURNELL()   #4
    KG()    #5
    ML()    #6
    DMF()   #7
    RCC()   #8
    SH()    #9
    WWH_HaH()   #10
    THH()   #11
    AC()    #12
    MH()    #13
    MC()    #14
    PH()    #15
    TC()    #16
    SD()    #17
    WH()    #18
    ECC()   #19


    BSUmapimage.Map.getMouse()
    BSUmapimage.Map.close()



main()