"""Scene description."""

__author__ = 730224294


from turtle import Turtle, colormode, done
colormode(255)


def main() -> None: 
    """The entrypoint of my scene."""
    scene: Turtle = Turtle()
    draw_grass(scene, -370, -100, 750)
    draw_mountains(scene, 100, 0, -100)
    draw_mountains(scene, 200, 100, -100)
    draw_mountains(scene, 150, -300, -100)
    draw_sun(scene, -200, 140)
    done()


def draw_grass(first_turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draw the grass of the scene."""
    first_turtle.color("green")
    first_turtle.penup()
    first_turtle.goto(x, y)
    first_turtle.setheading(0.0)
    first_turtle.pendown()
    i: int = 0
    while i < 4:
        first_turtle.forward(width)
        first_turtle.right(90)
        i += 1
    first_turtle.begin_fill()
    for _ in range(4):
        first_turtle.forward(width)
        first_turtle.right(90)
    first_turtle.end_fill()


def draw_mountains(second_turtle: Turtle, forward: float, x: float, y: float) -> None: 
    """Draw the mountains."""
    second_turtle.color(13, 60, 121)
    second_turtle.penup()
    second_turtle.goto(x, y)
    second_turtle.setheading(0.0)
    second_turtle.pendown()
    i: int = 0
    while i < 3: 
        second_turtle.forward(forward)
        second_turtle.left(120)
        i += 1
    second_turtle.begin_fill()
    for _ in range(3):
        second_turtle.forward(forward)
        second_turtle.left(120)
    second_turtle.end_fill()


def draw_sun(third_turtle: Turtle, x: float, y: float) -> None: 
    """Draw the sun."""
    third_turtle.color(234, 221, 23)
    third_turtle.penup()
    third_turtle.goto(x, y)
    third_turtle.setheading(0.0)
    third_turtle.pendown()
    third_turtle.circle(70)
    third_turtle.begin_fill()
    for _ in range(1):
        third_turtle.circle(70)
    third_turtle.end_fill()


if __name__ == "__main__":
    main()