from django.contrib import admin  # type: ignore
from .models import Game, Buyer, News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'data', 'time',)
    list_filter = ('title', 'data',)
    search_fields = ('title', 'data',)
    list_per_page = 20


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    list_filter = ('size', 'cost',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'balance',)
    list_filter = ('balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)
