class Logger:

    def __init__(self):
        self.time = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(self.time[message])
        if self.time[message] <= timestamp:
            self.time[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)