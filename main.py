
class FCFS():
    """Class representing a FCFS scheduling algorithm– FirstCome, FirstServed"""

    def __init__(self):
        self.process_list = []
        
    def process_add(self, process_time):
        """add process to processs list"""

        self.process_list.append(process_time)
    
    def avg_process_time_counting(self)-> None:
        """in this method we are counting avarage time of waiting and avarage full time"""
        
        self.avarage_time_of_waiting = 0
        self.avarage_full_time = 0
        
        for i in range(len(self.process_list)):
            self.avarage_time_of_waiting += sum(self.process_list[0:i])
            self.avarage_full_time += sum(self.process_list[0:i+1])

        self.avarage_time_of_waiting /= len(self.process_list)
        self.avarage_full_time /= len(self.process_list)
    
    def process_clean(self):
        """clean processs list"""

        self.process_list = []
        