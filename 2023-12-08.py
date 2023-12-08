class Fruits:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def fruit(self):
        print(f"The price of this {self.name} is {self.price}.")

    def CountFruitPrice(self):
        return self.price * self.weight
    
apple = Fruits("apple", 0.5, 30)
apple.fruit()
TotalPrice = apple.CountFruitPrice()
print(f"The total price for {apple.weight} kg of {apple.name} is {TotalPrice}.")
'''            
apple = Fruits("apple", 30 )
apple.fruit()
banana = Fruits("banana", 15)
banana.fruit()
watermelon = Fruits("watermelon", 50)
watermelon.fruit()
'''