import logging
logging.basicConfig(
    filename="retail.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s- %(message)s"
)
class Order:
    PLATFORM="BLINKIT"
    tax_percentage=10

    def __init__(self, order_id, cus_name, price):
        self.order_id=order_id
        self.cus_name=cus_name
        self.price=price
        self.order_placed =False
        self.order_cancelled=False
    def place_order(self):
        if not self.order_placed:
            self.order_placed=True
            logging.info("%s's order is placed successfully",self.cus_name)
        else:
            logging.error("order already placed on order_id %s",self.order_id)
    def cancel_order(self):
        if not self.order_cancelled and self.order_placed:
            self.order_cancelled=True
            logging.info("order id %s is cancelled successfully",self.order_id)
        elif not self.order_placed :
            logging.info("order id %s is not placed",self.order_id)
        else:
            logging.info("order %s is already cancelled ",self.order_id)
    def cal_total_price(self):
        if self.order_cancelled:
            logging.info("Order cancelled")
        tax=(self.price* Order.tax_percentage)/100
        final=self.price+tax
    
        logging.info("order id %s | Price: %s | Tax: %s | Final: %s",self.order_id,self.price,tax,final)
    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info(f"Tax percentage updated to {new_tax}%")
o1 = Order(101, "Usha", 500)

o1.place_order()
o1.cal_total_price()
Order.update_tax_percentage(12)
o1.cal_total_price()
o1.cancel_order()
o1.cal_total_price()