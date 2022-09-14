from progress.bar import Bar
import time

bar = Bar('Processing', max=10)
for i in range(10):
    time.sleep(0.5)
    bar.next()
bar.finish()
