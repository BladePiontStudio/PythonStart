#!/usr/bin/evn python3
# python基本数据类型

# 一、数字型（整数、浮点数、布尔和复数）
numberInt = 1
print(numberInt)
print(type(numberInt))

numberFloat = 1.2
print(numberFloat)
print(type(numberFloat))

numberBool = True
print(numberBool)
print(type(numberBool))

numberComplex = 1 + 3j
print(numberComplex)
print(type(numberComplex))

# 二、字符串 (Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。)
string = 'abc'
print(string)
print(type(string))

# 三、List(列表)
"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：变量[头下标:尾下标] 尾下标 =》 表示个数
"""
lists = [1, 2, 'abc']
print(lists[0:2])

# 四、Tuple（元组）
"""
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
"""
tuple = (1, 2, 'abc')
print(tuple[0: 2])

# 五、Set（集合）
"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 
"""
student = {'Tom', 'Jim', 'Mary', 'Jack', 'Rose'}

print(student)
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# 六、Dictionary（字典）
"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。 
"""
dict = {}
dict['one'] = "one string"
dict[1] = 1
tinydict = {'name': 'jay', 'code': 1, 'site': 'phalcon.site'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[1])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
