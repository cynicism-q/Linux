# coding: utf-8    	#需要输出汉字必须加上这一句
					# 一个汉字不一定占两个字节

#(1)变量名和赋值

#counter = 0
#pi = 3.14
#name = "qi"
#file = "其"
#
#print counter
#print pi
#print name
#print file

#(2)变量的增量赋值
#counter = 1
#counter += 1
#print counter

#(3)动态类型
#counter = 1
#print counter
#counter = 'hehe'
#print counter

#(4)变量名命名规则
#和C语言一致，字母，数字，下划线，数字不能开头

#(5)认识数字 
#type()  函数返回参数的类型
#myint = 100
#print type(myint)   #内建类型  不需要包含任何头文件
#myint =  3.14
#print type(myint)    
#x = 123.456789123
#print type(x)    #python中的float与c语言double精度相同

#myint = 10000000000000000000000000
#myint *= myint   
#print myint     #python整数长度没有限制
#print type(myint)

#(6)复数
#a = 10 + 5j
#print type(a)   #complex是复数类型

#(7)认识字符串
#单引号/双引号
#三引号可以用三个连续的单引号，也可以用三个连续的双引号
#a = 'diyi'
#b = "dier"
#c = '''disan'''
#print a,b,c  #可以连续打印
#
##如果字符串中有单引号和双引号，我们可以使用三引号
#mystr = """  my "name" is 'wsbg' """
#print mystr
#mystr = ''' my "name" is 'wsbg' '''  #c语言要进行转义\"  是输出双引号
#print mystr

#但是有些不可见字符仍然需要转义，使用\进行转义，比如换行符\n
#a = 'My name is \n "wsbg"'
#print a 
#a = 'My name is \\n "wsbg" ' #字符串结尾'\0'只使用于C语言
#print a

#(8)使用索引操作符[]/下标来访问字符串的内容
#mystr = 'abcd'
#print mystr[0],mystr[1],mystr[2],mystr[3]
#print type(mystr)
#print type(mystr[0])
##print mystr[100]   #越界
#print mystr[-1],mystr[-2],mystr[-3],mystr[-4] #输出倒数第1，2，3，4个字符串

#切片操作符[:]来获取子字符串（切片操作是一个前闭后开区间）
#字符串的索引规则是:第一个字符串索引是0，最后一个字符串的索引是-1（可以理解是length-1）
#mystr = 'ABCD'
#print mystr[1:2]
#print mystr[1:-1]
#print mystr[1:]     #第二个字符串到结束
#print mystr[:2]     #开始到第二个字符串
#print mystr[:]      #输出全部
#print mystr[2:1]    #非法操作空字符串
#print mystr[1:100]  #不会越界 第二个到最后一个

#(9)字符串拼接
#C语言中使用strcat
#a = 'hello '
#b = 'world'
#print a+b

#字符串重复
#a = "hehe "
#b = a*4
#print len(a)  
#print b
#e = a*b
#print e

#(10)格式化字符串
	#格式化字符串语法规则和C语言是一样的
  #a = 100
  #pystr = "a = %d"
  #result = pystr % a
  #print result

  #A = 100
  #mystr  = "A = %d" % A
  #print mystr

#(11)认识bool类型
#python 用True和False表示布尔值  注意首字母是大写的
#C语言在C99就有布尔值\
#a = True
#print a
#b = False
#print b
#print type(a)

#和整数进行运算是，True被当做1，False被当作0
#a = True
#b = True + 1
#print b

#(12)输入输出
#a = 20
#print a  #print不是函数，是一个语句
#print(a) #print()是一个函数
#a = raw_input( )  #函数从标准输入中获取用户输入,没有默认阻塞
#print a
#a = raw_input('$')  #命令输入符
#print(a)

#raw_input返回的结果是一个字符串，如果需要获取一个数字，需要使用int函数把字符串转化为整数
 #num = raw_input('Enter num:')
 ##print num + 1   #不能这样输出获取结果
 #print int(num) + 1   #int是一个内建函数

#(13)python 中的除法
#1）传统除法
#a = 1
#b = 2
#print a/b   #两个数都数都是整数，得到的结果也为整数
#
#a = 1.0
#b = 2
#print a/b  #有一个数为浮点数，结果也为浮点数

#2）地板除（向下取整）
#a = 1
#b = 2
#print a//b
#
#a = 1.0
#b = 2
#print a//b
#
#a = -1.0
#b = 2
#print a//b

#3)精度除
#from __future__ import division
#a = 1
#b = 2
#print 1/2

#(14)乘方操作
#a = 10
#b = 3
#print a**b

