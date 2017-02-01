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
    def writing_into_sql(cls, filename, num):
        with open(filename, "a") as f:
            f.write("\nBEGIN;\n")
            f.write("TRUNCATE TABLE  mentor_candidates;\n")
            for i in range(num):
                candidate = cls()
                f.write("INSERT INTO \"mentor_candidates\" (first_name, last_name, phone_number, email, city, level, birth_year) VALUES ('%s','%s','%s','%s','%s',%d,%d);\n"
                        % (candidate.first_name, candidate.last_name, candidate.generate_phone_num(),
                           candidate.generate_email(), candidate.city, candidate.level, candidate.birth_year))
            f.write("COMMIT;\n")


def main():
    return Candidate.writing_into_sql('1-fake-mentor-candidates.sql', 10000)

if __name__ == '__main__':
    main()
