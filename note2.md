# 数据容器

### 字符串

#### 1.字符串的替换

**字符串.replace(字符串1，字符串2）**

不是修改字符串本身，而是新建一个字符串，字符串具有不可改变性

```python
str="a b c d e"
str_new=str.replace(" ","")
print(str_new)
```

#### 2.字符串的分割

**字符串.split(分隔符字符串)**

按照指定的分割符字符串，将字符串划分为多个字符串，并存入对象列表中，字符串本身不会改变，只是得到一个新的列表对象

#### 3.字符串的切割

**字符串.strip(字符串)**

只能去除首尾的字符串！！！

#### 4.统计次数

**.count（）**

```python
introduction="i am cherie"
new_intro=introduction.count(" ")
print(new_intro)
```

#### 5.统计字符串长度

**len（）**

长度包含空格

```python
introduction="i am cherie"
num=len(introduction)
print(num)
```

---

### 数组list

初始化：list=[]

#### 1.统计长度

**len(list)**

#### 2.求最值

**max（list)**

**min（list)**

#### 3.查找元素

**列表.index(元素)**

#### 4.修改特定位置的元素值

**列表[下标]=值**

#### 5.插入元素

**列表.insert(下标，元素)**

#### 6.追加元素

**列表.append(元素)**

默认将元素追加到尾部，追加到其他地方的话就用insert

#### 7.删除元素

**列表.remove(元素)**

#### 8.抽出一些元素组成新list

**列表[start:end：step]**

### 元组tuple

元组是不可变的！！

不能使用append等追加元素，也不能给元组中的数据重新赋值

### 集合Set

集合是由<font color="red">不重复</font>元素组成的无序容器

#### 1.获取元素个数

len（）

#### 2.判断某元素是否在集合中

x in set

#### 3.添加元素

add（ele）

#### 4.union取并集

```python
books={"a","b"}
books2={"c","d"}
books_all=books.union(books2)
```

#### 5.intersection取交集

```python
books={"a","b"}
books2={"b","d"}
books_all=books.intersecyion(books2)
```

#### 6.difference（）求差集

```python
books={"a","b","c"}
books2={"c","d"}
book=books.difference(books2)
```

### 字典dictionary

dict_a={key:value,key:value,key:value....}