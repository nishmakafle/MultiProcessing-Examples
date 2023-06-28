import multiprocessing

def get_squre(x):
    return x * x

def get_cube(x):
    return x * x * x 


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=get_squre, args=(10, ))
    p2 = multiprocessing.Process(target=get_cube, args=(10, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("process is finished")
