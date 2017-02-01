import random


class Candidate:

    first_name_list = ['Miklós', 'Tamás', 'Dániel', 'Mateusz', 'Attila', 'Pál',
                       'Sándor', 'Prezmek', 'John', 'Tim', 'Matthew', 'Andy', 'Giancarlo']

    last_name_list = [
        'Beöthy', 'Tompa', 'Salamon', 'Ostafil', 'Molnár', 'Monoczki',
                 'Szodoray', 'Ciacka', 'Carrey', 'Obama', 'Lebron', 'Hamilton', 'Fisichella']

    city_list = ['Budapest', 'Miskolc', 'Krakow', 'Barcelona', 'New York']

    domain_list = ['gmai.com', 'hotmail.com', 'citromail.hu', 'upc.com']

    def __init__(self):
        self.first_name = random.choice(self.first_name_list)
        self.last_name = random.choice(self.last_name_list)
        self.birth_year = random.randint(1960, 1995)
        self.level = random.randint(1, 10)
        self.city = random.choice(self.city_list)
        self.domain = random.choice(self.domain_list)

    def generate_email(self):
        return self.first_name + "." + self.last_name + '@' + self.domain

    def generate_phone_num(self):
        return "+" + "".join(str(random.randint(0, 9)) for i in range(10))

    def generate_record(self):
        return [self.first_name, self.last_name, self.generate_phone_num(), self.generate_email(), self.city, str(
            self.level), str(self.birth_year)]

    @classmethod
    def generate_db(cls, filename, num):
        with open(filename, "w") as f:
            for i in range(num):
                candidate = cls()
                line = candidate.generate_record()
                f.writelines(
                    l + ',' if l != line[-1] else l + '\n' for l in line)


def main():
    return Candidate.generate_db('candidates.txt', 10000)

if __name__ == '__main__':
    main()
