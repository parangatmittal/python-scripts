import time
class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()
    def duration(self):
        return time.time() - self.start_time

timer = ExecutionTime()

# run actual code here

print('Finished in {} seconds.'.format(timer.duration()))
