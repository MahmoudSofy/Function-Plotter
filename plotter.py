#Part 0: Importing dependencies.
from PySide2.QtWidgets import * 
from PySide2.QtUiTools import QUiLoader 
from PySide2.QtCore import QFile
from matplotlib.backends.backend_qt5agg import (FigureCanvas ,NavigationToolbar2QT as  NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np

#Part 1: setting up the input function conditioner.
#The next dictionary includes the supported functions, more functions can be appended easily.
#Note that this dictionary supports sinh, archsinh, cosh, .. etc.
def prepare(fx):
    supported_functions = {"^":"**", "sin":"np.sin", "cos":"np.cos", "tan":"np.tan",
                           "arcnp.sin":"np.arcsin", "arcnp.cos":"np.arccos",
                           "arcnp.tan":"np.arctan", "e**":"np.exp", "log":"np.log10", "ln":"np.log"}
    for func in supported_functions.keys():
        fx = fx.replace(func, supported_functions[func])
    return fx


#Part 2: Matplotlib Widget.
class plot_area(QWidget):
    def  __init__ (self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget(self.canvas) 
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))
        self.canvas.axes = self.canvas.figure.add_subplot( 111 ) 
        self.setLayout(vertical_layout)

#Part 3: Main Widget.
class  MainWidget(QWidget):
    def  __init__ (self):
        QWidget.__init__(self)
        designer_file = QFile("gui.ui") 
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader() 
        loader.registerCustomWidget(plot_area) 
        self.ui = loader.load(designer_file, self)
        designer_file.close()
        self.setWindowTitle("Function Plotter")
        self.ui.plot.clicked.connect(self.update)
        
    #Plot update.
    def  update(self):
        f_x = self.ui.fx.text()
        f_x = prepare(f_x)
        #Check if the append option is checked.
        if (self.ui.append.isChecked()): 
            pass
        else:
            self.ui.plot_area.canvas.axes.clear()

        try:
            x_min = float(self.ui.xmin.text())
            x_max = float(self.ui.xmax.text())
            pts = int(self.ui.points.text())
        except:
            QMessageBox.warning(self, "Error", " Check your limits and number of points! \n Make sure you enter only numbers.") 
        
        x = np.linspace(x_min, x_max, pts)
        try:
            self.ui.plot_area.canvas.axes.plot(x, eval(f_x))
        except:
            QMessageBox.warning(self, "Error", " Check your function! \n Make sure you enter only functions in x with parentheses for any argument.") 
        self.ui.plot_area.canvas.draw()

#Part 4: Execution.
#If statement is to suppress GUI execution during testing.
if __name__ == '__main__':
    app = QApplication ([]) 
    window = MainWidget () 
    window.show() 
    app.exec_()
