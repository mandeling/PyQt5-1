from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("Button")
#以QWidget左上角为(0,0)点
btn.move(20,20)
#不同的操作系统可能对窗口的最小宽度有规定，若设置宽度小于规定值，则会以规定值进行显示
widget.resize(300,200)
#以屏幕左上角为(0,0)点
widget.move(250,200)

widget.setWindowTitle('PyQT坐标系统例子')
widget.show()
print("QWidget:")
print("w.x()=%d"%widget.x())
print("w.y()=%d"%widget.y())
print("w.width()=%d"%widget.width())
print("w.height()=%d"%widget.height())
print("QWidget.geometry")
print("w.geometry().x()=%d"%widget.geometry().x())
print("w.geometry().y()=%d"%widget.geometry().y())
print("w.geometry().width()=%d"%widget.geometry().width())
print("w.geometry().height()=%d"%widget.geometry().height())

sys.exit(app.exec_())