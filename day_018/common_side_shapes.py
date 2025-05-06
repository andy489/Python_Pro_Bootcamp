from turtle import Turtle, Screen, colormode
from random import randint

# import matplotlib.colors as mcolors

FULL_ROTATION = 360
MAX_ANGLED_SHAPE = 11
SIDE_LENGTH = 100

# def get_rand_color():
#     color = random.choice(list(mcolors.CSS4_COLORS.keys()))
#     return color

def get_rand_color():
    """
    Returns a 3-tuple of random numbers in the range 0 - 255
    eg : (89, 103, 108)
    """
    return tuple(randint(0, 255) for _ in range(3))


def draw(n, angle):
    """Draws and n sided shape. Before each draw a random pencolor color is selected."""
    # *iterable_variable means "treat the elements of this iterable as positional arguments to this function call"
    # **dictionary means "treat the key-value pairs in the dictionary as additional named arguments
    # to this function call"
    t.pencolor(*get_rand_color())

    for _ in range(n):
        t.forward(SIDE_LENGTH)
        t.right(angle)


t = Turtle()
t.shape("turtle")
t.color("coral")
colormode(255)
# t.speed("fast")

t.backward(50)

for i in range(3, MAX_ANGLED_SHAPE):
    draw(i, FULL_ROTATION / i)

s = Screen()
s.exitonclick()
