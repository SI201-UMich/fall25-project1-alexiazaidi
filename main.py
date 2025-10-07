class data_set_manager():
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}
    
    def load_data(self):
        print(self.file_name)
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
    
    def calculate_species_and_island(self):
        for line in self.data_list:
            line_list = line.split(",")
            species = line_list[1].strip().strip('"')
            island = line_list[2].strip().strip('"')
            species_info = self.data_dict.get(species)
            if species_info:
                species_info["total"] += 1
                islands = species_info["islands"]
                islands[island] = islands.get(island, 0) + 1
            else:
                self.data_dict[species] = {"total": 1, "islands": {island: 1}}
        return self.data_dict
    
    def write_summary(self, output_file = "output.txt"):
        with open(output_file, 'w') as file:
            file.write(f'There are a total of {self.number_of_penguins} penguins in {self.file_name}\n')
            file.write('-' * 40 + '\n')
            order = ["first", "second", "third", "fourth", "fifth", "sixth"]
            count1= 0
            count2= 0
            for species, info in self.data_dict.items():
                file
                file.write(f'{order[count1]} species -> {species}: {info["total"]}\n')
                islands = info.get("islands")
                if islands:
                    for island, count in islands.items():
                        file.write(f' {order[count2]} Island: {island}: {count}\n')
                        count2 +=1
                count1 +=1
                count2 = 0
                file.write('\n')
            file.write('-' * 40 + '\n')
            file.write(f'Species counted: {len(self.data_dict)}\n')

a = data_set_manager("fall25-project1-alexiazaidi/penguins.csv")
a.load_data()
a.calculate_species_and_island()
a.num_penguins()
print(a.number_of_penguins)
print(len(a.data_dict))
print(len(a.data_dict))
a.write_summary()
    
