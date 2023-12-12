import turtle
import time
import datetime as dt

def main():
    t = turtle.Turtle() #for displaying time
    t1 = turtle.Turtle() #for creating rectangle box
    s = turtle.Screen()
    s.bgcolor("blue")

    hr = dt.datetime.now().hour
    min = dt.datetime.now().minute
    sec = dt.datetime.now().second

    t1.pensize(9)
    t.color('red')
    t1.color('red')
    t1.penup()

    t.goto(-170,0)
    t1.goto(-175,0)
    t1.pendown()
 
    for i in range(2):
        t1.forward(375)
        t1.left(90)
        t1.forward(120)
        t1.left(90)

    while True:
        t.hideturtle()
        t.clear()
        # display the time
        t.write(str(hr).zfill(2) + ":"+str(min).zfill(2)+":" + str(sec).zfill(2), font=("Times New Roman", 75, "bold"))
        time.sleep(1)
        sec += 1
    
        if sec == 60:
            sec = 0
            min += 1
    
        if min == 60:
            min = 0
            hr += 1
    
        if hr == 13:
            hr = 1

if __name__ == "__main__":
  main()