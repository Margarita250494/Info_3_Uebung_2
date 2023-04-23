class people_in_Germany:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"{self.name}: {self.population}"


my_list = [people_in_Germany('Berlin', 3644826), people_in_Germany('Bayern', 13076721),
           people_in_Germany('Bremen', 682986), people_in_Germany('Hamburg', 1841179)]
sorted_list = sorted(my_list, key=lambda x: x.population)

if __name__ == '__main__':
    for obj in sorted_list:
        print(obj)
