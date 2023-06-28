import threading
import time


def get_input(data_list):

    while True:
        item = input("Enter data: ")
        data_list.append(item)
        print(data_list)
    
def count_list(data_list):
    while True:
        time.sleep(3)
        print(len(data_list))

def main():
    data_list = []
    t1 = threading.Thread(target=get_input, args=(data_list, ))
    t2 = threading.Thread(target=count_list, args=(data_list, ))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()