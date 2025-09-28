# 1. 动态类型

name = "VueDev"
age = 25
is_active = True

# 2. 列表 & 字典 （Vue 的 数组 & 对象）

users = ["VueDev", "ReactDev", "AngularDev"]
user = {
    name: "VueDev",
    age: 25,
    is_active: True
}

# 3. 条件与循环

if age > 18:
    print("Adult")
elif age < 18:
    print("Minor")
else:
    print("Invalid age")

for user in users:
    print(user)

# 4. 函数
def greet(name):
    print("Hello, " + name)

# 5. 导入标准库
import math
import random
import json
from datetime import datetime

print(math.sqrt(16))
print(random.randint(1, 10))
print(json.dumps({"name": "VueDev"}))
print(datetime.now())

