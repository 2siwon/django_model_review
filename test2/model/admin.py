from django.contrib import admin

from .models import (
    Car,
    Manufacturer,
    User,
    Pizza, Topping,
    FacebookUser, InstagramUser,
    Idol, Group, MemberShip,
    Entertainnment,
    Place, Restaurant, Waiter,
    Person)
admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(MemberShip)
admin.site.register(Entertainnment)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)