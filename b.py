# b.py

print('b.py')

print(__name__)


print('导入a')

import a

print('导入a结束')

if __name__ == "__main__":
    print('运行这个python文件，才会显示')