##线程相关内容

http://www.py3study.com/

【python3自用utils（备忘录）】
https://www.cnblogs.com/daigua/p/10193351.html

1.python多线程编程实例

1.1最常用的多线程例子

import threading
import time

def loop(name):
    for x in range(10):
        print(name + ":" + str(x))
        time.sleep(1)

if __name__ == "__main__":
    threads_pool = []
    for name in ["xxx", "yyy", "zzzz"]:
        t = threading.Thread(target=loop, args=(name,))
        threads_pool.append(t)
        t.start()  # 开启线程任务

    for t in threads_pool:
        t.join()  # 主进程等待子线程完成再结束
    print("---done!---")
1.2 线程池threadpool

import threadpool
import time

def show(name):
    for x in range(10):
        print("name:{}=>x:{}".format(name,x))
        time.sleep(1)

if __name__ == "__main__":
    # 创建线程池对象
    pool = threadpool.ThreadPool(10)

    # 组装任务列表
    name_list = ["张三", "李四", "王五"]
    requests = threadpool.makeRequests(show, name_list)
    
    # 执行任务
    for r in requests:
        pool.putRequest(r)
    # 主进程阻塞等待
    pool.wait()
    print("---done!---")
1.3 线程池futures实现

使用map：

无返回值：
import time

from concurrent import futures

def show(name):
    for x in range(10):
        print("name:{}=>x:{}".format(name,x))
        time.sleep(1)

if __name__ == "__main__":

    name_list = ["张三", "李四", "王五"]
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(show, name_list)
    print("---done!---")
获取返回值：
import time

from concurrent import futures

def show(name):
    for x in range(10):
        print("name:{}=>x:{}".format(name,x))
        time.sleep(0.1)
    return "我是:" + name

if __name__ == "__main__":

    name_list = ["张三", "李四", "王五"]
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_name = executor.map(show, name_list)
        print(future_to_name)
        for future in future_to_name:
            print(future)
    print("---done!---")
使用submit：

获取返回值：
import time

from concurrent import futures

def show(name):
    for x in range(10):
        print("name:{}=>x:{}".format(name,x))
        time.sleep(0.1)
    return "我是:" + name

if __name__ == "__main__":

    name_list = ["张三", "李四", "王五"]
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_name = [executor.submit(show, name) for name in name_list]
        print(future_to_name)
        for future in futures.as_completed(future_to_name):
            print(future.result())
    print("---done!---")
2.python多进程编程实例

2.1 基本例子

from multiprocessing import Process
import time

def show(name):
    for x in range(10):
        print("name:{}=>x{}".format(name,x))
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=show, args=("我是你爸爸",))
    p2 = Process(target=show, args=("我是你妈妈",))

    # 开始多进程任务
    p1.start()
    p2.start()

    # 阻塞等待
    p1.join()
    p2.join()

    print("---done!---")
2.2进程池futures实现

import time

from concurrent import futures

def show(name):
    for x in range(10):
        print("name:{}=>x:{}".format(name,x))
        time.sleep(1)

if __name__ == "__main__":

    name_list = ["张三", "李四", "王五"]
    with futures.ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(show, name_list)
    print("---done!---")