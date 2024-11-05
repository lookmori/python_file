import sys
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import requests

app = QApplication(sys.argv)
win = QWidget()
grid = QGridLayout()

figure = Figure()
canvas = FigureCanvas(figure)


# 画出折线图
def show_line():
    pass


ax = figure.add_subplot(111)
x = [1,2,3,4,5]
y = [10,4,6,2,6]
ax.plot(x,y)
canvas.draw()


input = QLineEdit()
seartch_btn = QPushButton('搜索')
seartch_7__btn = QPushButton('搜索7日天气')



grid.addWidget(input,1,1,1,1)
grid.addWidget(seartch_btn,1,3,1,1)
grid.addWidget(seartch_7__btn,2,1,3,3)
grid.addWidget(canvas,3,1,3,3)


# 搜索当日天气
def search_today():
    print(input.text())
    # try:
    #     result = requests.get('xxx',data={'city':city})
    #     print(result.json())
    # except requests.exceptions.HTTPError:
    #     return {'text':'请求错误'}
    # except requests.exceptions.Timeout:
    #     return {'text':'网络慢，请稍后再试'}
    

# 搜索七日天气
def search_7day(city='北京'):
    pass

seartch_btn.clicked.connect(search_today)
seartch_7__btn.clicked.connect(search_7day)

win.setLayout(grid)
win.setWindowTitle('天气查询')
win.show()

sys.exit(app.exec_())


