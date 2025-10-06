class data_set_manager():
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}
    
    def load_data(self):
        with open(self.file_name, 'r') as file:
            headers = []
            my_list = []
            counter = 0
            for line in file:
                if counter == 0:
                    headers.append(line)
                    counter +=1
                else:
                    my_list.append(line)
            self.headers = headers 
            self.data_list = my_list
    
    def num_penguins(self):
        total = 0
        for _ in self.data_list:
            total +=1
        self.number_of_penguins = total
        return total

    
