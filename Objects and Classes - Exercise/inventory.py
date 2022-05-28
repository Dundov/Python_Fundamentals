class Inventory:
    items = []

    def __init__(self, __capacity: int):
        self.__capacity = __capacity

    def add_item(self, item: str):
        self.item = item
        if self.__capacity > 0:
            Inventory.items.append(self.item)
            self.__capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(Inventory.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"



inventory = Inventory(5)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("Papa")
inventory.add_item("Dani")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)