#a = 10
#b = 3
#print a++b   //等效为a+ +b  尽量不要这样做

#(15)比较运算符
#print 2 < 3 
#print 2 == 8
#print 2 == 2
#print 2 != 3

#print 2 < 3 < 4 
#print 2 < 3 and 3 < 4    #与上一行等价    尽量不要用

#print 2 > 4 or 2 < 4
#print not 6.2 <= 6

#字符串和字符串之间也可以使用运算符进行操作
#例如使用+进行字符串的连接
#print 'haha'+'hehhe'
#字符串可以使用== != 来判断字符串的内容是否相同
#print 'haha' != 'hehe'
#字符串之间也可以比较大小，这个大小的结果取决与字符串的"字典序"
#print 'aa' < 'ab'

#(16)列表
###元组和列表基本操作是一样的，但有一点不同，列表中的元素可修改，元组中的元素不可修改
#a = [1,2,3,4,'wsbg']
#print type(a)       #list列表类型
#print type(a[0])   #int型
#print a
#print a[4]    #使用下标来访问元素
#a[0] = 'chu'
#print a
#print a[1:3]
#元组
#a = (1,2,3,4)
#print a
#print type(a)
#print a[0]
#print a[1:3]
#a[0] = 0   #源组中的元素不能被修改

#(17)字典
#字典是python中的映射数据类型，存储键值对(key-value)
#几乎所有类型的python对象都可以用做键，不过一般还是数字和字符串最常用
#使用{}表示字典

#a = {'ip':'127.0.0.1'}  #创建字典
#print a['ip']			#取字典中的元素
#a['port'] = 80          #插入新的键值对
#print a

#(18)理解引用
#a = 100
#print id(a)
#a = 200
#print id(a)
#
#b = a
#print id(b)
#
#b = 300
#print id(b)

#(19)代码块及缩进
#if 3 > 9:
#	print 'wsbg'
#else:
#	print 'admin'

#python里面还有神奇的elif(意思是else if)
#a = raw_input("$")
#b = raw_input("$")
#
#if a > b:
#	print 1
#elif a < b:
#	print 2
#else:
#	print 3

#(20)while循环
#count = 0
#while count < 3:	
#	print 'loop %d' % count
#	count += 1

#(21)for循环
#a = "wsbg"
#for c in a:
#	print c

#a = [1,2,3,4]
#for item in a:
#	print item

#a = {'ip':'192.168.1.1','port':80}
#for key in a:
#	print key,a[key]

#内建函数range(0,3)能够生成一个数字组成的列表，方便进行for循环遍历
#for i in range(0,3):
#	print 'loop %d' % i

#for i in range(0,100,2):    #遍历[0,100)区间中偶数
#	print i

#查找[0，100）第一个3的倍数
#for i in range(1,100):
#	if i % 3 == 0:
#		break
#print i

#for i in range(0,100):
#	if i % 3 != 0:
#		continue
#	print i

#pass语句
#有时候需要用到空语句这样的概念，什么都不做，由于没有{},需要有一个专门的语句来占位，要
#缩进就混乱了
#x = raw_input('$')
#if int(x) % 2 == 0:
#	pass
#else:
#	print x
	
#使用for循环将生成的值放在一个列表中
#生成[0,4）
#squared = [x ** 2 for x in range(4)]
#print squared

#获取[0,8)区间中的所有的奇数
#evens = [x for x in range(0,8) if x % 2 == 1]
#print evens

#(22)函数
#def Add(x,y):
#	return x + y
#print Add(1,2)

#python中没有"重载"这样的概念，相同名字的函数，后面会覆盖前面的
#def Func():
#	print 'aaaa'
#
#def Func():
#	print 'bbbb'
#
#Func()

#python支持默认参数，函数的参数可以具备默认值

#def Func(debug = True):
#	if debug:
#		print 'in debug mode'
#	print 'done'
#
#Func()
#Func(False)

#python解包(unpack)语法，函数返回多个值
#def GetPoint():
#	return 100,200
#
#x,y = GetPoint()
#print x,y

#函数也是"对象"，一个函数和一个数字，字符串一样，都可以定义"别名"来引用它
#def Func():
#	print 'aaa'
#func = Func
#func()
#print type(func)

#(23)文件操作
#使用内建函数open打开一个文件
#handle = open('test.txt','r')
#for line in handle:
#	print line
#handle.close()

#统计文本中的词频

#handle = open('test.txt','r')
#words = {}
#for word in handle:
#	word = word[:-1]
#	if word not in words:
#		words[word] = 1
#	else:
#		words[word] += 1
#handle.close()
#print words

#(24)模块
def Add(x,y):
		return x + y
