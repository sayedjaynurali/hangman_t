import turtle
import random
from hangman_function import Hangman_Drawing, words
import pygame
pygame.mixer.init()

screen = turtle.Screen()
screen.title("Hangman Game")
screen.setup(width=1.0, height=1.0)  # full screen
screen.bgcolor("white")
screen.tracer(0)

drawer = Hangman_Drawing()

hint_writer = turtle.Turtle(); hint_writer.hideturtle(); hint_writer.penup()
word_writer = turtle.Turtle(); word_writer.hideturtle(); word_writer.penup()
status_writer = turtle.Turtle(); status_writer.hideturtle(); status_writer.penup()
result_writer = turtle.Turtle(); result_writer.hideturtle(); result_writer.penup()
restart_writer = turtle.Turtle(); restart_writer.hideturtle(); restart_writer.penup()
title_writer = turtle.Turtle(); title_writer.hideturtle(); title_writer.penup()
subtitle_writer = turtle.Turtle(); subtitle_writer.hideturtle(); subtitle_writer.penup()
deco_writer = turtle.Turtle(); deco_writer.hideturtle(); deco_writer.penup()
timer_writer = turtle.Turtle(); timer_writer.hideturtle(); timer_writer.penup()  # ⏱️ NEW

def display_text(writer, message, x, y, size=18, color="black", align="center"):
    writer.clear()
    writer.goto(x, y)
    writer.color(color)
    writer.write(message, align=align, font=("Arial", size, "bold"))

chosen_word = ""
chosen_word_list = []
word_to_guess = []
l = 0
parts = []
letter_buttons = {}
used_letters = set()
game_over = False
restart_box = None

# Timer variables
TIMER_DURATION = 90   # seconds for each game ⏱️
time_left = TIMER_DURATION
timer_running = False

MATH_SYMBOLS = ["π", "√", "∞", "∑", "∫", "∆", "θ", "≈", "≠", "±"]

DECOR_COLORS = [
    "#FFDAB9", "#B0E0E6", "#98FB98", "#FFFACD", "#FFB6C1",
    "#E0FFFF", "#D8BFD8", "#F5DEB3", "#F0FFF0", "#FFE4E1"
]

def draw_decorations():
    """Draw random math symbols + geometric shapes in pastel colors."""
    deco_writer.clear()

    for _ in range(8):  
        x = random.randint(-450, 450)
        y = random.randint(-300, 300)
        deco_writer.goto(x, y)
        deco_writer.color(random.choice(DECOR_COLORS))
        symbol = random.choice(MATH_SYMBOLS)
        deco_writer.write(symbol, align="center", font=("Arial", 18, "bold"))

    for _ in range(4): 
        x = random.randint(-400, 400)
        y = random.randint(-250, 250)
        size = random.randint(30, 60)
        shape = random.choice(["circle", "square", "triangle"])
        deco_writer.goto(x, y)
        deco_writer.pendown()
        color = random.choice(DECOR_COLORS)
        deco_writer.color(color, color)  
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

# Load sound effects
correct_sound = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/correct.mp3")
wrong_sound   = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/error.mp3")
win_sound     = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/victory.mp3")
lose_sound    = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/lost.mp3")

# ⏱️ TIMER FUNCTIONS
def update_timer():
    global time_left, timer_running
    if not timer_running:
        return
    if time_left > 0:
        display_text(timer_writer, f"Time: {time_left}", 400, 320, 20, "blue", "center")
        time_left -= 1
        screen.ontimer(update_timer, 1000)  # call again in 1s
    else:
        display_text(timer_writer, "Time: 0", 400, 320, 20, "red", "center")
        start_game()  # restart game automatically

def start_timer():
    global time_left, timer_running
    time_left = TIMER_DURATION
    timer_running = True
    update_timer()

def stop_timer():
    global timer_running
    timer_running = False

