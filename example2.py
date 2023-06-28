import multiprocessing
import os


def worker1():
    print("process1: ", os.getpid())

def worker2():
    print("process2: ", os.getpid())

if __name__ == "__main__":
    print("PID: ", os.getpid())
    p1 = multiprocessing.Process(target = worker1)
    p2 = multiprocessing.Process(target = worker2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finished....")
