from django.contrib import admin


from .models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession
from .models import Kutuphane, Misafiruye, Ogrenciuye, Oneri, Rezervasyon, Siparis, Siparisurun, Urun            
# Register your models here.



admin.site.register(Kutuphane)
admin.site.register(Misafiruye)
admin.site.register(Ogrenciuye)
admin.site.register(Oneri)
admin.site.register(Rezervasyon)
admin.site.register(Siparis)
admin.site.register(Siparisurun)
admin.site.register(Urun)