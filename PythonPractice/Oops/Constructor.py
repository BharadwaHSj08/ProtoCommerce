class Constructor:

    def __init__(self,name,Address,town):
        self.name = name
        self.Address = Address
        self.town = town

    def Data(self):
        s= self.name +" " + "Address is"+ " " + self.Address + " "  + self.town
        return s

c= Constructor("Bharat","Veml","Nsp")
print(c.Data())

