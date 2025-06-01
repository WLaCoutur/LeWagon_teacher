# pylint: disable=too-few-public-methods missing-module-docstring
# $CHALLENGIFY_BEGIN
class Shape:
    """
    Base class for different shapes.

    Attributes:
        color (str): The color of the shape.
        name (str): The name of the shape.
    """
    def __init__(self, color, name):
        """
        Initialize a new Shape instance.

        Args:
            color (str): The color of the shape.
            name (str): The name of the shape.
        """
        self.color = color
        self.name = name

    def say_name(self):
        """
        Returns the name of the shape.

        Returns:
            str: A message stating the name of the shape.
        """
        return f"My name is {self.name}."


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, color, name, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            color (str): The color of the rectangle.
            name (str): The name of the rectangle.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """
        Returns the name and type of the shape.

        Returns:
            str: A message stating the name of the shape and that it is a rectangle.
        """
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, color, name, radius):
        """
        Initialize a new Circle instance.

        Args:
            color (str): The color of the circle.
            name (str): The name of the circle.
            radius (float): The radius of the circle.
        """
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """
        Returns the name and type of the shape.

        Returns:
            str: A message stating the name of the shape and that it is a circle.
        """
        return f"My name is {self.name} and I am a circle."

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * 3.14 * self.radius

# $CHALLENGIFY_END
