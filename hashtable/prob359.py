class Logger:

    def __init__(self):
        
        self.message_timestamps = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.message_timestamps:
            self.message_timestamps[message] = timestamp
            return True
        else:
            last_timestamp = self.message_timestamps[message]
            if timestamp - last_timestamp < 10:
                return False
            else:
                self.message_timestamps[message] = timestamp
                return True
        
