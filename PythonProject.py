# import the modules
import tkinter;
import random;
from tkinter import *;
from PIL import ImageTk, Image;

# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Magenta', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially 30 seconds.
timeLeft = 30


# function that will start the game.
def startGame(event):
    if timeLeft == 30:
        # start the countdown timer.
        countdown();

    # run the function to
    # choose the next colour.
    nextColour();


# Function to choose and
def restart():
    global timeLeft;
    global score;
    # flushing all the widgets
    if timeLeft <= 0:
        timeLeft = 30;
        score = 0;
        scoreLabel.config(text="Score: " + str(score));
        timeLabel.config(text="Time left: " + str(timeLeft));
        enterLabel.config(text="Press enter to start", fg="#1c0eef");
        e.delete(0, tkinter.END);
        label.config(text="");
        e.focus_set();


# Function to choose and
# display the next colour.
def nextColour():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score;
    global timeLeft;

    # if a game is currently in play
    if timeLeft > 0:
        # showing ststus of play
        enterLabel.config(text="Game in play->", fg="green");

        # make the text entry box active.
        e.focus_set();

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == "pink" and colours[1].lower() == "magenta":
            score += 1;
        elif e.get().lower() == colours[1].lower():
            score += 1;

        # clear the text entry box.
        e.delete(0, tkinter.END);

        random.shuffle(colours);

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        if colours[0].lower() == "magenta":
            label.config(fg=str(colours[1]), text="Pink");
        else:
            label.config(fg=str(colours[1]), text=str(colours[0]));

        # update the score.
        scoreLabel.config(text="Score: " + str(score));
    else:
        enterLabel.config(text="Time up!!", fg="red");
    # Countdown timer function


def countdown():
    global timeLeft;

    # if a game is in play
    if timeLeft > 0:
        # decrement the timer.
        timeLeft -= 1;

        # update the time left label
        timeLabel.config(text="Time left: " + str(timeLeft));

        # run the function again after 1 second.
        timeLabel.after(1000, countdown);

    # Driver Code


# create a GUI window
root = tkinter.Tk();

canvas = Canvas(root, width=512, height=512);
image = ImageTk.PhotoImage(Image.open("C:\\Users\\anike\\OneDrive\\Desktop\\java\\Images\\color.png"));
canvas.create_image(0, 0, anchor=NW, image=image);
canvas.pack();

# set the title
root.title("COLORGAME");

# set the size
root.geometry("512x512");

# add an instructions label
instructions = tkinter.Label(root, text="Type in the colour"
                                        "of the words, and not the word text!",
                             font=('Lucida Calligraphy', 13));
instructions.place(x=8, y=10);

# add a enter label
enterLabel = tkinter.Label(root, text="Press enter to start", font=('Lucida Calligraphy', 13), fg="#1c0eef")
enterLabel.place(x=150, y=390, width=250, height=29);

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeLeft), font=('Lucida Calligraphy', 13));

timeLabel.place(x=100,y=100);

# add a score label
scoreLabel = tkinter.Label(root, text="Score: 0",
                           font=('Lucida Calligraphy', 13));
scoreLabel.place(x=300, y=100, width=100, height=29);

# add a label for displaying the colours
label = tkinter.Label(root, width=6, height=1, font=('Lucida Calligraphy', 40), bg="#c1c1c1");
label.place(x=150, y=200);

# add a text entry box for
# typing in colours
e = tkinter.Entry(root, font=('Lucida Calligraphy', 15));
e.place(x=200, y=325, width=125, height=30);

# restart button
rs = tkinter.Button(root, text="Restart ⟳", font=('Lucida Calligraphy', 13, "bold"), bg="#317ad6",fg="white", command=restart);
rs.place(x=208, y=450, width=110, height=29);

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame);

# set focus on the entry box
e.focus_set();

# start the GUI
root.mainloop();
