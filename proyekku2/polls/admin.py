from django.contrib import admin
from .models import Provinsi
from .models import Kabkota

# Register your models here.
# admin.site.register(Provinsi)
@admin.register(Provinsi)  # 3. Gunakan decorator untuk mendaftarkan model
class ProvinsiAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)  # Kolom yang bisa difilter



@admin.register(Kabkota)  # 3. Gunakan decorator untuk mendaftarkan model
class KabkotaAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'provinsi', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('provinsi',)  # Kolom yang bisa difilter

# admin.site.register(Provinsi)
# admin.site.register(Kabkota)