#!/usr/bin/python

import sys
import threading
import time

class Semaphore(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1

class Fork(object):

    def __init__(self, number):
        self.number = number           # 叉子的 id
        self.user = -1                 # 跟踪哲学家的使用情况
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):         # 同步
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("哲学家[%s] 拿起 叉子[%s]\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):         # 同步
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("哲学家[%s] 放下 叉子[%s]\n" % (user, self.number))
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, number, left, right, butler):
        threading.Thread.__init__(self)
        self.number = number            # 哲学家数量
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for i in range(1):                  
            self.butler.down()              # 管家开始服务
            time.sleep(0.1)                 # 思考
            self.left.take(self.number)     # 拿起左边的叉子
            time.sleep(0.1)                 # (yield makes deadlock more likely)
            self.right.take(self.number)    # 拿起右边的叉子
            time.sleep(0.1)                 # 吃
            self.right.drop(self.number)    # 放下右边的叉子
            self.left.drop(self.number)     # 放下左边的叉子
            self.butler.up()                # 管家结束服务
        sys.stdout.write("哲学家[%s] 结束思考开始吃饭\n" % self.number)


def main():
    # 哲学家数量以及叉子数量
    n = 5

    # 避免死锁 (可用数为 n-1)
    butler = Semaphore(n-1)

    # 叉子
    c = [Fork(i) for i in range(n)]

    # 哲学家
    p = [Philosopher(i, c[i], c[(i+1)%n], butler) for i in range(n)]

    for i in range(n):
        p[i].start()


if __name__ == "__main__":
    main()