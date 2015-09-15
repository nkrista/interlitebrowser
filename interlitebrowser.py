import sys
from PyQt4 import QtGui, QtCore, QtWebKit

class Browser(QtGui.QWidget):
	
	def __init__(self):
		super(Browser, self).__init__()
		self.initUI()
		
	def initUI(self):
		
		mainLayout = QtGui.QVBoxLayout()
		self.linkLabel = QtGui.QLabel(self)
		inputLine = QtGui.QLineEdit(self)
		
		viewer = QtWebKit.QWebView(self)
		viewer.load(QtCore.QUrl("http://www.google.com"))
		
		mainLayout.addWidget(inputLine)
		mainLayout.addWidget(viewer)
		inputLine.textChanged[str].connect(self.userEdits)
		
		self.setLayout(mainLayout)
		self.setGeometry(2560,1620,500,500)
		self.setWindowTitle("Web Browser")
		self.resize(2000,2000)
		self.show()
		
	def userEdits(self, link):
		trace = False
		self.linkLabel.sizeHint()
		
		if trace:
			print "linkLabel has changed"

def main():
	
	app = QtGui.QApplication(sys.argv)
	
	browse = Browser()
	sys.exit(app.exec_())
	

if __name__ == '__main__':
	main()
		
