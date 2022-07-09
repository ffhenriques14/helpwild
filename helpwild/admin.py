from django.contrib import admin
from .models import Customer ,Donate, Quiz, Comments

# class donates(admin.ModelAdmin):
#    filter_horizontal = ('donation',) 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Donate)
admin.site.register(Quiz)
admin.site.register(Comments)



