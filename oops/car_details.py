


class CarDetails(object):



    def __init__(self, car_mod=None, car_year=None, car_loc=None, car_price=None):
        self.car_mod = car_mod
        self.car_year = car_year
        self.car_loc = car_loc
        self.car_price = car_price

    def mod(self):

        return self.car_mod

    def year(self):
        return self.car_year

    def loc(self):
        return self.car_loc

    def price(self):
        return self.car_price

    def det(self):
        model = self.car_mod
        year = self.car_year
        loc = self.car_loc
        price = self.car_price

        car_inv = "The model", model + " manufactured in the year", str(year) + " with a price of", str(price) + " is located in", loc
        return " ".join(car_inv)




if __name__ == '__main__':


    obj = CarDetails("A1", 2000, "San Francisco", 200000)

    # print obj.mod()
    # print obj.year()
    # print obj.loc()
    # print obj.price()
    # print obj.car_mod
    # print""
    #
    # obj_1 = CarDetails("A2")
    # print obj_1.mod()
    # print obj_1.car_mod

    obj_2 = CarDetails("A2", 2018, "San Jose", 100000)
    print obj_2.det()
