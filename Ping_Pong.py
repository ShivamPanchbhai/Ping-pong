import turtle  # Turtle module allows some basic graphics
import winsound # it is used to import sound functions present in winsound module
window = turtle.Screen()  # creation of window using Screen function
window.title("Pong by Shivam Panchbhai")  # creating title of the game
window.bgcolor("black")  # seting background colour of the screen
window.setup(width=1280, height=720)  # setting the resolution of the screen up 360 bottom 360
window.tracer(0)  # tracer function stops the window from updating automatically
                  # and we have to update it manually as done in the main loop

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()  # Turtle is a class name
paddle_a.speed(0)  # this is the speed of the paddle animation initialised to maximum
paddle_a.shape("square")  # shape of the pedal
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # resizing the paddle dimensions from default 20*20
paddle_a.color("white")  # colour of the paddle
paddle_a.penup()  # turtle draws a line as the paddle moves and this function make sures it doesn't make the line
paddle_a.goto(-450, 0)  # 00 is the centre coordinates and goto() will go to x axis(-450)

# paddle B
paddle_b = turtle.Turtle()  # Turtle is a class name
paddle_b.speed(0)  # this is the speed of the paddle animation initialised to maximum
paddle_b.shape("square")  # shape of the pedal
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # resizing the paddle dimensions from default 20*20
paddle_b.color("white")  # colour of the paddle
paddle_b.penup()  # turtle draws a line as the paddle moves and this function make sures it doesn't make the line
paddle_b.goto(450, 0)  # 00 is the centre coordinates and goto() will go to x axis(450)

# ball
ball = turtle.Turtle()  # Turtle is a class name
ball.speed(0)  # this is the speed of the paddle animation initialised to maximum
ball.shape("circle")  # shape of the ball
ball.color("white")  # colour of the ball
ball.penup()  # turtle draws a line as the ball moves and this function make sures it doesn't make the line
ball.goto(0, 0)  # 00 is the centre coordinates and goto() will go to x axis(0)

#pen scoreboard
pen = turtle.Turtle()  # turtle is the module name and Turtle is the class name
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# ball movement
# the ball movement is seperated in to two parts dx and dy
ball.dx = 0.3  # this means that ball is moved by 2 pixels in x axis in upward right direction
ball.dy = -0.3  # this means that ball is moved by 2 pixels in y axis in upward right direction
# function
def paddle_a_up(): # function to move paddle a up
    y = paddle_a.ycor()  # ycor is from the turtle module and it returns the y coordinates
    y += 20  # y is +ve because of the coordinate system(it is going up)
    paddle_a.sety(y)  # updating the value of paddle a in y cooridnates

def paddle_a_down(): # function to move paddle a down
        y = paddle_a.ycor()  # ycor is from the turtle module and it returns the y coordinates
        y -= 20  # y is -ve because of the coordinate system(it is going down)
        paddle_a.sety(y)  # updating the value of paddle a in y cooridnates

def paddle_b_up():# function to move paddle b up
    y = paddle_b.ycor()  # ycor is from the turtle module and it returns the y coordinates
    y += 20  # y is +ve because of the coordinate system(it is going up)
    paddle_b.sety(y)  # updating the value of paddle a in y coordinates

def paddle_b_down(): # function to move paddle b down
        y = paddle_b.ycor()  # ycor is from the turtle module and it returns the y coordinates
        y -= 20  # y is -ve because of the coordinate system(it is going down)
        paddle_b.sety(y)  # updating the value of paddle b in y coordinates
# keyboard binding
window.listen()  #listening the keyboard input
window.onkeypress(paddle_a_up, "w")  # onkeypress is a method and when w is pressed it call the function paddle_a_up
window.onkeypress(paddle_a_down, "s")  # onkeypress is a method and when d is pressed call the function paddle_a_down
window.onkeypress(paddle_b_up, "Up")  # onkeypress is a method and when Up is pressed it call the function paddle_b_up
window.onkeypress(paddle_b_down, "Down")  # onkeypress is a method and when Down is pressed call the function paddle_b_down






# Main game loop
while True:
    window.update()
# moving ball()
# ball start at (0,0)[xcor(),ycor()] and executing the main loop it's value will be 0.1 and keep on increasing
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# border collision checking top and bottom
    if ball.ycor() > 350:  # 350 because the above screen ends at 360
        ball.sety(350)  # setting the position back to 290
        ball.dy *= -1  # reversing the direction of the ball after collision by making the ball go down in y direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   # plays sound when border is touched

    if ball.ycor() < -350:  # -350 because the below screen ends at -360
        ball.sety(-350)  # setting the position back to -350
        ball.dy *= -1  # reversing the direction of the ball after collision by making the ball go down in y direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   # plays sound when border is touched

# border collision checking right and left
    if ball.xcor() > 630:  # 630 because the right screen ends at 640
        ball.goto(0, 0)  # setting the position back to 00
        ball.dx *= -1  # reversing the direction of the ball after collision by making the ball go down in y direction
        score_a += 1  # when the ball goes beyond the 'b bat' 'a' gets a score
        pen.clear()  # clearing the previous written value on scoreboard
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -630:  # -630 because the below screen ends at -640
        ball.goto(0, 0)  # setting the position back to 00
        ball.dx *= -1  # reversing the direction of the ball after collision by making the ball go down in y direction
        score_b += 1  # when the ball goes beyond the 'bat a' 'b' gets a score
        pen.clear()  # clearing the previous written value on scoreboard
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        # updating player A and player B value by using format()

# paddle and ball collisions
    # paddle b
    if (ball.xcor() > 440 and ball.xcor()<450) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):  # 440 because paddle b is at 450
    # and we are checking whether the ball touches in between the paddle in +50 from paddle_b y_position(0) and -50 from paddle_b y position(0)
       ball.setx(340) # set the ball back to 340 position
       ball.dx *= -1  # sending the ball in the opposite direction from where it came
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   # plays sound when paddle is touched

    # paddle a
    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):  # 440 because paddle b is at 450
        # and we are checking whether the ball touches in between the paddle in +50 from paddle_b y_position(0) and -50 from paddle_b y position(0)
        ball.setx(-340)  # set the ball back to 340 position
        ball.dx *= -1  # sending the ball in the opposite direction from where it came
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   # plays sound when paddle is touched