
class FCFS():
    """Class representing a FCFS scheduling algorithm– FirstCome, FirstServed"""

    def __init__(self):
        self.process_list = []
        self.visual_representation = []

    def process_add(self, process_time: int):
        """add process to processs list"""

        self.process_list.append(process_time)

    def process_clean(self):
        """clean processs list"""

        self.process_list = []

    def calculate_visual_representation(self)-> None:
        """in this method we are counting avarage time of waiting and avarage full time"""
        
        self.visual_representation = [[] for i in self.process_list]
        
        for i in range(len(self.process_list)):
            
            for j in range(self.process_list[i]):
                
                self.visual_representation[i].append('И')

                for g in range(i+1, len(self.process_list)):

                    self.visual_representation[g].append('Г')

        return self.visual_representation
    
    def calculate_time(self):
        if len(self.process_list)>0:
            self.avarage_full_time = f"Среднее время ожидания: {round(sum([len(i) for i in self.visual_representation])/len(self.visual_representation), 1)}"
            self.avarage_time_of_waiting = f"Среднее время выполнения: {round(sum([i.count('Г') for i in self.visual_representation])/len(self.visual_representation), 1)}"
        else:
            self.avarage_full_time = "Среднее время ожидания: "
            self.avarage_time_of_waiting = "Среднее время выполнения: "
        return [self.avarage_full_time, self.avarage_time_of_waiting]




    
        


