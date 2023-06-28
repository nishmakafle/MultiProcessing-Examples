import multiprocessing
import time


def get_squre(input_list):
    global result
    if len(input_list) == 4:
        time.sleep(0.5)
    for i in input_list:
        result.append(i * i)



if __name__ == '__main__':
    result = []
    input_list = [1, 2, 3, 4, 5]
    input_list2 = [1, 2, 4, 5]
    p1 = multiprocessing.Process(target=get_squre, args=(input_list, ))
    p2 = multiprocessing.Process(target=get_squre, args=(input_list2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("result in Main loop:", result)
    print(id(result),".................")

