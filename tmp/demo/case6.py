# 课程类
class Course(object):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


# 人类
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def __str__(self):
        return f"姓名:{self.name},性别:{self.__sex}"

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, name):
    #     self.__name = name
    #
    # @property
    # def sex(self):
    #     return self.__sex
    #
    # @sex.setter
    # def name(self, sex):
    #     self.__sex = sex


# 学生类
class Student(Person):

    def __init__(self, name, sex, balance):
        super(Student, self).__init__(name, sex)
        self.__balance = balance
        self.__class_list = []

    @property
    def classList(self):
        return [class_.name for class_ in self.__class_list]

    def addClass(self, class_):
        if self.__balance > class_.price:
            self.__class_list.append(class_)
            self.__balance -= class_.price
            class_.addStudent(self)
            class_.totalBalance()
            return
        print("余额不足，无法报名班级")

    def removeClass(self, class_):
        if class_ in self.__class_list:
            self.__class_list.remove(class_)
            class_.removeStudent(self)
        print("班级不存在，无法退学")


class Employee(Person):
    def __init__(self, name, sex):
        super(Employee, self).__init__(name, sex)
        self.money = 0


class Teacher(Employee):
    def __init__(self, name, sex):
        super(Teacher, self).__init__(name, sex)
        self.__class_list = []

    @property
    def classList(self):
        return [class_.name for class_ in self.__class_list]

    def teachClass(self, class_):
        self.__class_list.append(class_)
        class_.teacher = self


class Class(object):
    def __init__(self, name):
        self.__name = name
        self.__price = 0
        self.__course_list = []
        self.__student_list = []
        self.__teacher = None
        self.__balance = 0
        self.__school = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def school(self):
        return self.__school.name

    @school.setter
    def school(self, school):
        self.__school = school

    @property
    def price(self):
        return self.__price

    @property
    def courseList(self):
        return self.__course_list

    def addCourse(self, course):
        self.__course_list.append(course)
        self.__price += course.price

    @property
    def studentList(self):
        return [stu.name for stu in self.__student_list]

    def addStudent(self, student):
        self.__student_list.append(student)

    def removeStudent(self, student):
        self.__student_list.remove(student)

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        self.__teacher = teacher

    @property
    def balance(self):
        return self.__balance

    def totalBalance(self):
        self.__balance = self.__price * len(self.__student_list)


class School(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.employee_list = []
        self.__school_list = []

    def __str__(self):
        return f"学校:{self.name} 余额:{self.balance}"

    @property
    def schoolList(self):
        return [school.name for school in self.__school_list]

    def addEmployee(self, employee):
        self.employee_list.append(employee)

    def addBranchSchool(self, school):
        self.__school_list.append(school)

    def getEmployee(self):
        return [emp.name for emp in self.employee_list]

    def getTotalBalance(self):
        res = {}
        sum = 0
        for school in self.__school_list:
            school.getTotalBalance()
            res[self.name] = school.balance
            sum += school.balance
        res[self.name] = sum
        return res

    def getTotalEmployee(self):
        sum_emp = 0
        for school in self.__school_list:
            sum_emp += len(school.employee_list)
        sum_emp += len(school.employee_list)
        return sum_emp

    def getTotalStudent(self):
        sum_stu = 0
        for school in self.__school_list:
            sum_stu += school.getTotalStudent()
        return sum_stu


class BranchSchool(School):
    def __init__(self, name, balance):
        super(BranchSchool, self).__init__(name, balance)
        # 分校的班级列表：私有属性
        self.__class_list = []

    # 获取班级列表
    @property
    def classList(self):
        return [class_.name for class_ in self.__class_list]

    # 添加班级
    def addClass(self, class_):
        # 1、添加班级
        self.__class_list.append(class_)
        # 2、添加老师员工
        self.addEmployee(class_.teacher)

    # 获取总的余额
    def getTotalBalance(self):
        for class_ in self.__class_list:
            # 1、结算班级收入
            class_.totalBalance()
            # 2、累加班级收入
            self.balance += class_.balance

    # 获取学生总人数
    def getTotalStudent(self):
        sum_stu = 0
        for class_ in self.__class_list:
            sum_stu += len(class_.studentList)
        return sum_stu


# 总校
school = School("总校", 100000)
print(school)
# 分校
bj1 = BranchSchool("小猿圈北京分校", 2222)
sz1 = BranchSchool("深圳南山大学城分校", 5555)

# 添加分校
school.addBranchSchool(bj1)
school.addBranchSchool(sz1)

# 初始化班级
class1 = Class("Python 基础班级")
class2 = Class("Python 进阶班级")

# 初始化课程
c1 = Course("Python 基础", 666)
c2 = Course("Python 进阶", 1666)
c3 = Course("Python 实战", 2666)

# 添加课程
class1.addCourse(c1)
class1.addCourse(c2)
class2.addCourse(c2)
class2.addCourse(c3)

# 初始化老师
tea1 = Teacher("小菠萝老师", "girl")
tea2 = Teacher("大菠萝老师", "boy")

# 老师授课
tea1.teachClass(class1)
tea2.teachClass(class2)

bj1.addClass(class1)
sz1.addClass(class2)

# 初始化学生
stu1 = Student("小菠萝", "girl", 50000)
stu2 = Student("大菠萝", "boy", 50000)
stu3 = Student("大大菠萝", "girl", 10000)
# 学生报名
stu1.addClass(class1)
stu1.addClass(class2)
stu2.addClass(class1)
stu3.addClass(class2)

# 普通员工
emp1 = Employee("小菠萝员工", "girl")
emp2 = Employee("大菠萝员工", "boy")
emp3 = Employee("小小菠萝员工", "girl")

print(bj1.getTotalStudent())
print(school.getTotalBalance())
print(school.getTotalEmployee())
