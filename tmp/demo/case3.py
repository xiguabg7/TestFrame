class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具名称是{self.name},占地面积是{self.area}"


class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f"户型{self.type}\n" \
               f"面积{self.area}\n" \
               f"free_area{self.free_area}\n" \
               f"item_list{self.item_list}\n"

    def add_item(self, item):
        if self.free_area < item.area:
            print("面积不够")
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)

house = House("大平层", 120)
print(house)
house.add_item(bed)
print(house)
