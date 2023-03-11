from django.contrib import admin
from .models import Customer,Payment,Earning,Game,Payment1,RunningTotal
# Register your models here.
admin.site.register(Customer),
admin.site.register(Payment),
admin.site.register(Game),
admin.site.register(Earning),
admin.site.register(Payment1),
admin.site.register(RunningTotal)