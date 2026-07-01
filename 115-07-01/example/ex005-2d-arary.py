"""
numpy 並未預先建立於 python module 列表，所以必須事先安裝該模組。
指令如下：
pip install numpy
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("arr = ", arr)