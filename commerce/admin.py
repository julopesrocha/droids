from django.contrib import admin

from commerce.models.models import Advertiser, Demand

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ('description', 'delivery_address', 'contact_info', 'advertiser', 'status')

@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    pass