import time
import random
from threading import Thread, current_thread, Condition

'''
# TODO Explain what is condition used for?
# TODO Explain how does is_empty maintain the state management?
'''
class LogBuffer:
    def __init__(self):
        self.current_log = None
        self.is_empty = True
        self.condition = Condition()

    def write_log(self, log_msg):
        # TODO: 
        pass

    def archive_log(self):
        # TODO: 
        pass


class LogGenerator(Thread):
    # TODO:
    pass

class LogArchiver(Thread):
    # TODO:
    pass

def main():
    LOG_COUNT = 5
    buffer = LogBuffer()
    
    # Initialize and start threads
    gen = LogGenerator(buffer, LOG_COUNT)
    arc = LogArchiver(buffer, LOG_COUNT)
    
    gen.start()
    arc.start()
    
    gen.join()
    arc.join()
    print("\nLog Maintenance Complete.")

if __name__ == "__main__":
    main()