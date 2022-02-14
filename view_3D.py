from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout
from pyvistaqt import QtInteractor

class View3D(QWidget):
    """ Обёртка для QtInteractor"""
    def __init__(self):
        super(View3D, self).__init__()
        self.frame = QFrame()
        layout = QVBoxLayout()
        self.plotter = QtInteractor(self.frame)
        layout.addWidget(self.plotter.interactor)
        self.frame.setLayout(layout)
        self.setLayout(layout)

    def clear(self):
        self.plotter.clear()

    def addItem(self, data, *args, **kwargs):
        self.plotter.add_mesh(data, *args, **kwargs)