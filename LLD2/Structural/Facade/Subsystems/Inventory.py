class InventoryService:

    def check_stock(item):
        print(f"[Inventory] Checking stock for: {item}");
        return True; # Simplified — always in stock for demo

    def reduce_stock(item,quantity):
        print(f"[Inventory] Reduced stock of {item} by {quantity}");

    def restore_stock(item, quantity):
        print(f"[Inventory] Restored stock of {item} by {quantity}");
