import pulsekit
pulsekit.start_profile()
import threading
import datetime
import time
start = time.time()


def test_proc():
    for i in range(2):
        with pulsekit.CodeBlock("hello"):
            with pulsekit.CodeBlock("bye"):
                time.sleep(.3)
            with pulsekit.CodeBlock("hi"):
                time.sleep(.3)


t = []
for i in range(100):
    t.append(threading.Thread(target=test_proc))
    t[i].start()

for i in t:
    i.join()
