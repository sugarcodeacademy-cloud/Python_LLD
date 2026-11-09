class AnalyticsService:
    def record_sales(self, item ,price):
        print(f"[Analytics] sales recorded {item} for rupees {price}")

    def record_cancellation(self, item, price):
        print(f"[Analytics] Cancellation recorded {item} for rupees {price}")
