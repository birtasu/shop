from django.contrib import admin
from .models import *
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ['name', 'email'] # виводить обрані колонки
    list_display = [field.name for field in Subscriber._meta.fields] # виводить всі колонки
    list_filter = ['name'] # додає фільтр по полю name
    search_fields = ['name', 'email'] # додає пошук
    # fields = ['email'] // показувати тільки емейл на сторінці редагування
    # exclude = ['email']  // не показувати емейл на сторінці редагування

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
