from django.db import models

# Create your models here.
class SHOP(models.Model):
	shop_id=models.AutoField(primary_key=True, unique=True)  # shop ID		
	shop_name=models.CharField(max_length=256, blank=False, null=False) # shop name
	shop_address=models.CharField(max_length=256, blank=True, null=True)  # shop address
	shop_longitude=models.CharField(max_length=256, blank=True, null=True)  # shop longitude
	shop_latitude=models.CharField(max_length=256, blank=True, null=True)  # shop latitude
	shop_NTN=models.IntegerField(blank=True, null=True)  # shop NTN number
	shop_type=models.CharField(max_length=256,blank=False, null=False )  # shop Type
	shop_description=models.CharField(max_length=1000, blank=True, null=True)  # shop description

class CATEGORY(models.Model):
	category_name=models.CharField(max_length=256, blank=False, null=False)  # category name
	category_description=models.CharField(max_length=1000, blank=True, null=True)  # category description
	category_id=models.AutoField(primary_key=True, unique=True)  # category ID
	category_promotion=models.CharField(max_length=256,blank=True, null=True)  # category promotion
	category_discount=models.IntegerField( blank=True, null=True)  # category discount


class SUBCAT(models.Model):
	subcategory_parentid=models.ForeignKey(CATEGORY, on_delete=models.CASCADE, blank=True, null=True)  # SUBCATegory's parent (category)ID
	subcategory_subcatparentid=models.ForeignKey("self",on_delete=models.CASCADE, blank=False, null=False)  # SUBCATegory's parent (subcategory)ID
	subcategory_name=models.CharField(max_length=256, blank=False, null=False)  # SUBCATegory name
	subcategory_description=models.CharField(max_length=1000, blank=True, null=True)  # SUBCATegory description
	subcategory_id=models.AutoField(primary_key=True, unique=True, default=False)  # SUBCATegory  ID
	subcategory_promotion=models.CharField(max_length=1000, blank=True, null=True)  # SUBCATegory promotion
	subcategory_discount=models.IntegerField(blank=True, null=True)  # SUBCATegory discount



class ITEM(models.Model):
	item_name=models.CharField(max_length=256, blank=False, null=False) # item name
	item_id=models.AutoField(primary_key=True, unique=True)  # Item ID
	item_cat_id=models.ForeignKey(CATEGORY, on_delete=models.CASCADE, blank=False, null=False)  # Item's category id
	item_subcat_id=models.ForeignKey(SUBCAT, on_delete=models.CASCADE, blank=True, null=True)  # Item's sub-category ID
	item_description=models.CharField(max_length=1000, blank=True, null=True) # item description
	item_image= models.FileField( default=False)
	item_tag=models.CharField(max_length=256, blank=True, null=True) # item tag
	item_discount=models.IntegerField( blank=True, null=True) # item Discount
	item_price=models.IntegerField( blank=False, null=False,   default=False)
	#item_promotion=models.CharField(max_length=256,blank=True, null=True)  # item promotion
	item_PPU=models.IntegerField( blank=False, null=False,  default=False)  # price per Unit
	item_unit=models.CharField( max_length=16,blank=False, null=False)  # Unit
	item_avg_rating=models.IntegerField( blank=True, null=True,  default=True)  # item rating
	item_quantity=models.IntegerField( blank=False, null=False,   default=False)  # Item quantity

class ITEM_RATING(models.Model):
	Item_id=models.ForeignKey(ITEM, on_delete=models.CASCADE, blank=False, null=False)
	rating=models.IntegerField( blank=True, null=True,  default=True)  # item rating
	itemrating_review=models.CharField(max_length=512, blank=True, null=True)

class ITEM_PROMOTION(models.Model):
	Item_id=models.ForeignKey(ITEM, on_delete=models.CASCADE, blank=False, null=False)
	Promotion_name=models.CharField(max_length=256, blank=True, null=True)
	Promotion_description=models.CharField(max_length=1000, blank=True, null=True)
	Promotion_start_date=models.DateTimeField()
	Promotion_end_date=models.DateTimeField()

class SUBCAT_PROMOTION(models.Model):
	Subcat_id=models.ForeignKey(ITEM, on_delete=models.CASCADE, blank=False, null=False)
	Subcat_Promo_name=models.CharField(max_length=256, blank=True, null=True)
	Subcat_Promo_description=models.CharField(max_length=1000, blank=True, null=True)
	Subcat_Promo_start_date=models.DateTimeField()
	Subcat_Promo_end_date=models.DateTimeField()

class CAT_PROMOTION(models.Model):
	Cat_id=models.ForeignKey(ITEM, on_delete=models.CASCADE, blank=False, null=False)
	Cat_Promo_name=models.CharField(max_length=256, blank=True, null=True)
	Cat_Promo_description=models.CharField(max_length=1000, blank=True, null=True)
	Cat_Promo_start_date=models.DateTimeField()
	Cat_Promo_end_date=models.DateTimeField()

class shop_cat_relation(models.Model):
	catid=models.ForeignKey(CATEGORY, on_delete=models.CASCADE, blank=False, null=False)
	shopid=models.ForeignKey(SHOP, on_delete=models.CASCADE, blank=False, null=False)