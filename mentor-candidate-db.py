import random


class Candidate:

    first_name_list = ['Miklós', 'Tamás', 'Dániel', 'Mateusz', 'Attila', 'Pál',
                       'Sándor', 'Prezmek', 'John', 'Tim', 'Matthew', 'Andy', 'Giancarlo']

    last_name_list = [
        'Beöthy', 'Tompa', 'Salamon', 'Ostafil', 'Molnár', 'Monoczki',
                 'Szodoray', 'Ciacka', 'Carrey', 'Obama', 'Lebron', 'Hamilton', 'Fisichella']

    city_list = ['Budapest', 'Miskolc', 'Krakow', 'Barcelona', 'New York']

    domain_list = ['gmai.com', 'hotmail.com', 'citromail.hu', 'upc.com']

    level_list = [1, 10]

    birth_year_list = [1960, 1995]

    def __init__(self, first_name, last_name, birth_year, level, city, domain):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.level = level
        self.city = city
        self.domain = domain

    def generate_email(self):
        return self.first_name + "." + self.last_name + '@' + self.domain

    def generate_phone_num(self):
        return "+" + "".join(str(random.randint(0, 9)) for i in range(10))

    def generate_record(self):
        return [self.first_name, self.last_name, self.generate_phone_num(), self.generate_email(), self.city, str(
            self.level), str(self.birth_year)]

    @classmethod
    def generate_candidate(cls):
        return cls(
            random.choice(cls.first_name_list), random.choice(
                cls.last_name_list), random.randint(
                    cls.birth_year_list[0], cls.birth_year_list[1]),
                  random.randint(cls.level_list[0], cls.level_list[1]), random.choice(cls.city_list), random.choice(cls.domain_list))

    @classmethod
    def generate_db(cls, filename, num):
        with open(filename, "w") as f:
            for i in range(num):
                candidate = cls.generate_candidate()
                line = candidate.generate_record()
                f.writelines(
                    l + ',' if l != line[-1] else l + '\n' for l in line)


def main():
    return Candidate.generate_db('candidates.txt', 10000)

if __name__ == '__main__':
    main()
