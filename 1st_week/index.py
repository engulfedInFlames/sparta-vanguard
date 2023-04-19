import os
import threading
from multiprocessing import Process

# 1. 멀티 프로세싱 ✅
# os.getpid()
# print("Hello OS!")  # 이 또한 프로세스
# print("My pid is", os.getpid())


def func1():
    print("Child porcess : ", os.getpid())


def func2():
    print("This is func2")


def func3():
    print("This is func3")


# 2. 멀티 스레드 ✅


def func4():
    print("Process ID : ", os.getpid())
    print("Thread ID : ", threading.get_native_id())


if __name__ == "__main__":
    print("Version 1")
    print("! Multi Processing")
    print("Parent process : ", os.getpid())
    # 동일한 작업을 하는 프로세스를 여러 개 만들 수 있다.
    child1 = Process(target=func1).start()
    child2 = Process(target=func1).start()
    child3 = Process(target=func1).start()
    # 별개의 프로세스로 동시 실행 상태가 된다.
    child4 = Process(target=func2).start()
    child5 = Process(target=func3).start()

    print()

    print("! Multi Threading")
    print("Parent process : ", os.getpid())
    thread = threading.Thread(target=func4).start()

    print()

    print("Version 2")
    print("! Multi Processing")
    print("Parent process : ", os.getpid())

    child1 = Process(target=func1)
    child2 = Process(target=func1)
    child3 = Process(target=func1)
    child4 = Process(target=func2)
    child5 = Process(target=func3)
    child1.start()
    child2.start()
    child3.start()
    child4.start()
    child5.start()
    child1.join()
    child2.join()
    child3.join()
    child4.join()
    child5.join()

    print()

    print("! Multi Threading")
    print("Parent process : ", os.getpid())
    thread = threading.Thread(target=func4).start()

# The reason why the expected results are not obtained is that the child processes and the main process are executed asynchronously. When a child process is started using the Process() method, the method returns a Process object immediately, which means that the next line of code after starting the process will continue to execute while the child process runs in the background. Therefore, the print statement after starting the child processes may be executed before the child processes finish running and printing their output.

# To ensure that the child processes complete before the next line of code is executed, you can use the join() method of the Process object. The join() method waits for the child process to complete before continuing the execution of the main process. Here's an updated version of the code that should produce the expected results:

# This code starts all the child processes, and then waits for each one to complete using the join() method before moving on to the next line of code. This ensures that the child processes complete before the main process continues.
