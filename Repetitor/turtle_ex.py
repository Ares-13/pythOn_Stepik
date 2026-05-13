import turtle as t

# настройки
k = 30 # размер шага в пикселях
t.tracer(0) # мгновенная отрисовка
t.left(90) # куда она смотрит
t.pendown() # хвост опущен

t.right(270)

for i in range(2):
    t.forward(8*k)
    t.right(120)

t.right(120)

for i in range(2):
    t.right(120)
    t.forward(3*k)
    t.right(240)

t.right(240)

for i in range(2):    
    t.forward(14*k)
    t.right(120)

t.penup() # убрать кисточку(закончить рисовать)

for ix in range(-15, 15):
    for iy in range(-5, 15):
        t.goto(ix * k,  iy * k) # направление движения черепахи
        t.dot(3, "red" if ix==0 or iy ==0 else "blue") # (размер точки)
t.update()
t.done()