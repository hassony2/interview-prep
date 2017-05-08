class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self.value):
        if(self.items):
            dequeud_value = self.items[0]
        else:
            dequeud_value = None
        return dequeud_value
