from django.contrib import admin

from .models.brands import Brands
from .models.customer import Customer
from .models.dealers import Dealers
from .models.model import CarModel
from .models.pay import Pay
from .models.sales import Sales
from .models.sellers import Sellers

admin.site.register(Brands)
admin.site.register(Customer)
admin.site.register(Dealers)
admin.site.register(CarModel)
admin.site.register(Pay)
admin.site.register(Sales)
admin.site.register(Sellers)
