import time
import random
from threading import Thread, current_thread, Condition

'''
# TODO Explain what is condition used for?
A condition is a synchronizatio primitive that allows one 
or more threads to wait until they are notified by another thread.
It combines a lock with the ability to pause thread execution (wait)
and wake up waiting threads (notify).
In this log managerr, the condition coordinates the LogGenerator and Logarchiver:
- The generator waits when the buffer is full (not empty)
- The archiver waits when the buffer is empty
- notify() wakes the other thread when the state changes.

# TODO Explain how does is_empty maintain the state management?
is_empty is a boolean flag that tracks the state of the shared buffer:
- True  = buffer is empty, ready for generator to write
- False = buffer has a log, ready for archiver to read
It acts as a traffic signal: generator checks is_empty before writing,
archiver checks not is_empty before reading. This prevents race conditions
and ensures strict alternation between write and read operations.is_empty is a boolean flag that tracks the state of the shared buffer:
- True  = buffer is empty, ready for generator to write
- False = buffer has a log, ready for archiver to read
It acts as a traffic signal: generator checks is_empty before writing,
archiver checks not is_empty before reading. This prevents race conditions
and ensures strict alternation between write and read operations.
'''
class LogBuffer:
    def __init__(self):
        self.current_log = None
        self.is_empty = True
        self.condition = Condition()

    def write_log(self, log_msg):
        # TODO: 
        pass
        with self.condition:
            # Wait while buffer is not empty (archiver hasn't read yet)
            while not self.is_empty:
                print(f"  [{current_thread().name}] Buffer full, waiting...")
                self.condition.wait()
            
            # Write the log
            print(f"  [{current_thread().name}] Writing: {log_msg}")
            self.current_log = log_msg
            self.is_empty = False
            
            # Notify the archiver that data is ready
            self.condition.notify()

    def archive_log(self):
        # TODO: 
        pass
        with self.condition:
            # Wait while buffer is empty (generator hasn't written yet)
            while self.is_empty:
                print(f"  [{current_thread().name}] Buffer empty, waiting...")
                self.condition.wait()
            
            # Read and process the log
            log_msg = self.current_log
            print(f"  [{current_thread().name}] Archiving: {log_msg}")
            
            # Clear the buffer
            self.current_log = None
            self.is_empty = True
            
            # Notify the generator that buffer is clear
            self.condition.notify()
            return log_msg


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