### pandas

### csv

#### csv是什么？

一种用来储存表格数据的文本格式。用普通的文本，把表格一行一行写下来，每一列之间用逗号隔开（英文逗号）

![1772453769813](C:\Users\cheri\AppData\Roaming\Typora\typora-user-images\1772453769813.png)

#### 如何创建csv文件？

在桌面上新建纯文本文本文件，到文件资源管理器勾选“查看文件拓展名”将文件后缀修改为csv

![1772453933481](C:\Users\cheri\AppData\Roaming\Typora\typora-user-images\1772453933481.png)



#### 如何读取csv数据？

```python
import pandas as pd
df=pd.read_csv(r"C:\Users\cheri\Desktop\data.csv")
print(df)
#输出：
#  name  age  score
# 0  Cherie   20     90
# 1     Tom   21     85
# 2    Lili   19     95
```

# matplotlib

Matplotlib 是 Python 里非常常用的一个绘图库，它的作用就是把数据画出来——折线图、柱状图、散点图、饼图……几乎所有常见图表都能画

### 调用并生成简单的线性图像

```python
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,1,50)
y=2*x+1
plt.plot(x,y)
plt.show()
```

### 设置坐标轴

```
plt.xlabel("i'm x")
plt.ylabel("i'm y")
```

![1773102487882](C:\Users\cheri\AppData\Roaming\Typora\typora-user-images\1773102487882.png)

