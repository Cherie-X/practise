raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
list=[]
for i in raw_data:
    try:
        j=int(i)
        if j>=80:
            list.append(j)
    except:
        continue
a=max(list)
b=min(list)
list1=[]
for i in list:
    l=(i-b)/(a-b)
    list1.append(l)
    if l>1:
        print("核心过载")
    else:
        print("运转正常")

