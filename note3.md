# try except异常处理

### 结构

将有可能发生异常的代码放在try下方，若不能运行则运行except下的代码。正常运行的话会跳过except运行else下的语句

```python
try:
    value=8/0
    print(value)
except:
    print("error")
else:
    print("no error")
```

### 捕获特殊类型的错误

```python
try:
    value=8/0
    print(value)
except ZeroDivisionError:
    print("zerodivisionerror")
except NameError:
    print("NameError")
```

### 记录异常的类型

导入traceback这个包

```python
import traceback
try:
    value=8/0
    print(value)
except:
    info=traceback.format_exc()
    print(info)
```

# if-else-elif分支判断

### if单分支

```
if 条件表达式:
    满足条件时执行的代码块
```

```python
num = 8
if num > 0:
    print(f"{num} 是正数") 
```

### if-else双分支

```
if 条件表达式:
    满足条件时执行的代码块
else:
    不满足条件时执行的代码块
```

```python
age = 17
if age >= 18:
    print("你已成年")
else:
    print("你未成年")
```

### if-elif-else多分支

```
if 条件1:
    满足条件1时执行的代码块
elif 条件2:
    不满足条件1，但满足条件2时执行的代码块
elif 条件3:
    不满足条件1、2，但满足条件3时执行的代码块
...  # 可添加任意多个elif
else:
    所有条件都不满足时执行的代码块
```

```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")  # 输出：良好
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

# for/while循环结构

### for循环

```python
for 变量 in 可迭代对象:
    循环体代码
# 可迭代对象：字符串、列表、元组、字典、range() 等
```

#### 遍历序列

* 遍历字符串

  ```python
  str1 = "Python"
  for char in str1:
      print(char)
  ```

  

* 遍历列表

  ```python
  nums = [1, 2, 3, 4]
  sum_num = 0
  for num in nums:
      sum_num += num 
  print(sum_num)
  ```

  

#### 列表推导式

##### 简单式

* range(n)：生成 0 到 n-1 的整数（共 n 个）

* range(start, end)：生成 start 到 end-1 的整数

* range(start, end, step)：按步长 step 生成序列

  ```python
  for i in range(5):
      print(i)  # 输出：0 1 2 3 4
  ```

```python
list=[x for x in range(1,10)]
```

##### 带公式

```python
list=[]
for i in range(1,11):
	list.append(x*x)
print(list)
```



```
list=[x*x for x in range(1,11)]
```

##### 包含判断和筛选

```python
list=[]
for x in range(1.11):
	if x%2==0:
		list.append(x)
```

```
list=[x for x in range(1,11) if x%2==0]
从左到右依次递进
```



### while循环

```python
while 条件表达式:  # 条件为 True 时执行循环体
    循环体代码
```

#### 基础条件循环

```python
count = 1
while count <= 5:
    print(count)  # 输出：1 2 3 4 5
    count += 1
```

#### 无限循环

通过 `while True` 实现无限循环，结合 `break` 手动终止

```
while True:
    input_str = input("请输入指令（输入q退出）：")
    if input_str == "q":
        print("程序退出")
        break  # 终止循环
    else:
        print(f"你输入的指令是：{input_str}")

```

# 匿名函数lambda

具名函数：

```python
def 函数名(参数1，参数2)：
	代码块
	return 语句
```

匿名函数：

```
lambda 参数1，参数2：函数体代码
```

当

* 函数体只有一行代码
* 用作其他函数的参数

时通常使用lambda函数简化代码

# map函数

```python
member=["张三","李四","王五"]
def prefix(n):
    m="QG_"+n
    return m
member_new=list(map(prefix,member))
print(member_new)
```

