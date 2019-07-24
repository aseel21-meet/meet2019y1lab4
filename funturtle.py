import turtle
turtle.shape('square')
turtle.shape('turtle')
finn=turtle.clone()
finn.shape('square')
finn.goto(100,100)
finn.goto(0,200)
finn.goto(-100,100)
finn.goto(0,0)
charlie=turtle.clone()
charlie.shape("triangle")
charlie.goto(100,0)
charlie.goto(0,100)
charlie.goto (-100,0)
charlie.goto(0,0)
finn.goto(300,300)
id1=finn.stamp()
finn.goto(100,100)
id2=finn.stamp()
finn.goto(-250,-100)
finn.clearstamp()





turtle.mainloop()