def start_game():
    global chosen_word, chosen_word_list, word_to_guess, l, parts, game_over, used_letters
    hint_writer.clear(); word_writer.clear(); status_writer.clear()
    result_writer.clear(); restart_writer.clear()
    title_writer.clear(); subtitle_writer.clear(); deco_writer.clear()
    timer_writer.clear()

    game_over = False
    used_letters = set()
    draw_decorations()
    drawer.draw_gallows()

    display_text(title_writer, "Hangman Game", 0, 320, 44, "darkblue")
    display_text(subtitle_writer, "Where Maths meets Python. Solve the puzzle, save the man",
                 0, 280, 20, "purple")

    chosen_word, hint = random.choice(list(words.items()))
    chosen_word = str(chosen_word).strip().upper()
    chosen_word_list = list(chosen_word)

    word_to_guess = [ch if not ch.isalpha() else "_" for ch in chosen_word_list]

    display_text(hint_writer, f"Hint: {hint}", 250, 150, 20, "darkgreen")
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
    start_timer()  # ⏱️ start new timer each game

def check_guess(letter):
    global l, game_over
    if game_over:
        return

    letter = letter.upper()
    if letter not in chosen_word_list:
        display_text(status_writer, "Wrong Guess!", 200, 0, 18, "red")
        wrong_sound.play()
        if l < len(parts):
            parts[l]()
        l += 1
    else:
        for pos, char in enumerate(chosen_word_list):
            if char == letter:
                word_to_guess[pos] = letter
        display_text(status_writer, "Correct Guess!", 200, 0, 18, "green")
        correct_sound.play()

    display_text(word_writer, " ".join(word_to_guess), 200, 50, 30, "black")

    if "_" not in word_to_guess:
        display_text(result_writer, f"You Win! Word: {chosen_word}", 200, -300, 24, "green")
        win_sound.play()
        stop_timer()
        draw_restart_button()
        game_over = True
    elif l >= len(parts):
        display_text(result_writer, f"You Lose! Word: {chosen_word}", 200, -300, 24, "red")
        lose_sound.play()
        stop_timer()
        game_over = True

def click_handler(x, y):
    global used_letters

    if restart_box:
        x1, y1, x2, y2 = restart_box
        if x1 <= x <= x2 and y1 <= y <= y2:
            start_game()
            return

    if game_over:
        return  

    for letter, (bx, by) in letter_buttons.items():
        if abs(x - bx) < 20 and abs(y - by) < 20:
            if letter in used_letters:
                return
            used_letters.add(letter)
            check_guess(letter)
            draw_buttons()
            return

start_game()
screen.onclick(click_handler)
turtle.done()



# import turtle
# import random
# from hangman_function import Hangman_Drawing, words
# import pygame
# pygame.mixer.init()

# screen = turtle.Screen()
# screen.title("Hangman Game")
# screen.setup(width=1.0, height=1.0)  # full screen
# screen.bgcolor("white")
# screen.tracer(0)

# drawer = Hangman_Drawing()

# hint_writer = turtle.Turtle(); hint_writer.hideturtle(); hint_writer.penup()
# word_writer = turtle.Turtle(); word_writer.hideturtle(); word_writer.penup()
# status_writer = turtle.Turtle(); status_writer.hideturtle(); status_writer.penup()
# result_writer = turtle.Turtle(); result_writer.hideturtle(); result_writer.penup()
# restart_writer = turtle.Turtle(); restart_writer.hideturtle(); restart_writer.penup()
# title_writer = turtle.Turtle(); title_writer.hideturtle(); title_writer.penup()
# subtitle_writer = turtle.Turtle(); subtitle_writer.hideturtle(); subtitle_writer.penup()
# deco_writer = turtle.Turtle(); deco_writer.hideturtle(); deco_writer.penup()

# def display_text(writer, message, x, y, size=18, color="black", align="center"):
#     writer.clear()
#     writer.goto(x, y)
#     writer.color(color)
#     writer.write(message, align=align, font=("Arial", size, "bold"))

