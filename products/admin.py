from django.contrib import admin
from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['product', 'author', 'body', 'stars', 'active']
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'description', 'active']

    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active']
