from django.contrib import admin

# Register your models here.
from apartment.models import *

admin.site.register(Block)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(MemberType)
admin.site.register(Relation)
admin.site.register(Designation)
admin.site.register(Complain)
admin.site.register(Amenities)
admin.site.register(TimingSlot)




