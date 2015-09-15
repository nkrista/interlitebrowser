import sys
from PyQt4 import QtGui, QtCore, QtWebKit


class Browser(QtGui.QWidget):
	
	def __init__(self):
		super(Browser, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.trace = False
		
		mainLayout = QtGui.QVBoxLayout()
		self.linkLabel = QtGui.QLabel(self)
		self.inputLine = QtGui.QLineEdit(self)		
		
		self.viewer = QtWebKit.QWebView(self)
		self.viewer.load(QtCore.QUrl("http://www.google.com"))
		
		toolBar = QtGui.QToolBar()
		goButton = QtGui.QPushButton("Go")
		goButton.clicked.connect(self.switchPages)
		toolBar.addWidget(goButton)
		
		mainLayout.setMenuBar(toolBar)
		mainLayout.addWidget(self.inputLine)
		mainLayout.addWidget(self.viewer)
		self.inputLine.textChanged[str].connect(self.userEdits)
		
		self.setLayout(mainLayout)
		self.setGeometry(2560,1620,500,500)
		self.setWindowTitle("Web Browser")
		self.resize(2000,2000)
		self.show()
		
	def userEdits(self, link):
		self.linkLabel.sizeHint()
		
		if self.trace:
			print "linkLabel has changed"
			
	def switchPages(self):
		
		if self.trace:
			print "inputLine = ", self.inputLine.text()
		
		url = self.inputLine.text()
		self.viewer.load(QtCore.QUrl(url))

def main():
	
	app = QtGui.QApplication(sys.argv)
	
	browse = Browser()
	sys.exit(app.exec_())
	

if __name__ == '__main__':
	main()
		