# chosen_word = ""
# chosen_word_list = []
# word_to_guess = []
# l = 0
# parts = []
# letter_buttons = {}
# used_letters = set()
# game_over = False
# restart_box = None

# MATH_SYMBOLS = ["π", "√", "∞", "∑", "∫", "∆", "θ", "≈", "≠", "±"]

# DECOR_COLORS = [
#     "#FFDAB9",  # Peach Puff
#     "#B0E0E6",  # Powder Blue
#     "#98FB98",  # Pale Green
#     "#FFFACD",  # Lemon Chiffon
#     "#FFB6C1",  # Light Pink
#     "#E0FFFF",  # Light Cyan
#     "#D8BFD8",  # Thistle
#     "#F5DEB3",  # Wheat
#     "#F0FFF0",  # Honeydew
#     "#FFE4E1",  # Misty Rose
# ]

# def draw_decorations():
#     """Draw random math symbols + geometric shapes in pastel colors."""
#     deco_writer.clear()

#     for _ in range(8):  
#         x = random.randint(-450, 450)
#         y = random.randint(-300, 300)
#         deco_writer.goto(x, y)
#         deco_writer.color(random.choice(DECOR_COLORS))
#         symbol = random.choice(MATH_SYMBOLS)
#         deco_writer.write(symbol, align="center", font=("Arial", 18, "bold"))

#     for _ in range(4): 
#         x = random.randint(-400, 400)
#         y = random.randint(-250, 250)
#         size = random.randint(30, 60)
#         shape = random.choice(["circle", "square", "triangle"])
#         deco_writer.goto(x, y)
#         deco_writer.pendown()
#         color = random.choice(DECOR_COLORS)
#         deco_writer.color(color, color)  
#         deco_writer.begin_fill()
#         if shape == "circle":
#             deco_writer.circle(size)
#         elif shape == "square":
#             for _ in range(4):
#                 deco_writer.forward(size)
#                 deco_writer.right(90)
#         else:  # triangle
#             for _ in range(3):
#                 deco_writer.forward(size)
#                 deco_writer.left(120)
#         deco_writer.end_fill()
#         deco_writer.penup()

# def draw_buttons():
#     global letter_buttons
#     for btn in letter_buttons.values():
#         btn.clear() if isinstance(btn, turtle.Turtle) else None
#     letter_buttons = {}

#     x_start, y_start = 80, -50   # in Q4
#     spacing = 40
#     row_length = 7
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     for idx, letter in enumerate(letters):
#         row = idx // row_length
#         col = idx % row_length
#         x = x_start + col * spacing
#         y = y_start - row * spacing

#         btn = turtle.Turtle()
#         btn.hideturtle()
#         btn.speed(0)
#         btn.penup()
#         btn.goto(x, y)

#         if letter in used_letters:
#             btn.color("grey")
#         else:
#             btn.color("red")

#         btn.write(letter, align="center", font=("Arial", 18, "bold"))
#         letter_buttons[letter] = (x, y)

#     screen.update()

# def draw_restart_button(cx=200, cy=-360, width=140, height=50,
#                         border_color="black", fill_color="lightgrey",
#                         text="Restart", text_color="red",
#                         font=("Arial", 20, "bold"),
#                         vert_offset_factor=0.45):
#     global restart_box
#     restart_writer.clear()
#     restart_writer.penup()

#     x1 = cx - width / 2
#     y1 = cy - height / 2

#     restart_writer.setheading(0)
#     restart_writer.goto(x1, y1)
#     restart_writer.pendown()
#     restart_writer.color(border_color, fill_color)
#     restart_writer.begin_fill()
#     for _ in range(2):
#         restart_writer.forward(width)
#         restart_writer.left(90)
#         restart_writer.forward(height)
#         restart_writer.left(90)
#     restart_writer.end_fill()
#     restart_writer.penup()

#     font_size = font[1] if isinstance(font, tuple) and len(font) >= 2 else 20
#     y_text = cy - (font_size * vert_offset_factor)

