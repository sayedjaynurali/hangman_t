from turtle import Turtle

class Hangman_Drawing:

    def __init__(self):
        self.tim = Turtle()
        self.tim.shape("turtle")
        self.tim.shapesize(1.5)

    def reset_pen(self, color="black", size=4):
        """Utility: reset pen style."""
        self.tim.color(color)
        self.tim.pensize(size)

    def draw_gallows(self):
        self.tim.reset()
        self.tim.hideturtle()
        self.tim.speed(0)
        self.reset_pen("saddlebrown", 8)  # brown gallows, thick

        # Gallows centered on negative x-axis (spanning Q2 + Q3)
        self.tim.penup()
        self.tim.goto(-400, -300)
        self.tim.pendown()
        self.tim.forward(200)
        self.tim.back(100)
        self.tim.left(90)
        self.tim.forward(400)
        self.tim.right(90)
        self.tim.forward(120)
        self.tim.right(90)
        self.tim.forward(60)

        self.reset_pen("black", 5)  # switch to black for hangman

    def draw_head(self):
        self.tim.right(90)
        self.tim.circle(30)

    def draw_body(self):
        self.tim.left(90)
        self.tim.penup()
        self.tim.forward(60)
        self.tim.pendown()
        self.tim.forward(100)

    def draw_left_arm(self):
        self.tim.back(50)
        self.tim.left(45)
        self.tim.forward(60)
        self.tim.back(60)
        self.tim.right(45)

    def draw_right_arm(self):
        self.tim.right(45)
        self.tim.forward(60)
        self.tim.back(60)
        self.tim.left(45)

    def draw_left_leg(self):
        self.tim.forward(50)
        self.tim.left(30)
        self.tim.forward(80)
        self.tim.back(80)
        self.tim.right(30)

    def draw_right_leg(self):
        self.tim.right(30)
        self.tim.forward(80)
        self.tim.back(80)
        self.tim.left(30)



# Math-related words with hints
words = {
    'algebra': "I speak with letters, but I always mean numbers. Who am I?",
    'algorithm': "I'm a recipe, not for food but for solutions.",
    'angle': "I measure the turn when two lines decide to meet.",
    'area': "I tell you how much paint you need to cover the floor."
}




import turtle
import random
from hangman_function import Hangman_Drawing, words

# -----------------------------
# Setup screen
# -----------------------------
screen = turtle.Screen()
screen.title("Hangman Game")
screen.setup(width=1.0, height=1.0)  # full screen
screen.bgcolor("white")
screen.tracer(0)

# -----------------------------
# Hangman Drawer
# -----------------------------
drawer = Hangman_Drawing()

# -----------------------------
# Writers
# -----------------------------
hint_writer = turtle.Turtle(); hint_writer.hideturtle(); hint_writer.penup()
word_writer = turtle.Turtle(); word_writer.hideturtle(); word_writer.penup()
status_writer = turtle.Turtle(); status_writer.hideturtle(); status_writer.penup()
result_writer = turtle.Turtle(); result_writer.hideturtle(); result_writer.penup()
restart_writer = turtle.Turtle(); restart_writer.hideturtle(); restart_writer.penup()
title_writer = turtle.Turtle(); title_writer.hideturtle(); title_writer.penup()
subtitle_writer = turtle.Turtle(); subtitle_writer.hideturtle(); subtitle_writer.penup()
deco_writer = turtle.Turtle(); deco_writer.hideturtle(); deco_writer.penup()

def display_text(writer, message, x, y, size=18, color="black", align="center"):
    writer.clear()
    writer.goto(x, y)
    writer.color(color)
    writer.write(message, align=align, font=("Arial", size, "bold"))

# -----------------------------
# Global state
# -----------------------------
chosen_word = ""
chosen_word_list = []
word_to_guess = []
l = 0
parts = []
letter_buttons = {}
used_letters = set()
game_over = False
restart_box = None

# -----------------------------
# Decorations
# -----------------------------
MATH_SYMBOLS = ["π", "√", "∞", "∑", "∫", "∆", "θ", "≈", "≠", "±"]

# In hangman.py, near the top
DECOR_COLORS = [
    "#FFDAB9",  # Peach Puff
    "#B0E0E6",  # Powder Blue
    "#98FB98",  # Pale Green
    "#FFFACD",  # Lemon Chiffon
    "#FFB6C1",  # Light Pink
    "#E0FFFF",  # Light Cyan
    "#D8BFD8",  # Thistle
    "#F5DEB3",  # Wheat
    "#F0FFF0",  # Honeydew
    "#FFE4E1",  # Misty Rose
]

def draw_decorations():
    """Draw random math symbols + geometric shapes in pastel colors."""
    deco_writer.clear()

    # Draw random math symbols
    for _ in range(8):  # more symbols for aesthetics
        x = random.randint(-450, 450)
        y = random.randint(-300, 300)
        deco_writer.goto(x, y)
        deco_writer.color(random.choice(DECOR_COLORS))
        symbol = random.choice(MATH_SYMBOLS)
        deco_writer.write(symbol, align="center", font=("Arial", 18, "bold"))

    # Draw random geometric filled shapes
    for _ in range(4):  # a few shapes
        x = random.randint(-400, 400)
        y = random.randint(-250, 250)
        size = random.randint(30, 60)
        shape = random.choice(["circle", "square", "triangle"])
        deco_writer.goto(x, y)
        deco_writer.pendown()
        color = random.choice(DECOR_COLORS)
        deco_writer.color(color, color)  # outline + fill same pastel color
        deco_writer.begin_fill()
        if shape == "circle":
            deco_writer.circle(size)
        elif shape == "square":
            for _ in range(4):
                deco_writer.forward(size)
                deco_writer.right(90)
        else:  # triangle
            for _ in range(3):
                deco_writer.forward(size)
                deco_writer.left(120)
        deco_writer.end_fill()
        deco_writer.penup()

