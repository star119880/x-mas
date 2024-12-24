tree = input('enter any single symbol:  (press enter)')
#如果用户取消输入，则设置默认值
if not tree:
    tree = "*"   
    
import numpy as np
from colorama import Fore, init
import pyfiglet
import os
# 调整终端窗口大小，参数为行数和列数
os.system('mode con: cols=120 lines=40')  # 宽度120，行数40

# 初始化 colorama
init(autoreset=True)  # 启用颜色支持并自动重置
# 第一部分的樹形
x = np.arange(7, 16)
y = np.arange(1, 18, 2)
z = np.column_stack((x[::-1], y))

tree_part = []
tree_part.append(' ' * (z[0][0]) + '*')  # 樹頂
for i, j in z:
    tree_part.append(' ' * i + str(tree) * j)  # 樹體
for r in range(2):  # 樹幹的高度減少一行
    tree_part.append(' ' * 13 + ' || ')
tree_part.append(' ' * 10 + r' \======/')  # 樹幹底部

# 第二部分的縮小心形
heart_part = []
heart = '\n'.join(
    [''.join(
        [('Merry Christmas '[(x - y) % len('Merry Christmas ')]
          if ((x * 0.1) ** 2 + (y * 0.2) ** 2 - 1) ** 3 - (x * 0.1) ** 2 * (y * 0.2) ** 3 <= 0
          else ' ')
         for x in range(-15, 15)])  # 縮小範圍
     for y in range(7, -7, -1)]  # 縮小高度
)
heart_part.extend(heart.split('\n'))

# 合併樹形和心形部分的最大寬度
max_width = max(len(line) for line in tree_part + heart_part)
tree_part_aligned = [line.ljust(max_width) for line in tree_part]
heart_part_aligned = [line.ljust(max_width) for line in heart_part]

# 生成 ASCII 字體的 Merry Christmas
ascii_art1 = pyfiglet.figlet_format(f'{" " * 10}M e r r y')
ascii_art2 = pyfiglet.figlet_format(f'C h r i s t m a s')
ascii_art3 = pyfiglet.figlet_format(f'm y{" " * 18}l a d y')

# 对 ASCII 艺术字按行分割并着色
ascii_lines1 = ascii_art1.split("\n")
ascii_lines2 = ascii_art2.split("\n")
ascii_lines3 = ascii_art3.split("\n")

BRIGHT_YELLOW = '\033[93m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_RED = '\033[91m'
#RESET = '\033[0m'  # 重置颜色


# 打印 Merry Christmas 的上半部（紅色）和下半部（綠色）
for line in ascii_lines1:
    print(BRIGHT_RED + line)
for line in ascii_lines2:
    print(BRIGHT_GREEN + line)
for line in ascii_lines3:
    print(BRIGHT_RED + line)

# 打印樹形和心形部分
max_lines = max(len(tree_part_aligned), len(heart_part_aligned))
while len(tree_part_aligned) < max_lines:
    tree_part_aligned.append(' ' * max_width)
while len(heart_part_aligned) < max_lines:
    heart_part_aligned.append(' ' * max_width)

# 同步打印（樹幹部分換色）
for t_line, h_line in zip(tree_part_aligned, heart_part_aligned):
    if '||' in t_line or r'\======/' in t_line:  # 判斷是否是樹幹部分
        print(BRIGHT_YELLOW + t_line + ' ' + BRIGHT_RED + h_line)
    else:
        print(BRIGHT_GREEN + t_line + ' ' + BRIGHT_RED + h_line)

# 暂停窗口
input("Press Enter to exit...")


#pyinstaller --onefile --clean --icon=icon.ico --add-data="E:\UV\program\shioaji\.venv\Lib\site-packages\pyfiglet\fonts;pyfiglet/fonts" x_mas.py
#pyinstaller --onefile --icon=icon.ico --add-data="E:\UV\program\shioaji\.venv\Lib\site-packages\pyfiglet\fonts;pyfiglet/fonts" x_mas.py


