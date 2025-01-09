class CarNumber:
    def __init__(self, number,price,status=False,owner=None):
        self.number = number
        self.price = price
        self.status = status
        self.owner = owner

    def update_status(self, new_status):
        self.status = new_status

    def update_price(self, new_price):
        self.price = new_price