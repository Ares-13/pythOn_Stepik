class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print(f"Year: {self.year} and City: {self.city}")


class School(Building):
    amount_pupils = 0

    def __init__(self, amount_pupils, year, city):
        super().__init__(year, city)
        self.amount_pupils = amount_pupils

    def get_info(self):
        print(
            f"Year: {self.year} and City: {self.city} and Pupils: {self.amount_pupils}"
        )


house = Building(2026, "SPB")
school = School(200, 2026, "SPB")

school.get_info()
house.get_info()
