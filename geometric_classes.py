from PySide6.QtWidgets import (QLabel, QLineEdit, QGridLayout, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem,
                               QGraphicsPolygonItem)
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtCore import QPointF
import pyvista as pv
from math import sqrt, pow, pi
import abc

VALIDATOR = QDoubleValidator(0, 200, 2)
VALIDATOR.setNotation(QDoubleValidator.StandardNotation)


class Shape:
    """Создание прототипа фигуры"""
    title = "Фигура"

    def __init__(self, scene):
        """Создание виджета для отрисовки фигур"""
        self.scene = scene

    def get_area(self):
        """Получение площади фигуры"""
        pass

    def validate(self):
        """Проверка на соответствие свойствам фигуры"""
        pass

    @abc.abstractmethod
    def calculate(self):
        """Расчёт характеристик фигуры"""
        return {"area": self.get_area()}

    @abc.abstractmethod
    def draw(self):
        """Отрисовка фигуры"""
        pass

    @abc.abstractmethod
    def get_params_layout(self):
        """Расположение параметров"""
        pass


class Shape2D(Shape):
    """Прототип плоской фигуры"""
    title = "Плоская фигура"

    @classmethod
    def get_perimeter(cls):
        """Получение периметра фигуры"""
        pass

    def calculate(self) -> object:
        """Расчёт характеристик фигуры"""
        result = super().calculate()
        result.update({"perimeter": self.get_perimeter()})
        return result

    def validate(self):
        "Проверка на соответствие свойствам фигуры"
        pass

    def draw(self):
        """Отрисовка фигуры"""
        pass

    def get_params_layout(self):
        """Расположение параметров"""
        pass


class Shape3D(Shape):
    """Прототип объёмной фигуры"""
    title = "Объёмная фигура"

    @classmethod
    def get_volume(cls):
        """Получение объёма фигуры"""
        pass

    def calculate(self):
        """Расчёт характеристик фигуры"""
        result = super().calculate()
        result.update({"volume": self.get_volume()})
        return result

    def validate(self):
        "Проверка на соответствие свойствам фигуры"
        pass

    def draw(self):
        """Отрисовка фигуры"""
        pass

    def get_params_layout(self):
        """Расположение параметров"""
        pass


