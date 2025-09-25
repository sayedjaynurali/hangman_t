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
        self.reset_pen("saddlebrown", 8)  

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

        self.reset_pen("black", 5)  

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



words = {
    'algebra': "I speak with letters, but I always mean numbers. Who am I?",
    'algorithm': "I’m a set of steps, precise and neat, follow me through and problems retreat.",
    'angle': "I measure the turn when two lines decide to meet.",
    'area': "I tell you how much paint you need to cover the floor.",
    'axiom': "I’m the rule everyone accepts without argument.",
    'binomial': "I come in twos, joined by a plus or minus.",
    'calculus': "I’m the math of change, both instant and vast.",
    'circle': "I’m round and endless, with no beginning or end.",
    'coefficient': "I sit in front of a variable, powerful yet quiet.",
    'combinatorics': "I count choices, orders, and possibilities.",
    'cone': "Pointy at the top, round at the bottom, like ice-cream.",
    'congruence': "When sides and angles all agree, two figures become copies of me.",
    'cosine': "Adjacent over hypotenuse — that’s my claim to fame.",
    'cylinder': "I look like a soda can — round top, round bottom.",
    'denominator': "I live under the fraction line.",
    'derivative': "I’m the slope’s secret twin — instant change.",
    'diameter': "I cross the circle through its heart.",
    'dimension': "From a point to a line, a plane to a cube — I measure the degrees of freedom in your group.",
    'distribution': "I scatter values — sometimes normal, sometimes wild.",
    'divisor': "I divide numbers cleanly, leaving nothing behind.",
    'ellipse': "Not a circle, not a line — I balance on two foci.",
    'equation': "Two sides of me must always agree.",
    'exponent': "I sit high and make numbers explode.",
    'factorial': "I’m a countdown party — each number joins the multiplication train.",
    'fibonacci': "I grow remembering my last two steps.",
    'fraction': "I’m a slice of the whole pie.",
    'function': "Give me input, I’ll always return output.",
    'geometry': "I’m the art of shapes and spaces.",
    'gradient': "Change in y over change in x — that’s my secret formula.",
    'graph': "Axes, points, lines — I reveal patterns hidden in numbers.",
    'hypotenuse': "Across from 90°, I stand the longest of all.",
    'identity': "I never change, I stay the same in every case.",
    'inequality': "I’m not equal — greater or lesser, that’s me.",
    'infinity': "I never end, never stop — forever.",
    'integral': "I collect tiny parts into a whole curve.",
    'intersection': "Where sets shake hands and meet.",
    'inverse': "I undo what’s been done — the great reverser.",
    'irrational': "I never repeat, never end, but real nonetheless.",
    'isosceles': "I can’t help having two equal sides.",
    'limit': "I’m what you approach but may never reach.",
    'line': "I stretch forever, straight and unbending.",
    'logarithm': "I tell you the exponent that got you here.",
    'mean': "Add them all up, then share them equally — that’s me.",
    'median': "I’m the middle child of data.",
    'mode': "I love popularity — I appear the most.",
    'multiple': "I’m born when numbers repeat themselves.",
    'negative': "I live below zero, the opposite of positive.",
    'normal': "I stand tall — perpendicular and fair.",
    'numerator': "I proudly sit on top of fractions.",
    'octagon': "I wear eight sides like armor.",
    'parallel': "Like best friends walking forever, but never hugging.",
    'parabola': "Throw a ball, I’ll show you its path.",
    'perimeter': "Walk around me, and you measure me.",
    'permutation': "I care about order — who sits where matters.",
    'pi': "Endless, irrational, and the circle’s best friend.",
    'plane': "Flat and endless, like invisible paper.",
    'point': "No size, but I exist everywhere.",
    'polygon': "From three to ten (or more!), I’m the many-sided crew.",
    'polynomial': "I’m powers of x stacked together.",
    'prime': "Indivisible except by 1 and me.",
    'probability': "I whisper the odds of what could happen.",
    'product': "Two numbers meet, and I’m the result of their party.",
    'proof': "I convince the world with logic.",
    'proportion': "Two ratios, perfectly balanced.",
    'pyramid': "I point to the sky with a polygon base.",
    'quadratic': "I always curve into a U-shape.",
    'quotient': "I’m what you get when you divide.",
    'radius': "From circle’s center to its edge, that’s me.",
    'range': "I measure the gap between high and low.",
    'ratio': "I compare two numbers simply.",
    'rectangle': "I have right angles everywhere.",
    'rhombus': "Equal sides, tilted square.",
    'scalar': "Just a number — no direction attached.",
    'sequence': "Numbers marching in order.",
    'set': "I gather unique objects into one family.",
    'sine': "Opposite side divided by hypotenuse — that’s me.",
    'sphere': "I’m a perfect 3D ball.",
    'square': "Equal sides, right corners — perfection.",
    'statistics': "I make numbers tell a story.",
    'subtraction': "I take away and leave what’s left.",
    'sum': "I’m the result of adding up.",
    'symmetry': "Flip me, turn me — I stay the same.",
    'tangent': "I touch a curve at exactly one spot.",
    'theorem': "I’m a truth proven with reason.",
    'triangle': "Three edges, three angles, and endless possibilities.",
    'variable': "The shape-shifter in every formula.",
    'vector': "I march with size and direction.",
    'vertex': "Where edges meet, sharp and clear.",
    'volume': "Fill me up, pour me out — I keep track of the space about.",

    'atom': "I’m tiny, invisible to eyes, yet I build everything.",
    'galaxy': "I hold billions of stars — and you’re in one.",
    'gravity': "I keep you on Earth, not floating away.",
    'oxygen': "Breathe me or you won’t last a minute.",
    'volcano': "I explode with fire and lava when angry.",
    'desert': "Hot, dry, endless sand playground.",
    'ocean': "I’m salty, deep, and cover most of Earth.",
    'earthquake': "I shake the ground under your feet.",
    'rainbow': "I appear when light and raindrops dance.",
    'tornado': "I spin faster than a dancer, destroying paths.",
    'tsunami': "I’m the ocean’s sprint, a wave that doesn’t tire.",
    'mountain': "I stand tall, scraping the sky.",
    'river': "I flow endlessly, carving the land.",
    'island': "Water surrounds me — I’m all alone.",
    'forest': "I’m green, dense, and full of secrets.",
    'desert': "I burn by day, freeze by night.",
    'voltage': "I tell electrons where to go and how fast to run.",
    'current': "I’m the river of electricity.",
    'neutron': "I’m neutral but vital inside atoms.",
    'proton': "I’m positive by nature, at an atom’s heart.",
    'electron': "I’m tiny, negative, always zipping around.",
    'blackhole': "I eat everything, even light.",
    'robot': "I follow commands — sometimes smarter than humans.",
    'rocket': "I leave Earth in fire and thunder.",
    'planet': "I orbit stars — some are home to life.",
    'asteroid': "I wander space, rocky and wild.",
    'comet': "I carry icy tails, blazing through space.",
    'dinosaur': "I stomped, I roared, long before you were born.",
    'brain': "I’m squishy but smarter than any computer.",
    'heart': "I pump life nonstop until you stop.",
    'DNA': "I carry the code that makes you, you.",
    'cell': "I’m tiny but alive — life’s building block.",
    'virus': "I invade, multiply, and cause chaos.",
    'bacteria': "I can help you digest or make you sick.",
    'engine': "I roar with fuel and make wheels turn.",
    'bridge': "I connect lands, standing over rivers.",
    'tower': "I rise high, touching the clouds.",
    'train': "I run on tracks, carrying stories.",
    'airplane': "I fly higher than birds.",
    'internet': "I connect the world in a click.",
    'computer': "Brilliant assistant, obedient mind.",
    'python': "I’m a snake, but also a language.",
    'java': "I’m coffee in a cup, but also code.",
    'keyboard': "I help you talk to computers.",
    'mouse': "I’m not squeaky — I click.",
    'phone': "I ring, buzz, and keep you addicted.",
    'camera': "I freeze moments in frames.",
    'music': "I make your soul dance.",
    'guitar': "Six strings, endless emotions.",
    'piano': "Black and white soldiers march, and I make them sing.",
    'football': "I roll, I bounce, I make crowds scream.",
    'cricket': "Bat, ball, stumps — my game.",
    'basketball': "I bounce and swish through hoops.",
    'chess': "I’m war without bloodshed — kings and queens fight here.",
    'school': "I teach, punish, and prepare you.",
    'teacher': "I explain things until you understand — or pretend to.",
    'student': "I learn, procrastinate, and survive exams.",
    'exam': "I test your memory, not your wisdom.",
    'holiday': "I’m freedom in the calendar.",
    'dream': "I’m stories your brain writes at night.",
    'nightmare': "I scare you while you sleep.",
    'friend': "I laugh, cry, and fight with you.",
    'enemy': "I’m your rival, keeping you sharp.",
    'hero': "I save the day in movies and comics.",
    'villain': "I make the hero’s life interesting.",
    'robotics': "I mix mechanics with brains.",
    'AI': "I mimic your intelligence — sometimes too well.",
    'machine': "I replace your muscles with gears.",
    'laser': "I cut, heal, and dazzle with light.",
    'magnet': "I attract without touching.",
    'clock': "I chase time but never catch it.",
    'calendar': "I turn endless days into neat little boxes.",
    'city': "Tall buildings, traffic, endless lights.",
    'village': "Quiet, peaceful, with open skies.",
    'desire': "I burn inside you, pushing you forward.",
    'fear': "I freeze your body, speed your heart.",
    'courage': "I face fear and still move forward.",
    'hope': "I shine even in darkness.",
    'love': "I make people do crazy things.",
    'anger': "I burn hotter than fire.",
    'smile': "I’m the curve that fixes everything.",
    'laughter': "I’m contagious, spreading happiness.",
    'sleep': "I recharge you every night.",
    'hunger': "I roar inside your belly.",
    'coffee': "I wake you better than alarms.",
    'tea': "I calm nerves in a cup.",
    'chocolate': "I melt hearts and mouths alike.",
    'pizza': "Cheesy, round, loved everywhere.",
    'burger': "I’m stacked, messy, but worth it.",
    'fries': "Golden, crispy, addictive sticks.",
    'icecream': "Cold, sweet, everyone’s guilty pleasure.",
    'sun': "I shine, burn, and give life.",
    'moon': "I glow softly, borrowing light.",
    'star': "I sparkle far away in the dark.",
    'rain': "I fall, I pour, I refresh.",
    'snow': "I’m cold, white, and fun to play with.",
    'wind': "Invisible but felt everywhere.",
    'storm': "I rumble and flash with fury.",
}

import turtle
import random

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

MATH_SYMBOLS = ["π", "√", "∞", "∑", "∫", "∆", "θ", "≈", "≠", "±"]

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

def start_game():
    global chosen_word, chosen_word_list, word_to_guess, l, parts, game_over, used_letters
    hint_writer.clear(); word_writer.clear(); status_writer.clear()
    result_writer.clear(); restart_writer.clear()
    title_writer.clear(); subtitle_writer.clear(); deco_writer.clear()

    game_over = False
    used_letters = set()
    draw_decorations()
    drawer.draw_gallows()

    display_text(title_writer, "Hangman.py", 0, 320, 44, "darkblue")
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
