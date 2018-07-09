from django.contrib import admin
from .models import SUBCAT, SHOP, CATEGORY, ITEM, ITEM_RATING, ITEM_PROMOTION, SUBCAT_PROMOTION, CAT_PROMOTION, shop_cat_relation

# Register your models here.

admin.site.register(SHOP)
admin.site.register(CATEGORY)
admin.site.register(ITEM)
admin.site.register(SUBCAT)
admin.site.register(ITEM_RATING)
admin.site.register(ITEM_PROMOTION)
admin.site.register(SUBCAT_PROMOTION)
admin.site.register(CAT_PROMOTION)
admin.site.register(shop_cat_relation)