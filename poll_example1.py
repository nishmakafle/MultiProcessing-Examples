from multiprocessing import Pool

def get_squre(x):
    return x * x



if __name__ == '__main__':
    pool = Pool(processes=3)