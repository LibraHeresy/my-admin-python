# 1. 迭代器 & 生成器
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


for i in count_up_to(5):
    print(i)

# 2. 上下文管理器
with open("file.txt", "w") as f:
    f.write("Hello, World!")
    f.close()


# 3. 元类（类比 Vue 的自定义指令或插件系统）
# 只在一个特定生命周期点干一次脏活
# 元类既有继承的壳，也有指令/插件的魂——
# “壳”用来代码复用，“魂”用来一次性干预生命周期。
# 拉远叫继承，拉近叫指令；两种类比都对，只是视角不同。
class SingletonMeta(type):
    """让任何继承自 SingletonMeta 的类都只能有一个实例"""

    _instances = {}

    def __call__(cls, *args, **kwargs):  # 相当于 Vue 的 beforeCreate
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        print("Logger 初始化一次")


l1 = Logger()  # 首次：打印「Logger 初始化一次」
l2 = Logger()  # 再次：无打印，返回同一对象
assert l1 is l2

# 4. 异步编程（类比 Vue 的 async/await + axios）
# async 写在 函数/方法 前面 → 声明协程；
# async with 写在 代码块 前面 → 异步上下文管理器语法糖，自带 2 次隐藏式 await（进入/退出）；
# await 写在 函数/方法 前面 → 交出控制权；
# as 别名关键字
# async def              →  造一辆“协程车”
#      ↓
# async with             →  车上装“自动开门/关门”的异步集装箱
#      ↓
# await                  →  挂挡、松离合（交出控制权）
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


asyncio.run(fetch("https://vuejs.org"))
