import random

class REDQueue:
    def __init__(self, max_size, min_threshold, max_threshold, drop_probability):
        self.max_size = max_size
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.drop_probability = drop_probability
        self.queue = []

    def enqueue(self, packet):
        if len(self.queue) < self.max_size:
            self.queue.append(packet)
        else:
            self.random_early_drop(packet)

    def random_early_drop(self, packet):
        queue_length = len(self.queue)
        drop_probability = 0.0

        if queue_length < self.min_threshold:
            drop_probability = 0.0
        elif queue_length >= self.min_threshold and queue_length < self.max_threshold:
            drop_probability = (queue_length - self.min_threshold) / float(self.max_threshold - self.min_threshold)
        else:
            drop_probability = 1.0

        if random.random() < drop_probability:
            self.queue.pop(0)
            self.queue.append(packet)
        else:
            print("Packet dropped!",random.random())

# Example usage:
red_queue = REDQueue(max_size=5, min_threshold=2, max_threshold=4, drop_probability=0.2)

for packet in range(10):
    red_queue.enqueue(packet)
    print( red_queue.queue )
#print( red_queue )
## The changes include using the float function for proper division in Python 2 and using the print statement without parentheses. Adjust the code further based on your specific requirements.
