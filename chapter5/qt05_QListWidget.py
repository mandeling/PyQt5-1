import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ListWidget(QListWidget):
	def clicked(self, item):
		QMessageBox.information(self, 'ListWidget', '你选择了：' + item.text())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	listWidget = ListWidget()
	listWidget.resize(300, 120)
	listWidget.addItem('Item 1')
	listWidget.addItem('Item 2')
	listWidget.addItem('Item 3')
	listWidget.addItem('Item 4')
	listWidget.setWindowTitle('QListwidget例子')
	listWidget.itemClicked.connect(listWidget.clicked)
	listWidget.show()
	sys.exit(app.exec())
