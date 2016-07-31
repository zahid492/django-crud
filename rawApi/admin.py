from django.contrib import admin

# Register your models here.
from rawApi.models import State,City,Country,Zip

admin.site.register(State)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Zip)