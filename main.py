from PySide6.QtWidgets import (QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget,
                               QSpacerItem, QSizePolicy, QPushButton, QGraphicsView, QGraphicsScene, QMessageBox,
                               QStackedWidget)
import sys

from view_3D import View3D
from geometric_classes import (Rectangle, Square, Circle, Cube, Sphere, Triangle, Rhombus, Cylinder, Cone,
                               Parallelepiped, Pyramid)


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.figure = None
        self.setWindowTitle("Геометрический Калькулятор")
        self.init_window()

    def init_window(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        self.figure_selector = QComboBox()
        self.figure_selector.addItems(["", "Triangle", "Rectangle", "Square", "Circle", "Cube", "Sphere", "Rhombus",
                                       "Cylinder", "Cone", "Parallelepiped", "Pyramid"])
        self.figure_selector.setMinimumWidth(200)
        self.figure_selector.currentIndexChanged.connect(self.figure_selected)
        v_layout.addWidget(self.figure_selector)
        self.params_widget = QWidget()
        v_layout.addWidget(self.params_widget)
        self.results_label = QLabel()
        v_layout.addWidget(self.results_label)
        v_layout.addSpacerItem(QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        h_layout.addLayout(v_layout)
        self.scene2D = QGraphicsScene()
        self.view2D = QGraphicsView(self.scene2D)
        self.view2D.setMinimumSize(600, 400)
        self.view3D = View3D()
        self.view3D.setMinimumSize(600, 400)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.view2D)
        self.stacked_widget.addWidget(self.view3D)
        h_layout.addWidget(self.stacked_widget)

        widget = QWidget()
        widget.setLayout(h_layout)
        self.setCentralWidget(widget)

    def figure_selected(self, index):
        QWidget().setLayout(self.params_widget.layout())
        v_layout = QVBoxLayout()
        self.results_label.setText("")
        self.scene2D.clear()
        self.view3D.clear()

        figure_name = self.figure_selector.currentText()
        if figure_name == "Triangle":
            self.stacked_widget.setCurrentIndex(0)
            self.figure = Triangle(self.scene2D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Rhombus":
            self.stacked_widget.setCurrentIndex(0)
            self.figure = Rhombus(self.scene2D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Rectangle":
            self.stacked_widget.setCurrentIndex(0)
            self.figure = Rectangle(self.scene2D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Square":
            self.stacked_widget.setCurrentIndex(0)
            self.figure = Square(self.scene2D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Circle":
            self.stacked_widget.setCurrentIndex(0)
            self.figure = Circle(self.scene2D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Cube":
            self.stacked_widget.setCurrentIndex(1)
            self.figure = Cube(self.view3D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Parallelepiped":
            self.stacked_widget.setCurrentIndex(1)
            self.figure = Parallelepiped(self.view3D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Sphere":
            self.stacked_widget.setCurrentIndex(1)
            self.figure = Sphere(self.view3D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Cylinder":
            self.stacked_widget.setCurrentIndex(1)
            self.figure = Cylinder(self.view3D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Pyramid":
            self.stacked_widget.setCurrentIndex(1)
            self.figure = Pyramid(self.view3D)
            v_layout.addLayout(self.figure.get_params_layout())
        elif figure_name == "Cone":
            self.stacked_widget.setCurrentIndex(1)
            self.figure = Cone(self.view3D)
            v_layout.addLayout(self.figure.get_params_layout())
        else:
            self.figure = None

        if len(figure_name):
            calc_btn = QPushButton("Calculate")
            calc_btn.clicked.connect(self.calculate)
            v_layout.addWidget(calc_btn)

        self.params_widget.setLayout(v_layout)

    def calculate(self):
        self.results_label.setText("")
        try:
            result = self.figure.calculate()
            ans = ""
            for k, v in result.items():
                ans += f"{k} = {v:.2f}\n"

            self.results_label.setText(ans)
        except ValueError as e:
            QMessageBox.critical(self, "", str(e.args[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    app.exec()
