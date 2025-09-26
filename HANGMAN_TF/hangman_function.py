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
    'rocket': "I leave Earth in fire and thunder.",
    'guitar': "Six strings, endless emotions.",
    'friend': "I laugh, cry, and fight with you.",
    'volcano': "I explode with fire and lava when angry.",
    'galaxy': "I hold billions of stars — and you're in one.",
    'basketball': "I bounce and swish through hoops.",
    'pyramid': "I point to the sky with a polygon base.",
    'algebra': "I speak with letters, but I always mean numbers. Who am I?",
    'permutation': "I care about order — who sits where matters.",
    'bacteria': "I can help you digest or make you sick.",
    'computer': "Brilliant assistant, obedient mind.",
    'ratio': "I compare two numbers simply.",
    'tower': "I reach for the sky yet have no wings. People build me to watch over things. What am I?",
    'holiday': "I'm freedom in the calendar.",
    'storm': "I rumble and flash with fury.",
    'rain': "I fall, I pour, I refresh.",
    'student': "I learn, procrastinate, and survive exams.",
    'identity': "I never change, I stay the same in every case.",
    'polynomial': "I'm powers of x stacked together.",
    'icecream': "Cold, sweet, everyone's guilty pleasure.",
    'robotics': "I give metal bodies motion and thought.",
    'heart': "I pump life nonstop until you stop.",
    'engine': "I roar with fuel and make wheels turn.",
    'vector': "I march with size and direction.",
    'fibonacci': "I grow remembering my last two steps.",
    'internet': "I connect the world in a click.",
    'line': "I stretch forever, straight and unbending.",
    'love': "I bind hearts stronger than chains. I can bring joy or break you apart.",
    'machine': "I turn cogs and gears to do your work.",
    'algebra': "I speak with letters, but I always mean numbers. Who am I?",
    'sequence': "Numbers marching in order.",
    'coffee': "I wake you better than alarms.",
    'moon': "I glow softly, borrowing light.",
    'hope': "I am the light at the end of every tunnel.",
    'statistics': "I make numbers tell a story.",
    'python': "I'm a snake, but also a language.",
    'fear': "I freeze your steps but race your heart.",
    'enemy': "I'm your rival, keeping you sharp.",
    'dream': "I'm stories your brain writes at night.",
    'current': "I'm the river of electricity.",
    'denominator': "I live under the fraction line.",
    'angle': "I measure the turn when two lines decide to meet.",
    'DNA': "I carry the code that makes you, you.",
    'range': "I measure the gap between high and low.",
    'sine': "Opposite side divided by hypotenuse — that's me.",
    'integral': "I collect tiny parts into a whole curve.",
    'exam': "I test your memory, not your wisdom.",
    'galaxy': "I hold billions of stars — and you're in one.",
    'variable': "The shape-shifter in every formula.",
    'plane': "Flat and endless, like invisible paper.",
    'virus': "I invade, multiply, and cause chaos.",
    'coffee': "I wake you better than alarms.",
    'cosine': "Adjacent over hypotenuse — that's my claim to fame.",
    'earthquake': "I arrive without warning, rumbling deep below. I can topple towers but cannot be seen. What am I?",
    'music': "I make your soul dance.",
    'tangent': "I touch a curve at exactly one spot.",
    'desert2': "I burn by day, freeze by night.",
    'cylinder': "I look like a soda can — round top, round bottom.",
    'function': "Give me input, I'll always return output.",
    'area': "I tell you how much paint you need to cover the floor.",
    'courage': "I face fear and still move forward.",
    'magnet': "I attract without touching.",
    'radius': "From circle's center to its edge, that's me.",
    'teacher': "I explain things until you understand — or pretend to.",
    'piano': "Black and white soldiers march, and I make them sing.",
    'island': "Water surrounds me — I'm all alone.",
    'graph': "Axes, points, lines — I reveal patterns hidden in numbers.",
    'inequality': "I'm not equal — greater or lesser, that's me.",
    'pizza': "Cheesy, round, loved everywhere.",
    'robot': "I follow commands — sometimes smarter than humans.",
    'meteor': "I wander space, rocky and wild.",
    'neutron': "I'm neutral but vital inside atoms.",
    'prime': "Indivisible except by 1 and me.",
    'trapezium': "Two sides parallel, the others free.",
    'storm': "I rumble and flash with fury.",
    'equation': "Two sides of me must always agree.",
    'divisor': "I divide numbers cleanly, leaving nothing behind.",
    'hunger': "I roar inside your belly.",
    'chess': "I'm war without bloodshed — kings and queens fight here.",
    'burger': "I'm stacked, messy, but worth it.",
    'river': "I flow endlessly, carving the land.",
    'blackhole': "I eat everything, even light.",
    'fire': "I burn bright, destroy, but also warm.",
    'exam': "I test your memory, not your wisdom.",
    'snow': "I'm cold, white, and fun to play with.",
    'bridge': "I connect lands, standing over rivers.",
    'robotics': "I give metal bodies motion and thought.",
    'circle': "I'm round and endless, with no beginning or end.",
    'star': "I sparkle far away in the dark.",
    'desert': "Hot, dry, endless sand playground.",
    'sun': "I shine, burn, and give life.",
    'mountain': "I rise from the earth, standing still yet touching the clouds.",
    'polygon': "From three to ten (or more!), I'm the many-sided crew.",
    'calculus': "I'm the math of change, both instant and vast.",
    'oxygen': "Breathe me or you won't last a minute.",
    'laser': "I cut, heal, and dazzle with light.",
    'octagon': "I wear eight sides like armor.",
    'school': "I teach, punish, and prepare you.",
    'symmetry': "Flip me, turn me — I stay the same.",
    'clock': "I have hands but never touch, I chase time yet never catch. What am I?",
    'football': "I roll, I bounce, I make crowds scream.",
    'ocean': "I'm salty, deep, and cover most of Earth.",
    'villain': "I live in shadows, making the hero's path harder.",
    'fries': "Golden, crispy, addictive sticks.",
    'rainbow': "I appear when light and raindrops dance.",
    'volume': "Fill me up, pour me out — I keep track of the space about.",
    'median': "I'm the middle child of data.",
    'proof': "I convince the world with logic.",
    'camera': "I freeze moments in frames.",
    'angle': "I measure the turn when two lines decide to meet.",
    'algorithm': "I'm a set of steps, precise and neat, follow me through and problems retreat.",
    'train': "I run on tracks, carrying stories.",
    'sleep': "I take you to dreams when the day is done.",
    'java': "I'm coffee in a cup, but also code.",
    'derivative': "I'm the slope's secret twin — instant change.",
    'coefficient': "I sit in front of a variable, powerful yet quiet.",
    'tower': "I reach for the sky yet have no wings. People build me to watch over things. What am I?",
    'dream': "I'm stories your brain writes at night.",
    'multiple': "I'm born when numbers repeat themselves.",
    'hero': "I save the day in movies and comics.",
    'smile': "I'm the curve that fixes everything.",
    'tornado': "I spin faster than a dancer, destroying paths.",
    'square': "Equal sides, right corners — perfection.",
    'identity': "I never change, I stay the same in every case.",
    'cell': "I'm tiny but alive — life's building block.",
    'enemy': "I'm your rival, keeping you sharp.",
    'normal': "I stand tall — perpendicular and fair.",
    'perimeter': "Walk around me, and you measure me.",
    'set': "I gather unique objects into one family.",
    'rhombus': "Equal sides, tilted square.",
    'moon': "I glow softly, borrowing light.",
    'integral': "I collect tiny parts into a whole curve.",
    'quotient': "I'm what you get when you divide.",
    'exam': "I test your memory, not your wisdom.",
    'wind': "Invisible but felt everywhere.",
    'logarithm': "I tell you the exponent that got you here.",
    'desire': "I burn inside you, pushing you forward.",
    'binomial': "I come in twos, joined by a plus or minus.",
    'village': "I rest in quiet fields, where open skies meet peaceful lives-A place",
    'infinity': "I never end, never stop — forever.",
    'range': "I measure the gap between high and low.",
    'chocolate': "I melt hearts and mouths alike.",
    'sphere': "I'm a perfect 3D ball.",
    'nightmare': "I scare you while you sleep.",
    'laughter': "I'm contagious, spreading happiness.",
    'mean': "Add them all up, then share them equally — that's me.",
    'congruence': "When sides and angles all agree, two figures become copies of me.",
    'fibonacci': "I grow remembering my last two steps.",
    'trapezium': "Two sides parallel, the others free.",
    'product': "Two numbers meet, and I'm the result of their party.",
    'island': "Water surrounds me — I'm all alone.",
    'forest': "I'm green, dense, and full of secrets.",
    'sun': "I shine, burn, and give life.",
    'dinosaur': "I stomped, I roared, long before you were born.",
    'star': "I sparkle far away in the dark.",
    'phone': "I ring, buzz, and keep you addicted.",
    'probability': "I whisper the odds of what could happen.",
    'mode': "I love popularity — I appear the most.",
    'electron': "I'm tiny, negative, always zipping around.",
    'parallel': "Like best friends walking forever, but never hugging.",
    'gradient': "Change in y over change in x — that's my secret formula.",
    'volume': "Fill me up, pour me out — I keep track of the space about.",
    'exponent': "I sit high and make numbers explode.",
    'tsunami': "I'm the ocean's sprint, a wave that doesn't tire.",
    'pyramid': "I point to the sky with a polygon base.",
    'calculus': "I'm the math of change, both instant and vast.",
    'inverse': "I undo what's been done — the great reverser.",
    'galaxy': "I hold billions of stars — and you're in one.",
    'statistics': "I make numbers tell a story.",
    'trapezium': "Two sides parallel, the others free.",
    'axiom': "I'm the rule everyone accepts without argument.",
    'rainbow': "I appear when light and raindrops dance.",
    'fraction': "I'm a slice of the whole pie.",
    'brain': "I'm squishy but smarter than any computer.",
    'mountain': "I rise from the earth, standing still yet touching the clouds.",
    'coffee': "I wake you better than alarms.",
    'city': "A place with tall buildings, traffic, endless lights.",
    'pythagoras': "The square of the hypotenuse equals the sum of the other two.",
    'galaxy': "I hold billions of stars — and you're in one.",
    'river': "I flow endlessly, carving the land.",
    'hero': "I save the day in movies and comics."
}
