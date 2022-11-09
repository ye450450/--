import turtle

def drawPolygon(sideLength, numSides, col):
    t= turtle.Turtle()
    t.color(col)
    turnAngle= 360/numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

drawPolygon(50,4,"green")
drawPolygon(60,5,"darkgrey")
drawPolygon(70,8,"orange")
drawPolygon(15,30,"red")
