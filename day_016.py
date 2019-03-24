# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
#     record(order_id): adds the order_id to the log
#     get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

class Logs(object):
    def __init__(self, num):
        self.buffer = [None] * num
        self.current = 0
    
    def record(self, logId):
        self.buffer[self.current] = logId
        self.current += 1
        if self.current == len(self.buffer):
            self.current = 0

    def get_last(self, i):
        return self.buffer[self.current-i:]

test = Logs(4)
test.record(1)
test.record(2)
test.record(3)
test.record(4)
print(test.get_last(2))
