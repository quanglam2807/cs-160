# Quang Lam

import turtle

def drawSpiral(myTurtle, r):
    if r > 0:
        myTurtle.circle(r, 180)
        drawSpiral(myTurtle, r - 5)

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    
    drawSpiral(myTurtle, 120)
    myWin.exitonclick()    

if __name__ == "__main__":
    main()