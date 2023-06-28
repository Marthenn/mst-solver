import graph, parser
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.graph = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 680))
        MainWindow.setMaximumSize(QtCore.QSize(800, 680))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.header.setStyleSheet("color: white")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.headerBar = QtWidgets.QFrame(self.centralwidget)
        self.headerBar.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.headerBar.setStyleSheet("background-color: #5F9DF7;")
        self.headerBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerBar.setObjectName("headerBar")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 811, 691))
        self.background.setStyleSheet("background-color: #1746A2;")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.frame = QtWidgets.QFrame(self.background)
        self.frame.setGeometry(QtCore.QRect(30, 100, 741, 80))
        self.frame.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.fileButton = QtWidgets.QPushButton(self.frame)
        self.fileButton.setGeometry(QtCore.QRect(30, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fileButton.setFont(font)
        self.fileButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.fileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileButton.setObjectName("fileButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.background)
        self.frame_2.setGeometry(QtCore.QRect(30, 190, 521, 471))
        self.frame_2.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.canvas = FigureCanvas(plt.figure())
        self.canvas.setParent(self.frame_2)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 501, 441))
        self.canvas.figure.set_facecolor('#5F9DF7')
        self.frame_3 = QtWidgets.QFrame(self.background)
        self.frame_3.setGeometry(QtCore.QRect(560, 190, 211, 471))
        self.frame_3.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.vertex1 = QtWidgets.QSpinBox(self.frame_3)
        self.vertex1.setGeometry(QtCore.QRect(20, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.vertex1.setFont(font)
        self.vertex1.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 5px 10px;\n"
"outline: none;\n"
"")
        self.vertex1.setObjectName("vertex1")
        self.vertex2 = QtWidgets.QSpinBox(self.frame_3)
        self.vertex2.setGeometry(QtCore.QRect(20, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.vertex2.setFont(font)
        self.vertex2.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 5px 10px;\n"
"outline: none;\n"
"")
        self.vertex2.setObjectName("vertex2")
        self.weight = QtWidgets.QSpinBox(self.frame_3)
        self.weight.setGeometry(QtCore.QRect(20, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.weight.setFont(font)
        self.weight.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 5px 10px;\n"
"outline: none;\n"
"")
        self.weight.setObjectName("weight")
        self.addEdgeButton = QtWidgets.QPushButton(self.frame_3)
        self.addEdgeButton.setGeometry(QtCore.QRect(20, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addEdgeButton.setFont(font)
        self.addEdgeButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.addEdgeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addEdgeButton.setObjectName("addEdgeButton")
        self.removeEdgeButton = QtWidgets.QPushButton(self.frame_3)
        self.removeEdgeButton.setGeometry(QtCore.QRect(100, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.removeEdgeButton.setFont(font)
        self.removeEdgeButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.removeEdgeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeEdgeButton.setObjectName("removeEdgeButton")
        self.vertexNumber = QtWidgets.QSpinBox(self.frame_3)
        self.vertexNumber.setGeometry(QtCore.QRect(20, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.vertexNumber.setFont(font)
        self.vertexNumber.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 5px 10px;\n"
"outline: none;\n"
"")
        self.vertexNumber.setObjectName("vertexNumber")
        self.removeVertexButton = QtWidgets.QPushButton(self.frame_3)
        self.removeVertexButton.setGeometry(QtCore.QRect(100, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.removeVertexButton.setFont(font)
        self.removeVertexButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.removeVertexButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeVertexButton.setObjectName("removeVertexButton")
        self.addVertexNumber = QtWidgets.QPushButton(self.frame_3)
        self.addVertexNumber.setGeometry(QtCore.QRect(20, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addVertexNumber.setFont(font)
        self.addVertexNumber.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.addVertexNumber.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addVertexNumber.setObjectName("addVertexNumber")
        self.clusterButton = QtWidgets.QPushButton(self.frame_3)
        self.clusterButton.setGeometry(QtCore.QRect(20, 380, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clusterButton.setFont(font)
        self.clusterButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.clusterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clusterButton.setObjectName("clusterButton")
        self.clusterNumber = QtWidgets.QSpinBox(self.frame_3)
        self.clusterNumber.setGeometry(QtCore.QRect(20, 340, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.clusterNumber.setFont(font)
        self.clusterNumber.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 5px 10px;\n"
"outline: none;\n"
"")
        self.clusterNumber.setObjectName("clusterNumber")
        self.mstButton = QtWidgets.QPushButton(self.frame_3)
        self.mstButton.setGeometry(QtCore.QRect(20, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mstButton.setFont(font)
        self.mstButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.mstButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mstButton.setObjectName("mstButton")
        self.algoBox = QtWidgets.QComboBox(self.frame_3)
        self.algoBox.setGeometry(QtCore.QRect(20, 270, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.algoBox.setFont(font)
        self.algoBox.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 5px 10px;\n"
"outline: none;\n"
"")
        self.algoBox.addItem("Prim")
        self.algoBox.addItem("Kruskal")
        self.algoBox.setObjectName("algoBox")
        self.resetButton = QtWidgets.QPushButton(self.frame_3)
        self.resetButton.setGeometry(QtCore.QRect(20, 420, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color: #1746A2;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px 20px;\n"
"border-radius: 15px;")
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setObjectName("resetButton")
        self.background.raise_()
        self.headerBar.raise_()
        self.header.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.algoBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.fileButton.clicked.connect(self.chooseFile)
        self.mstButton.clicked.connect(self.findMST)
        self.addEdgeButton.clicked.connect(self.addEdge)
        self.removeEdgeButton.clicked.connect(self.delEdge)
        self.removeVertexButton.clicked.connect(self.delVertex)
        self.addVertexNumber.clicked.connect(self.addVertex)
        self.resetButton.clicked.connect(self.reset)
        self.clusterButton.clicked.connect(self.findCluster)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MST Finder"))
        self.header.setText(_translate("MainWindow", "MST FINDER"))
        self.fileButton.setText(_translate("MainWindow", "Choose File"))
        self.label.setText(_translate("MainWindow", "No File Selected"))
        self.addEdgeButton.setText(_translate("MainWindow", "Add"))
        self.removeEdgeButton.setText(_translate("MainWindow", "Del"))
        self.removeVertexButton.setText(_translate("MainWindow", "Del"))
        self.addVertexNumber.setText(_translate("MainWindow", "Add"))
        self.clusterButton.setText(_translate("MainWindow", "Find Cluster"))
        self.mstButton.setText(_translate("MainWindow", "Find MST"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))

    def chooseFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Choose File", "", "Text Files (*.txt)", options=options)

        if not file_name:
            return

        try:
            self.label.setText(file_name)
            matrix = parser.parse(file_name)
            self.graph = graph.Graph(matrix)
            self.draw_graph()
        except Exception as e:
            error_message = f"Error opening file: {str(e)}"
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
            self.label.setText("No File Selected")
	
    def draw_graph(self):
        self.canvas.figure.clear()

        ax = self.canvas.figure.add_subplot(111)
        ax.axis('off')

        for vertex in self.graph.vertices:
            pos = self.graph.vertices_position[vertex]
            ax.plot(pos[0], pos[1], 'o', color='orange', markersize=15)
            ax.annotate(vertex, pos, color='white', fontweight='bold')
        
        for edge in self.graph.edges:
            [v1, v2, weight] = edge
            pos1 = self.graph.vertices_position[v1]
            pos2 = self.graph.vertices_position[v2]
            ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], color='white')
            ax.text((pos1[0] + pos2[0])/2, (pos1[1] + pos2[1])/2, str(weight), color = 'black', fontweight='bold')
        
        self.canvas.draw()
    
    def findMST(self):
        if self.graph is None:
            QtWidgets.QMessageBox.critical(None, "Error", "No graph found")
            return

        if self.algoBox.currentText() == "Prim":
            self.graph.prim()
        else:
            self.graph.kruskal()
        
        self.draw_graph()
    
    def addVertex(self):
        if self.graph is None:
            QtWidgets.QMessageBox.critical(None, "Error", "No graph found")
            return

        try:
            if not self.vertexNumber.value():
                self.vertexNumber.setValue(0)
            
            if self.vertexNumber.value() in self.graph.vertices:
                raise Exception("Vertex already exists")

            self.graph.add_vertex(int(self.vertexNumber.value()))
            self.draw_graph()
        except Exception as e:
            error_message = f"Error adding vertex: {str(e)}"
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
    
    def delVertex(self):
        if self.graph is None:
            QtWidgets.QMessageBox.critical(None, "Error", "No graph found")
            return
        
        try:
            if not self.vertexNumber.value():
                self.vertexNumber.setValue(0)
            
            if self.vertexNumber.value() not in self.graph.vertices:
                raise Exception("Vertex does not exist")

            self.graph.remove_vertex(int(self.vertexNumber.value()))
            self.draw_graph()
        except Exception as e:
            error_message = f"Error deleting vertex: {str(e)}"
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
    
    def addEdge(self):
        if self.graph is None:
            QtWidgets.QMessageBox.critical(None, "Error", "No graph found")
            return
        
        try:
            if not self.vertex1.value():
                self.vertex1.setValue(0)

            if not self.vertex2.value():
                self.vertex2.setValue(0)

            if not self.weight.value():
                raise Exception("Weight cannot be 0")
            
            if self.vertex1.value() not in self.graph.vertices or self.vertex2.value() not in self.graph.vertices:
                raise Exception("Vertex does not exist")
            
            if self.vertex1.value() == self.vertex2.value():
                raise Exception("Cannot add edge to same vertex")

            edgeExist = False

            for edge in self.graph.edges:
                if self.vertex1.value() == edge[0] and self.vertex2.value() == edge[1]:
                    edgeExist = True
                    break

            if edgeExist:
                raise Exception("Edge already exists")
            
            self.graph.add_edge(self.vertex1.value(), self.vertex2.value(), self.weight.value())
            self.draw_graph()

        except Exception as e:
            error_message = f"Error adding edge: {str(e)}"
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
    
    def delEdge(self):
        if self.graph is None:
            QtWidgets.QMessageBox.critical(None, "Error", "No graph found")
            return
        
        try:
            if not self.vertex1.value():
                self.vertex1.setValue(0)
            
            if not self.vertex2.value():
                self.vertex2.setValue(0)
            
            if self.vertex1.value() not in self.graph.vertices or self.vertex2.value() not in self.graph.vertices:
                raise Exception("Vertex does not exist")

            edgeExist = False

            for edge in self.graph.edges:
                if self.vertex1.value() == edge[0] and self.vertex2.value() == edge[1]:
                    edgeExist = True
                    break

            if not edgeExist:
                raise Exception("Edge does not exist")
            
            self.graph.remove_edge(self.vertex1.value(), self.vertex2.value())
            self.draw_graph()
        
        except Exception as e:
            error_message = f"Error deleting edge: {str(e)}"
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
    
    def reset(self):
        if self.graph:
            self.graph.reset()
            self.draw_graph()

    def findCluster(self):
        if self.graph is None:
            QtWidgets.QMessageBox.critical(None, "Error", "No graph found")
            return
        
        try:
            if not self.clusterNumber.value():
                raise Exception("Cluster number cannot be empty")
            if self.clusterNumber.value() > len(self.graph.vertices):
                raise Exception("Cluster number cannot be greater than number of vertices")
            self.graph.clustering(self.clusterNumber.value())
            self.draw_graph()
        except Exception as e:
            error_message = f"Error finding cluster: {str(e)}"
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
