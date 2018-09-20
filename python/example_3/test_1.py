

class Gerat_1():

    def __init__(self, gerate_name, gerate_price):
        # self.name = gerate_name
        self.price = gerate_price
        self.set_name(gerate_name)

    def set_name(self, gerate_name):
        self.name = gerate_name

class Gerat_2():

    def __init__(self):
        self.name = None
        self.price = None
        self.tax = None

    def set_name(self, gerate_name):
        print 'name: %s' % gerate_name
        self.name = gerate_name

    def set_price(self, gerate_price):
        self.price = gerate_price

    def set_tax(self, gerate_tax):
        self.tax = gerate_tax

    def calculate_total_price():
        self.total_price = self.price * self.tax
