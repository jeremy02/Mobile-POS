from wx.lib.agw import thumbnailctrl
from django.db import models
from PIL import Image

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

from time import time

from django.contrib.auth.models import User

class Customer(models.Model):
    """docstring for UserProfile"""
    #This line is required.Links user profile to a user model instance
    user = models.OneToOneField(User)

    phone = models.IntegerField()


class Suppliers(models.Model):
    """docstring for Suppliers"""
    #This line is required.Links user profile to a user model instance
    user = models.OneToOneField(User)

    phone = models.IntegerField()


class Pos_Users(models.Model):
    #This line is required.Links user profile to a user model instance
    user = models.OneToOneField(User)

    #The additional attributes we wish to include
    id_no = models.IntegerField()
    phone_number = models.IntegerField()


class Catalogue(models.Model):
    catalogue_name = models.CharField(max_length=128, blank=False)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" %(self.id,self.catalogue_name)



class Category(models.Model):
    #category_id=models.AutoField(primary_key=True)
    category_name = models.CharField(_('category name'), max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    catalogue= models.ForeignKey(Catalogue)
    #views = models.IntegerField(default=0)
    #likes = models.IntegerField(default=0)
    def __str__(self):
        return u"%s %s" %(self.category_name,self.catalogue)



class Product(models.Model):
    product_name = models.CharField(_('product name'), max_length=128, blank=False)
    product_serial_code = models.IntegerField()
    category=models.ForeignKey(Category)
    #is product deactivated or still on sale

    def __str__(self):
        return u"%s %s" %(self.product_name,self.product_serial_code)

class Tax(models.Model):
    tax_code = models.CharField(max_length=100)
    tax_rate = models.IntegerField()
    tax_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s %s" %(self.tax_name,self.tax_rate)

class Product_Description(models.Model):
    # This line is required. Links Product Description to a Product model instance.
    product = models.ForeignKey(Product)
    description = models.TextField()
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    restock_value= models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)
    date_out_of_stock = models.DateTimeField(auto_now=True)
    tax = models.ForeignKey(Tax)

    #def __str__(self):
        #return u"%s" %(self.product)

class Payment_Mode(models.Model):
    payment_name = models.CharField(max_length=100)

    def __str__(self):
        return u"%s" %(self.payment_name)

class Sales(models.Model):
    """
    This method ss
    """
    totalsale= models.FloatField(max_length=100)
    totalnet = models.FloatField(max_length=100)
    totaltax = models.FloatField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    transaction = models.CharField(max_length=100)
    users = models.ForeignKey(Pos_Users)

class Payment(models.Model):
    payment_mode = models.ForeignKey(Payment_Mode)
    sales = models.ForeignKey(Sales)
    amount_paid = models.FloatField()

    def __str__(self):
        return u"%s" %(self.id)

class Sales_line_item(models.Model):
    """
    This method
    """    
    product = models.ForeignKey(Product)
    sales = models.ForeignKey(Sales)
    quantity = models.IntegerField(max_length=100)
    subtotal= models.FloatField(max_length=100)    
    tax_amount = models.FloatField(max_length=100)
    net_total = models.FloatField(max_length=100)
    status = models.BooleanField(default=False)


    def __unicode__(self):
        return "{0} {1}".format(self.product, self.net_total)

    def lastreview(self):
        try:
            return self.sales_line_item.order_by('-id')[0]
        except IndexError:
            return None

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class UploadFile(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='.')

    def save(self, size=(200, 200)):
        """
        Save Photo after ensuring it is not blank.  Resize as needed.
        """

        try:
	        from PIL import Image, ImageOps
    	except ImportError:
    	    import Image
    	    import ImageOps

        if not self.id and not self.file:
            return

        super(UploadFile, self).save()

        #filename = self.file.get_filename()
        image = Image.open(self.file)

        image.thumbnail(size, Image.ANTIALIAS)
        image.save(self.file, quality=75)





