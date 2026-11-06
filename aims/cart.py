MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return -1

    def get_discounted_total(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Discount percent must be between 0 and 100")
        return self.total_cost() * (1 - percent / 100)

    def sort_by_title(self):
        """Sắp xếp các DVD theo tiêu đề tăng dần."""
        self.items.sort(key=lambda item: item.title)

    def sort_by_cost(self):
        """Sắp xếp các DVD theo giá tăng dần."""
        self.items.sort(key=lambda item: item.cost)

    def print_cart(self):
        """In danh sách DVD và tổng tiền của giỏ hàng."""
        print("***********************CART***********************")
        print("Ordered Items:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
