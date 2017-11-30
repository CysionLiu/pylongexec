import random
import threading

import time


def timer(interval):
    for i in range(5):
        time.sleep(random.choice(range(interval)))
        th_id = threading.get_ident()
        print('thread:{0},start-time:{1}'.format(th_id, time.ctime()))


def test_timer():
    threading.Thread(target=timer, name='t1', args=(3,)).start()
    threading.Thread(target=timer, name='t2', args=(3,)).start()
    threading.Thread(target=timer, name='t3', args=(3,)).start()

test_timer()