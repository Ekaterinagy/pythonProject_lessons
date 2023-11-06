# Введите ваше решение ниже
import argparse
import logging

parser = argparse.ArgumentParser(
    prog='Rectangle',
    description='Выполняет операции над прямоугольниками',
    epilog='спасибо')

parser.add_argument('-a', '--width', help="сторона a", type=int)
parser.add_argument('-b', '--height', help="сторна b", type=int)
parser.add_argument('-c', '--console', help="вывод в консоль", action='store_true')

my_namespace = parser.parse_args()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename="rectangle.log",
                    encoding='utf-8',
                    level=logging.DEBUG)


class Rectangle:
    logger = logging.getLogger(__name__)

    def __init__(self, width, height=None):
        logger.info("rectangle init start")
        self.width = width
        if width < 0:
            raise Exception('NegativeValueError')
        if height is None:
            self.height = width
        else:
            if height < 0:
                raise Exception('NegativeValueError')
            self.height = height
        logger.info("rectangle init end")

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):

        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):

        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):

        return self.area() < other.area()

    def __eq__(self, other):

        return self.area() == other.area()

    def __le__(self, other):

        return self.area() <= other.area()

    def __str__(self):

        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):

        return f"Rectangle({self.width}, {self.height})"


def perform_rectangle():
    logger.info("perform_rectangle with args: %s, %s Start", my_namespace.width, my_namespace.height)
    try:
        rectangle = Rectangle(my_namespace.width, my_namespace.height)
        perimeter = rectangle.perimeter()
        area = rectangle.area()
        logger.debug("создан прямоугольник: %s", rectangle)
        logger.debug("периметр: %s, площадь: %s", perimeter, area)
        if my_namespace.console:
            print(f'Вывод: \n\tПрямоугольник: {rectangle} \n\tпериметер: {perimeter} \n\tплощадь: {area}')
    except Exception as ex:
        logger.error('Error perform_rectangle: %s', ex)
        raise ex
    logger.info("perform_rectangles End")


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    perform_rectangle()