class Rectangle(Shape2D):

    title = "Прямоугольник"

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0
        self.b = 0

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

    def get_diagonal(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def validate(self):
        if self.a == 0 or self.b == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        if self.b_edit.text() != "":
            self.set_b(float(self.b_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        result.update({'diagonal': self.get_diagonal()})
        return result

    def draw(self):
        self.scene.clear()
        rect_item = QGraphicsRectItem(0, 0, self.a, self.b)
        rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(rect_item)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        b_label = QLabel("b =")
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("0")
        self.b_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(b_label, 1, 0)
        grid_layout.addWidget(self.b_edit, 1, 1)

        return grid_layout


class Square(Shape2D):

    title = "Квадрат"

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0

    def set_a(self, a):
        self.a = a

    def get_perimeter(self):
        return 4 * self.a

    def get_area(self):
        return pow(self.a, 2)

    def get_diagonal(self):
        return self.a * sqrt(2)

    def validate(self):
        if self.a == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        result.update({'diagonal': self.get_diagonal()})
        return result

    def draw(self):
        self.scene.clear()
        rect_item = QGraphicsRectItem(0, 0, self.a, self.a)
        rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(rect_item)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        return grid_layout


class Circle(Shape2D):

    title = "Круг"

    def __init__(self, scene):
        super().__init__(scene)
        self.r = 0

    def set_r(self, r):
        self.r = r

    def get_diameter(self):
        return self.r * 2

    def get_perimeter(self):
        return 2 * pi * self.r

    def get_area(self):
        return pi * pow(self.r, 2)

    def validate(self):
        if self.r == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.r_edit.text() != "":
            self.set_r(float(self.r_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        result.update({'diameter': self.get_diameter()})
        return result

    def draw(self):
        self.scene.clear()
        circle_item = QGraphicsEllipseItem(0, 0, 2 * self.r, 2 * self.r)
        circle_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(circle_item)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        r_label = QLabel("r =")
        self.r_edit = QLineEdit()
        self.r_edit.setPlaceholderText("0")

        self.r_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(r_label, 0, 0)
        grid_layout.addWidget(self.r_edit, 0, 1)

        return grid_layout


class Cube(Shape3D):

    title = "Куб"

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0

    def set_a(self, a):
        self.a = a

    def get_volume(self):
        return pow(self.a, 3)

    def get_area(self):
        return 6 * pow(self.a, 2)

    def get_diagonal(self):
        return self.a * sqrt(3)

    def validate(self):
        if self.a == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        result.update({'diagonal': self.get_diagonal()})
        return result

    def draw(self):
        self.scene.clear()
        cube = pv.Cube(x_length=self.a, y_length=self.a, z_length=self.a)
        self.scene.addItem(cube, color="green", show_edges=True)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        return grid_layout


class Sphere(Shape3D):

    title = "Сфера"

    def __init__(self, scene):
        super().__init__(scene)
        self.r = 0

    def set_r(self, r):
        self.r = r

    def get_volume(self):
        return 4 * pi * pow(self.r, 3) / 3

    def get_area(self):
        return 4 * pi * pow(self.r, 2)

    def validate(self):
        if self.r == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.r_edit.text() != "":
            self.set_r(float(self.r_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        return result

    def draw(self):
        self.scene.clear()
        sphere = pv.Sphere(radius=self.r)
        self.scene.addItem(sphere, color="green", show_edges=True)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        r_label = QLabel("r =")
        self.r_edit = QLineEdit()
        self.r_edit.setPlaceholderText("0")
        self.r_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(r_label, 0, 0)
        grid_layout.addWidget(self.r_edit, 0, 1)

        return grid_layout


class Rhombus(Shape2D):

    title = 'Ромб'

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0
        self.h = 0

    def set_a(self, a):
        self.a = a

    def set_h(self, h):
        self.h = h

    def get_area(self):
        return self.a * self.h

    def get_perimeter(self):
        return self.a * 4

    def validate(self):
        if self.a == 0 or self.h == 0:
            raise ValueError("Параметры не могут быть 0")
        if self.h >= self.a:
            raise ValueError("Высота должна быть меньше стороны")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        if self.h_edit.text() != "":
            self.set_h(float(self.h_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        return result

    def draw(self):
        self.scene.clear()
        x = sqrt(pow(self.a, 2) - pow(self.h, 2))
        points = [QPointF(0, 0), QPointF(x, self.h), QPointF(self.a + x, self.h), QPointF(self.a, 0), QPointF(0, 0)]
        rhombus_item = QGraphicsPolygonItem(points)
        rhombus_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(rhombus_item)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        h_label = QLabel("h =")
        self.h_edit = QLineEdit()
        self.h_edit.setPlaceholderText("0")
        self.h_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(h_label, 1, 0)
        grid_layout.addWidget(self.h_edit, 1, 1)

        return grid_layout


class Cylinder(Shape3D):

    title = "Цилиндр"

    def __init__(self, scene):
        super().__init__(scene)
        self.r = 0
        self.h = 0

    def set_r(self, r):
        self.r = r

    def set_h(self, h):
        self.h = h

    def get_volume(self):
        return pi * pow(self.r, 2) * self.h

    def get_area(self):
        return 2 * pi * pow(self.r, 2) + 2 * pi * self.r * self.h

    def validate(self):
        if self.r == 0 or self.h == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.r_edit.text() != "":
            self.set_r(float(self.r_edit.text()))
        if self.h_edit.text() != "":
            self.set_h(float(self.h_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        return result

    def draw(self):
        self.scene.clear()
        cylinder = pv.Cylinder(radius=self.r, height=self.h)
        self.scene.addItem(cylinder, color="green", show_edges=True)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        r_label = QLabel("r =")
        self.r_edit = QLineEdit()
        self.r_edit.setPlaceholderText("0")
        self.r_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(r_label, 0, 0)
        grid_layout.addWidget(self.r_edit, 0, 1)

        h_label = QLabel("h =")
        self.h_edit = QLineEdit()
        self.h_edit.setPlaceholderText("0")
        self.h_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(h_label, 1, 0)
        grid_layout.addWidget(self.h_edit, 1, 1)

        return grid_layout


class Cone(Shape3D):

    title = "Конус"

    def __init__(self, scene):
        super().__init__(scene)
        self.r = 0
        self.h = 0

    def set_r(self, r):
        self.r = r

    def set_h(self, h):
        self.h = h

    def get_volume(self):
        c_l = sqrt(self.r ** 2 + self.h ** 2)
        return pi * pow(self.r, 2) + pi * self.r * c_l

    def get_area(self):
        return pi * pow(self.r, 2) * self.h / 3

    def validate(self):
        if self.r == 0 or self.h == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.r_edit.text() != "":
            self.set_r(float(self.r_edit.text()))
        if self.h_edit.text() != "":
            self.set_h(float(self.h_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        return result

    def draw(self):
        self.scene.clear()
        cone = pv.Cone(radius=self.r, height=self.h, resolution=20)
        self.scene.addItem(cone, color="green", show_edges=True)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        r_label = QLabel("r =")
        self.r_edit = QLineEdit()
        self.r_edit.setPlaceholderText("0")
        self.r_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(r_label, 0, 0)
        grid_layout.addWidget(self.r_edit, 0, 1)

        h_label = QLabel("h =")
        self.h_edit = QLineEdit()
        self.h_edit.setPlaceholderText("0")
        self.h_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(h_label, 1, 0)
        grid_layout.addWidget(self.h_edit, 1, 1)

        return grid_layout


class Triangle(Shape2D):

    title = "Треугольник"

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0
        self.b = 0
        self.c = 0

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_perimeter() / 2
        height = 2 * sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) / self.b
        return height * self.b / 2

    def get_median(self):
        return 1 / 2 * sqrt(2 * self.a ** 2 + 2 * self.b ** 2 - self.c ** 2)

    def validate(self):
        if self.a == 0 or self.b == 0 or self.c == 0:
            raise ValueError("Параметры не могут быть 0")
        if self.a + self.b <= self.c \
                or self.a + self.c <= self.b \
                or self.b + self.c <= self.a:
            raise ValueError("Данные не соответствуют свойствам треугольника")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        if self.b_edit.text() != "":
            self.set_b(float(self.b_edit.text()))
        if self.c_edit.text() != "":
            self.set_c(float(self.c_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        result.update({'median': self.get_median()})
        return result

    def draw(self):
        self.scene.clear()
        points = [QPointF(0, 0), QPointF(self.a, 0)]
        x3 = (pow(self.a, 2) + pow(self.b, 2) - pow(self.c, 2)) / (2 * self.a)
        y3 = -sqrt(pow(self.b, 2) - pow(x3, 2))
        points.append(QPointF(x3, y3))
        points.append(QPointF(0, 0))
        triangle_item = QGraphicsPolygonItem(points)
        triangle_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.scene.addItem(triangle_item)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        b_label = QLabel("b =")
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("0")
        self.b_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(b_label, 1, 0)
        grid_layout.addWidget(self.b_edit, 1, 1)

        c_label = QLabel("c =")
        self.c_edit = QLineEdit()
        self.c_edit.setPlaceholderText("0")
        self.c_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(c_label, 2, 0)
        grid_layout.addWidget(self.c_edit, 2, 1)

        return grid_layout


class Parallelepiped(Shape3D):

    title = "Параллелепипед"

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0
        self.b = 0
        self.c = 0

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_volume(self):
        return self.a * self.b * self.c

    def get_area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def get_diagonal(self):
        return sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2)

    def validate(self):
        if self.a == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        if self.b_edit.text() != "":
            self.set_b(float(self.b_edit.text()))
        if self.c_edit.text() != "":
            self.set_c(float(self.c_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        result.update({'diagonal': self.get_diagonal()})
        return result

    def draw(self):
        self.scene.clear()
        parallelepiped = pv.Cube(x_length=self.a, y_length=self.b, z_length=self.c)
        self.scene.addItem(parallelepiped, color="green", show_edges=True)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        b_label = QLabel("b =")
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("0")
        self.b_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(b_label, 1, 0)
        grid_layout.addWidget(self.b_edit, 1, 1)

        c_label = QLabel("c =")
        self.c_edit = QLineEdit()
        self.c_edit.setPlaceholderText("0")
        self.c_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(c_label, 2, 0)
        grid_layout.addWidget(self.c_edit, 2, 1)

        return grid_layout


class Pyramid(Shape3D):

    title = "Пирамида"

    def __init__(self, scene):
        super().__init__(scene)
        self.a = 0
        self.n = 0
        self.h = 0

    def set_a(self, a):
        self.a = a

    def set_h(self, h):
        self.h = h

    def set_n(self, n):
        self.n = n

    def get_volume(self):
        x = sqrt(pow(self.a, 2) - pow(self.a / 2, 2))
        p = self.a * self.n
        S = p * x / 2
        return S * self.h / 3

    def get_area(self):
        x = sqrt(pow(self.a, 2) - pow(self.a / 2, 2))
        p = self.a * self.n
        S1 = p * x / 2
        x2 = pow(self.a, 2) + pow(self.h, 2)
        h = sqrt(x2 - pow(self.a / 2, 2))
        S2 = self.a * h / 2
        return S1 + self.n * S2

    def validate(self):
        if self.a == 0 or self.h == 0 or self.n == 0:
            raise ValueError("Параметры не могут быть 0")

    def calculate(self):
        if self.a_edit.text() != "":
            self.set_a(float(self.a_edit.text()))
        if self.h_edit.text() != "":
            self.set_h(float(self.h_edit.text()))
        if self.n_edit.text() != "":
            self.set_n(int(self.n_edit.text()))
        self.validate()
        self.draw()
        result = super().calculate()
        return result

    def draw(self):
        self.scene.clear()
        cone = pv.Cone(radius=self.a, height=self.h, resolution=self.n)
        self.scene.addItem(cone, color="green", show_edges=True)

    def get_params_layout(self):
        grid_layout = QGridLayout()

        a_label = QLabel("a =")
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("0")
        self.a_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(a_label, 0, 0)
        grid_layout.addWidget(self.a_edit, 0, 1)

        h_label = QLabel("h =")
        self.h_edit = QLineEdit()
        self.h_edit.setPlaceholderText("0")
        self.h_edit.setValidator(VALIDATOR)
        grid_layout.addWidget(h_label, 1, 0)
        grid_layout.addWidget(self.h_edit, 1, 1)

        n_label = QLabel("n =")
        self.n_edit = QLineEdit()
        self.n_edit.setPlaceholderText("0")
        self.n_edit.setValidator(QIntValidator(3, 10))
        grid_layout.addWidget(n_label, 2, 0)
        grid_layout.addWidget(self.n_edit, 2, 1)

        return grid_layout
