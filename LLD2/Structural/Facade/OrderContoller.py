from LLD2.Structural.Facade.OrderFacade import OrderFacade


class OrderController:
    def __init__(self):
        self.order_facade = OrderFacade()

    def process_order(self, item, price, quantity, customer):
        self.order_facade.process_order(item, price, quantity, customer)

    def small_order(self):
        pass

    def quick_delivery(self):
        pass