from home.models import *
import datetime
from django.contrib.auth.models import User


class ChartMaker:
    """ChartMaker."""


    def __init__(self):
        """get_date."""
        self.times = []
        self.product_selling_price = []
        self.product_selling_time = []
        self.product_price_count= 0

    def get_date(self):
        u = User.objects.all()
        for x in u:
            self.times.append(x.date_joined)
        self.times.sort()

    def date_sorter(self, month, **kwargs):
        month_list = []
        for x in self.times:
            if x.month == month:
                month_list.append(x)

        return month_list


    def selling_price(self,month):
        o = Order.objects.all().filter(status="RECIVED")
        for x in o:
            if x.expectedtime.month == month:

                orderItem, created = OrderItem.objects.get_or_create(order=x)
                self.product_price_count += orderItem.product.price

        return self.product_price_count



# setting some variables

c = ChartMaker()
c.get_date()
c.selling_price(1)

a = {
    "January": len(c.date_sorter(1)),
    "February": len(c.date_sorter(2)),
    "March": len(c.date_sorter(3)),
    "April": len(c.date_sorter(4)),
    "May": len(c.date_sorter(5)),
    "June": len(c.date_sorter(6)),
    "July": len(c.date_sorter(7)),
    "August": len(c.date_sorter(8)),
    "Suptember": len(c.date_sorter(9)),
    "October": len(c.date_sorter(10)),
    "Nevember": len(c.date_sorter(11)),
    "December": len(c.date_sorter(12)),
}

b = {"some": 10, "random": 20, "data": 30}
