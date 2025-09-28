# 1. 列表推导式（Vue 的 computed 映射）

users = ["apple", "banana", "cherry"]
user_upper = [user.upper() for user in users]

# 2. lambda 函数（类比 Vue 的箭头函数）
# 箭头函数是 JS 的“内联匿名函数”，lambda 是 Python 的“内联匿名函数”
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
]
adults = list(filter(lambda person: person["age"] >= 18, people))


# 3. 类与对象（Vue 的 class 组件）
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18


user = User("VueDev", 25)
print(user.is_adult())


# 4. 装饰器（类比 Vue 的 mixin 或高阶函数）
def log(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result

    return wrapper


@log
def say_hi(a, b):
    return a + b


say_hi()
