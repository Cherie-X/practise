# numpy

简写numpy：import numpy as np

针对数学相关操作，解决python运算性能不佳的问题

```python
import numpy as np
array=np.array([[1,2,3],[4,5,6]])
print(array)

```

### numpy属性

numpy的数组类被称作ndarray，通常被称为数组

##### ndarray.ndim

ndim->有几个方向，二维数组有行和列两个方向，因此ndim是2

##### ndarray.shape

数组的维度，这是一个指示数组在每个维度上大小的整组元组，例如一个n行m列的矩阵，它的shape属性是（n,m）

##### ndarray.size

数组总元素的个数

##### ndarray.dtype

数组的元素类型

##### ndarray.itemsize

数组中每个元素占用多少字节（内存），若电脑默整数是int64，则输出8，int64=64位，64位=8字节，一位=8字节

```python
import numpy as np
a=np.arange(15).reshape(3,5)
#创建一个从0开始有15个数的数组，即0~14
print("数组的维度是：",a.shape)#(3,5)
print("数组轴的个数：",a.ndim)#2
print("数组元素类型：",a.dtype)#int64
print("数组元素总个数：",a.size)#15
print("类型查询：",type(a))#<class'numpy.ndarray'>
```

### 常用numpy操作

##### 更改维度

将数组从3行4列更改为4行3列

```python
import numpy as np
a=np.arange(12).reshape(3,4)
print(a.shape)
print(a.dtype)
print(a.ndim)
b=a.reshape(4,3)
print(b)#将数组变形为（4，3）
```

##### 展平为一维数组

###### 按行展平

```python
a=np.arrange(12).reshape(3,4)
b=a.reshape(-1)
#输出[ 0  1  2  3  4  5  6  7  8  9 10 11]
```

###### 按列展平

[0,1,2,3]

[4,5,6,7]

[8,9,10,11]

第一列：0,4,8

第二列：1,5,9

第三列：2,6,10

第四列：3,7,11

```python
a=np.arange(12).reshape(3,4)
b=a.reshape(-1,order='F')#F表sh
```