# -----------------------------
# Functions
# -----------------------------
def draw_buttons():
    global letter_buttons
    for btn in letter_buttons.values():
        btn.clear() if isinstance(btn, turtle.Turtle) else None
    letter_buttons = {}

    x_start, y_start = 80, -50   # in Q4
    spacing = 40
    row_length = 7
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for idx, letter in enumerate(letters):
        row = idx // row_length
        col = idx % row_length
        x = x_start + col * spacing
        y = y_start - row * spacing

        btn = turtle.Turtle()
        btn.hideturtle()
        btn.speed(0)
        btn.penup()
        btn.goto(x, y)

        if letter in used_letters:
            btn.color("grey")
        else:
            btn.color("red")

        btn.write(letter, align="center", font=("Arial", 18, "bold"))
        letter_buttons[letter] = (x, y)

    screen.update()

def draw_restart_button(cx=200, cy=-360, width=140, height=50,
                        border_color="black", fill_color="lightgrey",
                        text="Restart", text_color="red",
                        font=("Arial", 20, "bold"),
                        vert_offset_factor=0.45):
    global restart_box
    restart_writer.clear()
    restart_writer.penup()

    x1 = cx - width / 2
    y1 = cy - height / 2

    restart_writer.setheading(0)
    restart_writer.goto(x1, y1)
    restart_writer.pendown()
    restart_writer.color(border_color, fill_color)
    restart_writer.begin_fill()
    for _ in range(2):
        restart_writer.forward(width)
        restart_writer.left(90)
        restart_writer.forward(height)
        restart_writer.left(90)
    restart_writer.end_fill()
    restart_writer.penup()

    font_size = font[1] if isinstance(font, tuple) and len(font) >= 2 else 20
    y_text = cy - (font_size * vert_offset_factor)

    restart_writer.goto(cx, y_text)
    restart_writer.color(text_color)
    restart_writer.write(text, align="center", font=font)

    restart_box = (x1, y1, x1 + width, y1 + height)

def hide_restart_button():
    global restart_box
    restart_writer.clear()
    restart_box = None

def start_game():
    global chosen_word, chosen_word_list, word_to_guess, l, parts, game_over, used_letters
    hint_writer.clear(); word_writer.clear(); status_writer.clear()
    result_writer.clear(); restart_writer.clear()
    title_writer.clear(); subtitle_writer.clear(); deco_writer.clear()

    game_over = False
    used_letters = set()
    draw_decorations()
    drawer.draw_gallows()

    # Title + Subtitle
    display_text(title_writer, "Hangman.py", 0, 320, 44, "darkblue")
    display_text(subtitle_writer, "Where Maths meets Python. Solve the puzzle, save the man",
                 0, 280, 20, "purple")

    # Decorations
    # draw_decorations()

    # Pick a random word + hint
    chosen_word, hint = random.choice(list(words.items()))
    chosen_word = str(chosen_word).strip().upper()
    chosen_word_list = list(chosen_word)

    word_to_guess = [ch if not ch.isalpha() else "_" for ch in chosen_word_list]

    # Hint (Q1 center)
    display_text(hint_writer, f"Hint: {hint}", 250, 150, 20, "darkgreen")

    # Word blanks (on +x axis center)
    display_text(word_writer, " ".join(word_to_guess), 200, 50, 30, "black")

    parts = [
        drawer.draw_head,
        drawer.draw_body,
        drawer.draw_left_arm,
        drawer.draw_right_arm,
        drawer.draw_left_leg,
        drawer.draw_right_leg,
    ]
    l = 0

    draw_buttons()
    draw_restart_button()

def check_guess(letter):
    global l, game_over
    if game_over:
        return

    letter = letter.upper()
    if letter not in chosen_word_list:
        display_text(status_writer, "Wrong Guess!", 200, 0, 18, "red")
        if l < len(parts):
            parts[l]()
        l += 1
    else:
        for pos, char in enumerate(chosen_word_list):
            if char == letter:
                word_to_guess[pos] = letter
        display_text(status_writer, "Correct Guess!", 200, 0, 18, "green")

    display_text(word_writer, " ".join(word_to_guess), 200, 50, 30, "black")

    if "_" not in word_to_guess:
        display_text(result_writer, f"You Win! Word: {chosen_word}", 200, -300, 24, "green")
        draw_restart_button()
        game_over = True
    elif l >= len(parts):
        display_text(result_writer, f"You Lose! Word: {chosen_word}", 200, -300, 24, "red")
        
        game_over = True

def click_handler(x, y):
    global used_letters

    # Check restart button click FIRST, always
    if restart_box:
        x1, y1, x2, y2 = restart_box
        if x1 <= x <= x2 and y1 <= y <= y2:
            start_game()
            return

    # Letter buttons click
    if game_over:
        return  # no letter guesses after game ends

    for letter, (bx, by) in letter_buttons.items():
        if abs(x - bx) < 20 and abs(y - by) < 20:
            if letter in used_letters:
                return
            used_letters.add(letter)
            check_guess(letter)
            draw_buttons()
            return

# -----------------------------
# Main
# -----------------------------
start_game()
screen.onclick(click_handler)
turtle.done()
