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

    def selling_price(self, month):
        count = 0
        o = Order.objects.all().filter(status="RECIVED")
        for x in o:
            if x.expectedtime.month == month:

                orderItem = OrderItem.objects.get(order=x)
                count += orderItem.product.price

        return count


# setting some variables

c = ChartMaker()
c.get_date()
print(c.selling_price(10))

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

b = {
    "January": c.selling_price(1),
    "February": c.selling_price(2),
    "March": c.selling_price(3),
    "April": c.selling_price(4),
    "May": c.selling_price(5),
    "June": c.selling_price(6),
    "July": c.selling_price(7),
    "August": c.selling_price(8),
    "Suptember": c.selling_price(9),
    "October": c.selling_price(10),
    "Nevember": c.selling_price(11),
    "December": c.selling_price(12),
}
