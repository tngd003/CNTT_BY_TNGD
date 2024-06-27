from django.contrib import admin

from .models import TheLoai, Sach, ThichSach, ItemSach, ThongTin
# Register your models here.
#
admin.site.register(Sach)
admin.site.register(TheLoai)
admin.site.register(ThichSach)
admin.site.register(ItemSach)
admin.site.register(ThongTin)
