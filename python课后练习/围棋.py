import matplotlib.pyplot as plt
import numpy as np

# 定义棋盘的大小
board_size = 19

# 创建棋盘图像
fig, ax = plt.subplots(figsize=(8, 8))

# 绘制棋盘网格
for i in range(board_size + 1):
    ax.plot([i, i], [0, board_size], color='black', lw=1)
    ax.plot([0, board_size], [i, i], color='black', lw=1)

# 设置棋盘背景颜色为浅棕色
ax.set_facecolor('#f5deb3')

# 绘制棋盘的交点
for i in range(board_size):
    for j in range(board_size):
        ax.plot(i + 0.5, j + 0.5, 'ko', markersize=3, alpha=0.7)

# 设置坐标轴
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-0.5, board_size - 0.5)
ax.set_ylim(-0.5, board_size - 0.5)

# 设置棋盘的标题
ax.set_title('围棋棋盘', fontsize=16)

# 保存图像
plt.savefig('go_board.png', dpi=300, bbox_inches='tight')
plt.show()
