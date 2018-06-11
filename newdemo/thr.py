from threading import Thread
import threading
import time


class MyThread(Thread):

    def __init__(self,interval):
        super(MyThread, self).__init__()
        self.inter=interval
    def run(self):
        for i in range(5):
            time.sleep(0.5)
            print('name:',self.name,'tid:',threading.get_ident())


if __name__ == '__main__':
    t1=MyThread('pyt')
    t2=MyThread('hon')
    t1.start()
    t2.start()
    print("waiting..1..")
    t2.join()
    print("waiting..2..")