

class Gerate_1():

    def __init__(self):
        self.name = None
        self.price = None
        self.tax = None
        self.total_price = None

    def set_name(self, gerate_name):
        print 'name: %s' % gerate_name
        self.name = gerate_name

    def set_price(self, gerate_price):
        self.price = gerate_price

    def set_tax(self, gerate_tax):
        self.tax = gerate_tax

    def calculate_total_price(self):
        self.total_price = self.price + (self.price * self.tax)
