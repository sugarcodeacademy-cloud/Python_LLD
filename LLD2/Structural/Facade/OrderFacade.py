from LLD2.Structural.Facade.Subsystems.Logistics import LogisticsService
from LLD2.Structural.Facade.Subsystems.Analytics import AnalyticsService
from LLD2.Structural.Facade.Subsystems.Inventory import InventoryService
class OrderFacade:
    def __init__(self):
        self.analytics_service = AnalyticsService()
        self.inventory_service = InventoryService()
        self.logistics_service = LogisticsService()
        #self.payment_service = PaymentService()
        #other service also


    def process_order(self, item, price, quantity, customer):
    #1.check inventory --> inventoryService
        if(self.inventory_service.check_stock() == False):
            print("Order Failed: Item out of stock")
            return False;

    #2.Process payment --> paymentService
        if(self.payment_service.process_payment() == False):
            print("Order Failed: Payment declined")
            return False

    #3.update the inventory -> inventoryService
        self.inventory_service.reduce_stock(item, quantity)
    #4.notify seller --> notificationService
        self.notification_service.notify_seller(item, price, quantity)

    #5.Schedule delivery--> logisticsService
        self.logistics_service.schedule_delivery(item, customer)

    #6.send confirmation to user--> notificationService
        self.notification_service.notify_user(customer, item)

    #7.record analytics-->analyticsService
        self.analytics_service.record_sales(item, price, customer)
