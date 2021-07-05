"""
File: my_drawing.py
Name: Jael lin
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(width=800, height=400, title="psychedelic")


def main():
    """
    "Neither agreeable nor disagreeable," I answered. "It just is."
                                                --- ALDOUS HUXLEY
    """
    bg_1()
    bg_2()
    bg_4()
    bg_3()
    bg_5()
    bg_6()
    bg_7()
    bg_8()
    bg_9()
    bg_10()
    bg_11()
    bg_12()
    bg_13()
    bg_14()
    bg_15()
    bg_16()
    dot()


def bg_1():
    bg1 = GRect(200, 200)
    bg1.filled = True
    bg1.color = "blue"
    bg1.fill_color = "blue"
    window.add(bg1)
    c1 = GOval(200, 200, x=-80, y=0)
    c1.color = "white"
    window.add(c1)
    c2 = GOval(200, 200, x=-60, y=0)
    c2.color = "white"
    window.add(c2)
    c3 = GOval(200, 200, x=-40, y=0)
    c3.color = "white"
    window.add(c3)
    c4 = GOval(200, 200, x=-20, y=0)
    c4.color = "white"
    window.add(c4)
    c5 = GOval(200, 200, x=0, y=0)
    c5.color = "white"
    window.add(c5)


def bg_2():
    bg2 = GRect(100, 100)
    bg2.filled = True
    bg2.color = "deeppink"
    bg2.fill_color = "deeppink"
    window.add(bg2, x=200, y=0)


def bg_3():
    bg3 = GRect(100, 100)
    bg3.filled = True
    bg3.color = "white"
    bg3.fill_color = "white"
    window.add(bg3, x=200, y=100)
    c10 = GOval(100, 100)
    c10.color = "lavender"
    c10.filled = True
    c10.fill_color = "lavender"
    window.add(c10, x=200, y=100)
    arc9 = GArc(200, 200, 270, 90)
    arc9.fill_color = "Lime"
    arc9.color = "Lime"
    arc9.filled = True
    window.add(arc9, x=150, y=50)
    arc10 = GArc(200, 200, 180, 90)
    arc10.fill_color = "Lime"
    arc10.color = "Lime"
    arc10.filled = True
    window.add(arc10, x=200, y=100)
    arc11 = GArc(200, 200, 90, 90)
    arc11.color = "Lime"
    window.add(arc11, x=250, y=100)
    arc12 = GArc(200, 200, 90, 90)
    arc12.color = "Lime"
    window.add(arc12, x=250, y=150)
    line1 = GLine(250, 150, 300, 150)
    line1.color = "Lime"
    window.add(line1)
    line2 = GLine(250, 200, 300, 200)
    line2.color = "Lime"
    window.add(line2)


def bg_4():
    bg4 = GRect(100, 100)
    bg4.filled = True
    bg4.color = "blue"
    bg4.fill_color = "blue"
    window.add(bg4, x=200, y=200)
    c6 = GOval(100, 20, x=200, y=210)
    c6.color = "white"
    window.add(c6)
    c7 = GOval(100, 20, x=200, y=220)
    c7.color = "white"
    window.add(c7)
    c8 = GOval(100, 20, x=200, y=230)
    c8.color = "white"
    window.add(c8)
    c9 = GOval(100, 20, x=200, y=240)
    c9.color = "white"
    window.add(c9)


def bg_5():
    bg5 = GRect(100, 100)
    bg5.filled = True
    bg5.color = "white"
    bg5.fill_color = "white"
    window.add(bg5, x=200, y=300)
    tri1 = GPolygon()
    tri1.add_vertex((200, 300))
    tri1.add_vertex((233, 350))
    tri1.add_vertex((200, 400))
    tri1.color = "Lime"
    tri1.filled = True
    tri1.fill_color = "Lime"
    window.add(tri1)
    tri2 = GPolygon()
    tri2.add_vertex((233, 300))
    tri2.add_vertex((267, 350))
    tri2.add_vertex((233, 400))
    tri2.color = "Lime"
    tri2.filled = True
    tri2.fill_color = "Lime"
    window.add(tri2)
    tri3 = GPolygon()
    tri3.add_vertex((267, 300))
    tri3.add_vertex((300, 350))
    tri3.add_vertex((267, 400))
    tri3.color = "Lime"
    tri3.filled = True
    tri3.fill_color = "Lime"
    window.add(tri3)


def bg_6():
    bg6 = GRect(200, 200)
    bg6.filled = True
    bg6.color = "lavender"
    bg6.fill_color = "lavender"
    window.add(bg6, x=0, y=200)
    arc1 = GArc(200, 200, 270, 90)
    arc1.filled = True
    arc1.color = "lavender"
    arc1.fill_color = "lime"
    window.add(arc1, x=-50, y=150)
    arc2 = GArc(200, 200, 270, 90)
    arc2.filled = True
    arc2.color = "lavender"
    arc2.fill_color = "lime"
    window.add(arc2, x=0, y=150)
    arc3 = GArc(200, 200, 270, 90)
    arc3.filled = True
    arc3.color = "lavender"
    arc3.fill_color = "lime"
    window.add(arc3, x=50, y=150)
    arc4 = GArc(400, 400, 0, 90)
    arc4.filled = True
    arc4.color = "lavender"
    arc4.fill_color = "lime"
    window.add(arc4, x=50, y=150)
    arc5 = GArc(200, 200, 180, 90)
    arc5.filled = True
    arc5.color = "lavender"
    arc5.fill_color = "lime"
    window.add(arc5, x=0, y=200)
    arc6 = GArc(400, 400, 180, 90)
    arc6.filled = True
    arc6.color = "lavender"
    arc6.fill_color = "lime"
    window.add(arc6, x=50, y=150)
    arc7 = GArc(200, 200, 180, 90)
    arc7.filled = True
    arc7.color = "lavender"
    arc7.fill_color = "lime"
    window.add(arc7, x=150, y=200)
    arc8 = GArc(200, 200, 0, 90)
    arc8.filled = True
    arc8.color = "lavender"
    arc8.fill_color = "lime"
    window.add(arc8, x=-50, y=300)
    arc9 = GArc(200, 200, 0, 90)
    arc9.filled = True
    arc9.color = "lavender"
    arc9.fill_color = "lime"
    window.add(arc9, x=0, y=300)
    arc10 = GArc(200, 200, 0, 90)
    arc10.filled = True
    arc10.color = "lavender"
    arc10.fill_color = "lime"
    window.add(arc10, x=100, y=300)
    arc11 = GArc(200, 200, 90, 90)
    arc11.filled = True
    arc11.color = "lavender"
    arc11.fill_color = "lime"
    window.add(arc11, x=0, y=350)
    arc12 = GArc(200, 200, 90, 90)
    arc12.filled = True
    arc12.color = "lavender"
    arc12.fill_color = "lime"
    window.add(arc12, x=50, y=350)
    arc13 = GArc(200, 200, 90, 90)
    arc13.filled = True
    arc13.color = "lavender"
    arc13.fill_color = "lime"
    window.add(arc13, x=100, y=350)
    arc14 = GArc(200, 200, 90, 90)
    arc14.filled = True
    arc14.color = "lavender"
    arc14.fill_color = "lime"
    window.add(arc14, x=150, y=350)
    arc15 = GArc(50, 25, 90, 180)
    arc15.filled = True
    arc15.color = "white"
    arc15.fill_color = "black"
    window.add(arc15, x=137, y=336)


def bg_7():
    bg7_1 = GRect(100, 100)
    bg7_1.color = "white"
    bg7_1.filled = True
    bg7_1.fill_color = "white"
    window.add(bg7_1, x=300, y=0)
    bg7_2 = GRect(200, 100)
    bg7_2.color = "lavender"
    bg7_2.filled = True
    bg7_2.fill_color = "lavender"
    window.add(bg7_2, x=400, y=0)
    tri4 = GPolygon()
    tri4.add_vertex((350, 0))
    tri4.add_vertex((450, 50))
    tri4.add_vertex((350, 100))
    tri4.color = "Lime"
    tri4.filled = True
    tri4.fill_color = "Lime"
    window.add(tri4)
    tri5 = GPolygon()
    tri5.add_vertex((450, 0))
    tri5.add_vertex((550, 50))
    tri5.add_vertex((450, 100))
    tri5.color = "Lime"
    tri5.filled = True
    tri5.fill_color = "Lime"
    window.add(tri5)
    tri6 = GPolygon()
    tri6.add_vertex((300, 0))
    tri6.add_vertex((400, 50))
    tri6.add_vertex((300, 100))
    tri6.color = "white"
    window.add(tri6)
    tri7 = GPolygon()
    tri7.add_vertex((400, 0))
    tri7.add_vertex((500, 50))
    tri7.add_vertex((400, 100))
    tri7.color = "white"
    window.add(tri7)
    tri8 = GPolygon()
    tri8.add_vertex((500, 0))
    tri8.add_vertex((600, 50))
    tri8.add_vertex((500, 100))
    tri8.color = "deeppink"
    window.add(tri8)


def bg_8():
    bg8_1 = GRect(200, 200)
    bg8_1.color = "lime"
    bg8_1.fill_color = "lime"
    bg8_1.filled = True
    window.add(bg8_1, x=300, y=100)
    c10 = GOval(100, 200)
    c10.color = "white"
    window.add(c10, x=350, y=100)
    c11 = GOval(100, 200)
    c11.color = "white"
    window.add(c11, x=400, y=100)
    l1 = GRect(200, 10)
    l1.color = "lavender"
    l1.filled = True
    l1.fill_color = "lavender"
    window.add(l1, x=300, y=120)
    l2 = GRect(200, 10)
    l2.color = "deeppink"
    l2.filled = True
    l2.fill_color = "deeppink"
    window.add(l2, x=300, y=140)
    l3 = GRect(200, 10)
    l3.color = "lavender"
    l3.filled = True
    l3.fill_color = "lavender"
    window.add(l3, x=300, y=160)
    l4 = GRect(200, 10)
    l4.color = "deeppink"
    l4.filled = True
    l4.fill_color = "deeppink"
    window.add(l4, x=300, y=180)
    bg8_2 = GRect(100, 100)
    bg8_2.color = "deeppink"
    bg8_2.fill_color = "deeppink"
    bg8_2.filled = True
    window.add(bg8_2, x=300, y=200)
    c16 = GOval(100, 20)
    c16.color = "lavender"
    window.add(c16, x=300, y=205)
    c17 = GOval(100, 20)
    c17.color = "lavender"
    window.add(c17, x=300, y=220)
    c12 = GOval(100, 20)
    c12.fill_color = "lavender"
    c12.filled = True
    c12.color = "lavender"
    window.add(c12, x=300, y=235)
    c13 = GOval(100, 20)
    c13.fill_color = "lavender"
    c13.filled = True
    c13.color = "lavender"
    window.add(c13, x=300, y=250)
    c14 = GOval(100, 20)
    c14.fill_color = "lavender"
    c14.filled = True
    c14.color = "lavender"
    window.add(c14, x=300, y=265)
    c15 = GOval(100, 20)
    c15.fill_color = "lavender"
    c15.filled = True
    c15.color = "lavender"
    window.add(c15, x=300, y=280)
    l5 = GRect(100, 10)
    l5.color = "lavender"
    l5.filled = True
    l5.fill_color = "lavender"
    window.add(l5, x=400, y=210)
    l6 = GRect(100, 10)
    l6.color = "deeppink"
    l6.filled = True
    l6.fill_color = "deeppink"
    window.add(l6, x=400, y=230)
    l7 = GRect(100, 10)
    l7.color = "lavender"
    l7.filled = True
    l7.fill_color = "lavender"
    window.add(l7, x=400, y=250)
    l8 = GRect(100, 10)
    l8.color = "deeppink"
    l8.filled = True
    l8.fill_color = "deeppink"
    window.add(l8, x=400, y=270)


def bg_9():
    bg9 = GRect(100, 100)
    bg9.color = "blue"
    bg9.filled = True
    bg9.fill_color = "blue"
    window.add(bg9, x=300, y=300)
    c13 = GOval(100, 100)
    c13.color = "lavender"
    window.add(c13, x=300, y=300)


def bg_10():
    bg10 = GRect(100, 100)
    bg10.color = "white"
    bg10.filled = True
    bg10.fill_color = "white"
    window.add(bg10, x=500, y=100)
    c14 = GOval(100, 100)
    c14.color = "lavender"
    c14.filled = True
    c14.fill_color = "lavender"
    window.add(c14, x=500, y=100)
    tri9 = GPolygon()
    tri9.add_vertex((500, 50))
    tri9.add_vertex((600, 100))
    tri9.add_vertex((500, 150))
    tri9.color = "deeppink"
    window.add(tri9)
    tri10 = GPolygon()
    tri10.add_vertex((500, 100))
    tri10.add_vertex((600, 150))
    tri10.add_vertex((500, 200))
    tri10.color = "deeppink"
    window.add(tri10)


def bg_11():
    bg11 = GRect(100, 100)
    bg11.color = "deeppink"
    bg11.filled = True
    bg11.fill_color = "deeppink"
    window.add(bg11, x=500, y=200)
    c15 = GOval(100, 100)
    c15.color = "lime"
    c15.filled = True
    c15.fill_color = "lime"
    window.add(c15, x=535, y=200)
    c16 = GOval(90, 100)
    c16.color = "deeppink"
    c16.filled = True
    c16.fill_color = "deeppink"
    window.add(c16, x=570, y=200)


def bg_12():
    bg12 = GRect(200, 100)
    bg12.color = "lime"
    bg12.filled = True
    bg12.fill_color = "lime"
    window.add(bg12, x=400, y=300)
    c16 = GOval(100, 100)
    c16.color = "white"
    window.add(c16, x=350, y=300)
    c17 = GOval(100, 100)
    c17.color = "white"
    window.add(c17, x=400, y=300)
    c18 = GOval(100, 100)
    c18.color = "white"
    window.add(c18, x=450, y=300)
    c19 = GOval(100, 100)
    c19.color = "white"
    window.add(c19, x=500, y=300)


def bg_13():
    bg13 = GRect(200, 100)
    bg13.color = "lime"
    bg13.filled = True
    bg13.fill_color = "lime"
    window.add(bg13, x=600, y=0)
    c17 = GOval(100, 100)
    c17.color = "lavender"
    c17.filled = True
    c17.fill_color = "lavender"
    window.add(c17, x=600, y=0)
    c18 = GOval(100, 100)
    c18.color = "lavender"
    c18.filled = True
    c18.fill_color = "lavender"
    window.add(c18, x=650, y=0)
    c19 = GOval(100, 100)
    c19.color = "lavender"
    c19.filled = True
    c19.fill_color = "lavender"
    window.add(c19, x=700, y=0)
    c20 = GOval(30, 80)
    c20.color = "lime"
    c20.filled = True
    c20.fill_color = "lime"
    window.add(c20, x=660, y=10)
    c21 = GOval(30, 80)
    c21.color = "lime"
    c21.filled = True
    c21.fill_color = "lime"
    window.add(c21, x=710, y=10)


def bg_14():
    bg14 = GRect(200, 100)
    bg14.color = "lime"
    bg14.filled = True
    bg14.fill_color = "lime"
    window.add(bg14, x=600, y=100)
    c22 = GOval(100, 100)
    c22.color = "white"
    window.add(c22, x=600, y=100)
    c23 = GOval(100, 100)
    c23.color = "white"
    window.add(c23, x=650, y=100)
    c24 = GOval(100, 100)
    c24.color = "white"
    window.add(c24, x=700, y=100)


def bg_15():
    bg15_1 = GRect(100, 100)
    bg15_1.color = "white"
    bg15_1.filled = True
    bg15_1.fill_color = "white"
    window.add(bg15_1, x=600, y=200)
    bg15_2 = GRect(100, 100)
    bg15_2.color = "white"
    bg15_2.filled = True
    bg15_2.fill_color = "white"
    window.add(bg15_2, x=700, y=200)
    tri11 = GPolygon()
    tri11.add_vertex((733, 200))
    tri11.add_vertex((700, 250))
    tri11.add_vertex((733, 300))
    tri11.color = "Lime"
    tri11.filled = True
    tri11.fill_color = "Lime"
    window.add(tri11)
    tri12 = GPolygon()
    tri12.add_vertex((767, 200))
    tri12.add_vertex((733, 250))
    tri12.add_vertex((767, 300))
    tri12.color = "Lime"
    tri12.filled = True
    tri12.fill_color = "Lime"
    window.add(tri12)
    tri13 = GPolygon()
    tri13.add_vertex((800, 200))
    tri13.add_vertex((767, 250))
    tri13.add_vertex((800, 300))
    tri13.color = "Lime"
    tri13.filled = True
    tri13.fill_color = "Lime"
    window.add(tri13)
    c29 = GOval(100, 100)
    c29.color = "lime"
    window.add(c29, x=620, y=200)
    c30 = GOval(100, 100)
    c30.color = "lime"
    c30.filled = True
    c30.fill_color = "lime"
    window.add(c30, x=600, y=200)


def bg_16():
    bg16 = GRect(200, 100)
    bg16.color = "white"
    bg16.filled = True
    bg16.fill_color = "white"
    window.add(bg16, x=600, y=300)
    c25 = GOval(100, 100)
    c25.color = "lavender"
    c25.filled = True
    c25.fill_color = "lavender"
    window.add(c25, x=550, y=300)
    c26 = GOval(100, 100)
    c26.color = "lime"
    window.add(c26, x=600, y=300)
    c27 = GOval(100, 100)
    c27.color = "blue"
    window.add(c27, x=650, y=300)
    c28 = GOval(100, 100)
    c28.color = "deeppink"
    window.add(c28, x=700, y=300)


def dot():
    dot1 = GOval(25, 25)
    dot1.color = "white"
    dot1.fill_color = "black"
    dot1.filled = True
    window.add(dot1, x=50, y=336)
    dot2 = GOval(25, 25)
    dot2.color = "black"
    dot2.fill_color = "white"
    dot2.filled = True
    window.add(dot2, x=75, y=336)
    dot3 = GOval(25, 25)
    dot3.color = "white"
    dot3.fill_color = "black"
    dot3.filled = True
    window.add(dot3, x=161, y=88)
    dot4 = GOval(25, 25)
    dot4.color = "black"
    dot4.fill_color = "white"
    dot4.filled = True
    window.add(dot4, x=186, y=88)
    dot5 = GOval(25, 25)
    dot5.color = "white"
    dot5.fill_color = "black"
    dot5.filled = True
    window.add(dot5, x=250, y=88)
    dot6 = GOval(25, 25)
    dot6.color = "black"
    dot6.fill_color = "white"
    dot6.filled = True
    window.add(dot6, x=275, y=88)
    dot7 = GOval(25, 25)
    dot7.color = "white"
    dot7.fill_color = "black"
    dot7.filled = True
    window.add(dot7, x=475, y=190)
    dot8 = GOval(25, 25)
    dot8.color = "black"
    dot8.fill_color = "white"
    dot8.filled = True
    window.add(dot8, x=500, y=190)
    dot9 = GOval(25, 25)
    dot9.color = "white"
    dot9.fill_color = "black"
    dot9.filled = True
    window.add(dot9, x=575, y=190)
    dot10 = GOval(25, 25)
    dot10.color = "black"
    dot10.fill_color = "white"
    dot10.filled = True
    window.add(dot10, x=600, y=190)
    dot11 = GOval(25, 25)
    dot11.color = "white"
    dot11.fill_color = "black"
    dot11.filled = True
    window.add(dot11, x=610, y=40)
    dot12 = GOval(25, 25)
    dot12.color = "black"
    dot12.fill_color = "white"
    dot12.filled = True
    window.add(dot12, x=635, y=40)
    dot13 = GOval(25, 25)
    dot13.color = "white"
    dot13.fill_color = "black"
    dot13.filled = True
    window.add(dot13, x=685, y=40)
    dot14 = GOval(25, 25)
    dot14.color = "black"
    dot14.fill_color = "white"
    dot14.filled = True
    window.add(dot14, x=710, y=40)


if __name__ == '__main__':
    main()
