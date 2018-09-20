

class Gerate():

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

class Zimmer():

    def __init__(self):
        self.gerate_1 = Gerate()
        self.gerate_2 = Gerate()
        self.gerate_3 = Gerate()

    def setNameGerate1(self,gerate_name):
        self.gerate_1.set_name(gerate_name)

    def setNameGerate2(self,gerate_name):
        self.gerate_1.set_name(gerate_name)

    def calculateTotalGerate1(self, price, tax):
        self.gerate_1.set_price(price)
        self.gerate_1.set_tax(tax)
        self.gerate_1.calculate_total_price()

    def showTotalPriceGerate1(self, price, tax):
        self.calculateTotalGerate1(price, tax)
        print "Price Gerate 1: %f" % self.gerate_1.total_price

    def showTotalPriceGerate1_OLD(self):
        print "Price Gerate 1: %f" % self.gerate_1.total_price
