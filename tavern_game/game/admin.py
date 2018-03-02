from django.contrib import admin

from .models import Person, Ration, BarPurchase, RichPerson

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class RationAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'person', 'value')

class BarPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'person', 'value')

class RichPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'person', 'value')

admin.site.register(Person, PersonAdmin)
admin.site.register(Ration, RationAdmin)
admin.site.register(BarPurchase, BarPurchaseAdmin)
admin.site.register(RichPerson, RichPersonAdmin)