#     restart_writer.goto(cx, y_text)
#     restart_writer.color(text_color)
#     restart_writer.write(text, align="center", font=font)

#     restart_box = (x1, y1, x1 + width, y1 + height)

# def hide_restart_button():
#     global restart_box
#     restart_writer.clear()
#     restart_box = None

# # Load sound effects (place your mp3 files in the same folder as the script)
# correct_sound = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/correct.mp3")
# wrong_sound   = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/error.mp3")
# win_sound     = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/victory.mp3")
# lose_sound    = pygame.mixer.Sound("/Users/sayedjaynurali/Desktop/HANGMAN_TF/lost.mp3")

# def start_game():
#     global chosen_word, chosen_word_list, word_to_guess, l, parts, game_over, used_letters
#     hint_writer.clear(); word_writer.clear(); status_writer.clear()
#     result_writer.clear(); restart_writer.clear()
#     title_writer.clear(); subtitle_writer.clear(); deco_writer.clear()

#     game_over = False
#     used_letters = set()
#     draw_decorations()
#     drawer.draw_gallows()

#     display_text(title_writer, "Hangman.py", 0, 320, 44, "darkblue")
#     display_text(subtitle_writer, "Where Maths meets Python. Solve the puzzle, save the man",
#                  0, 280, 20, "purple")


#     chosen_word, hint = random.choice(list(words.items()))
#     chosen_word = str(chosen_word).strip().upper()
#     chosen_word_list = list(chosen_word)

#     word_to_guess = [ch if not ch.isalpha() else "_" for ch in chosen_word_list]

#     display_text(hint_writer, f"Hint: {hint}", 250, 150, 20, "darkgreen")

#     display_text(word_writer, " ".join(word_to_guess), 200, 50, 30, "black")

#     parts = [
#         drawer.draw_head,
#         drawer.draw_body,
#         drawer.draw_left_arm,
#         drawer.draw_right_arm,
#         drawer.draw_left_leg,
#         drawer.draw_right_leg,
#     ]
#     l = 0

#     draw_buttons()
#     draw_restart_button()

# def check_guess(letter):
#     global l, game_over
#     if game_over:
#         return

#     letter = letter.upper()
#     if letter not in chosen_word_list:
#         display_text(status_writer, "Wrong Guess!", 200, 0, 18, "red")
#         wrong_sound.play()   # 🔊 play error sound
#         if l < len(parts):
#             parts[l]()
#         l += 1
#     else:
#         for pos, char in enumerate(chosen_word_list):
#             if char == letter:
#                 word_to_guess[pos] = letter
#         display_text(status_writer, "Correct Guess!", 200, 0, 18, "green")
#         correct_sound.play()  # 🔊 play correct sound

#     display_text(word_writer, " ".join(word_to_guess), 200, 50, 30, "black")

#     if "_" not in word_to_guess:
#         display_text(result_writer, f"You Win! Word: {chosen_word}", 200, -300, 24, "green")
#         win_sound.play()      # 🔊 play victory sound
#         draw_restart_button()
#         game_over = True
#     elif l >= len(parts):
#         display_text(result_writer, f"You Lose! Word: {chosen_word}", 200, -300, 24, "red")
#         lose_sound.play()     # 🔊 play lost sound
#         game_over = True

# def click_handler(x, y):
#     global used_letters

#     if restart_box:
#         x1, y1, x2, y2 = restart_box
#         if x1 <= x <= x2 and y1 <= y <= y2:
#             start_game()
#             return

#     if game_over:
#         return  

#     for letter, (bx, by) in letter_buttons.items():
#         if abs(x - bx) < 20 and abs(y - by) < 20:
#             if letter in used_letters:
#                 return
#             used_letters.add(letter)
#             check_guess(letter)
#             draw_buttons()
#             return

# start_game()
# screen.onclick(click_handler)
# turtle.done()