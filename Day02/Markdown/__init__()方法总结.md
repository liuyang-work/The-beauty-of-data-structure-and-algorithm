### 例子一

```python
class Student:
    def __init__(self):       #两者之间的区别
        self.name = None
        self.score = None
```



### 例子二

```python
def __init__(self, name, score):
    self.name = name
    self.score = score
```

​		区别很明显，前者在__init__方法中，只有一个self，指的是实例的本身，但是在方法的类部，包含两个属性，name， score

下面的这个即是在定义方法时，就直接给定了两个参数，



#### 实例化方法

```python
# student = Student("sansan", 90)

student = Student()
student.name= "sansan"
student.score = 90

# susan = Student("sunny", 78)

susan = Student()
susan.name = "susan"
susan.score = 8
```

即显示了两种实例化的方法， 注释的部分即是在创建的时候就直接传入参数

那么这两者的区别，在哪里？

第一种的区别，他定义了这样一种类，他可以是一个空的结构，比如学生的表，当学生还没有进行考试时，他已经有了学生的姓名和成绩，当新的数据来的时候，可以直接添加进来。这个可以很方便的进行，

而第二种，则需要必须传值，不允许为空。当然第二种对于已有数据的导入是很方便的，在语句上减少了很多