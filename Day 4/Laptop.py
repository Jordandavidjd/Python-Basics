# create a class called laptop with 4 attributes like -brand name,model name and price. create 2 objects of the
# laptop class. if dell, 20% discount. if hp,40% discount
class laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def discount(self, brand):
        if brand == "Dell":
            self.d = self.price - (0.2 * self.price)
            print("Price after Discount- ", self.d)
        elif brand == "Hp":
            self.d = self.price - (0.4 * self.price)
            print("Price after Discount- ", self.d)
        else:
            print("No discount")
            print("Final price- ", self.price)


b = input("Enter brand name")
h = input("Enter model name")
p = int(input("Enter price"))
l1 = laptop(b, h, p)
l1.discount(b)
