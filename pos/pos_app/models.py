from django.db import models

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

from django.contrib.auth.models import User


class UserProfile(models.Model):
    """docstring for UserProfile"""
    #This line is required.Links user profile to a user model instance
    user = models.OneToOneField(User)

    #The additional attributes we wish to include
    #website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to = 'profile_images',blank=True)
    phone = models.IntegerField()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
#no_of_catalogues = 0
#catalogue_name=0
class ThukuManager(models.Manager):

    fname = 0
    lname = 0
    def get_queryset(self):
        h1 = super(ThukuManager, self).get_queryset().filter(first_name = 'Thuku')
        for p in h1:
            return u"%s %s" %(p.first_name,p.last_name)
            #print (p.first_name,p.last_name)
        #return '%s' %(h1.first_name)
        #h1 = super(ThukuManager,self).get_queryset().filter(first_name='Thuku')
        #fname = h1.first_name
        #lname = h1.last_name
        #self.__dict__['fname']=fname
        #self.__dict__['lname']=lname
        #return fname,lname

    #def GetFullNames(self):
        #nm = self.get_queryset()
        #return '%s %s'%(fname,lname)
        #return nm[0]+" "+nm[1]
        #pass

    #def get_full_name(self):
        #fullname = '%s %s' %(first_name,last_name)
        #return fullname.strip()
# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        #return super(DahlBookManager, self).get_queryset().filter(first_name='Thuku')
        h1 = super(DahlBookManager, self).get_queryset().filter(first_name = 'thuku')
        for p in h1:
            #print (p.first_name,p.last_name)
            return u"%s %s %s %s" %(p.first_name,p.last_name,p.id_no,p.telephone_number)

class Pos_Users(models.Model):
    #This line is required.Links user profile to a user model instance
    user = models.OneToOneField(User)

    #The additional attributes we wish to include
    id_no = models.IntegerField()
    phone_number = models.IntegerField()




class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES =(
        (MALE,'Male'),

        (FEMALE,'Female'),
        )

    first_name = models.CharField(_('first name'), max_length=200, blank=True)
    last_name = models.CharField(_('last name'), max_length=200, blank=True)
    id_no = models.IntegerField()
    telephone_number = models.IntegerField()
    #age = models.IntegerField (default='18 and over',validators =[MinValueValidator(18), MaxValueValidator(65)])
    #sex = models.CharField(max_length=1,choices=GENDER_CHOICES,default=MALE)
    email_address = models.EmailField(_('email address'), max_length=200)
    #address = models.CharField(_('address'), max_length=30, blank=True)
    #zip_code = models.IntegerField(default=1,blank=False)
    #city = models.CharField(_('city'), max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s" %(self.first_name,self.last_name)

    """
    objects = models.Manager()
    thuku_objects = DahlBookManager()
#
    def save12(self, *args, **kwargs):
        #do_something()hu
        #super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
        #do_something_else()
        email_exists = Person.objects.filter(email_address =self.email_address)
        if self.first_name == "Thuku":
            return 'Yoko shall never have her own blog!'
        elif(email_exists.count() >= 1):
            return u"%s" %("The email address already exists in the database")
        else:
            super(Person, self).save(*args, **kwargs) # Call the "real" save() method.
            return "self.name saved sucessfully"

    def search12(self):
        #return 'Yoko shall never have her own blog!'
        #dir_name = raw_input("What is the name of the directory you want to make");
        #print dir_name
        p = Person.objects.filter(first_name='thuku').get()
        if not p:
            return "No match"
        else:
            return p.last_name
    """
class Catalogue(models.Model):
    catalogue_name = models.CharField(_('catalogue name'), max_length=128, blank=False)
    #date_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" %(self.id,self.catalogue_name)
    """
    def save_catalogue(self, *args, **kwargs):
        no_of_catalogues = Catalogue.objects.all().count()
        #catalogue_name2 = Catalogue.objects.all()
        #print no_of_catalogues
        if no_of_catalogues >=1:
            return "There already exists a catalogue.Only one catalogue exists at a time." 
        else:
            catalogue_save = super(Catalogue, self).save(*args, **kwargs) # Call the "real" save() method.
            if (catalogue_save != False):
                return "The catalogue %s has been created sucessfully" %(self.catalogue_name)
            else:
                return "There is a problem with the system.Please try again later"
    """


class Category(models.Model):
    #category_id=models.AutoField(primary_key=True)
    category_name = models.CharField(_('category name'), max_length=30, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    catalogue= models.ForeignKey(Catalogue)
    #views = models.IntegerField(default=0)
    #likes = models.IntegerField(default=0)
    def __str__(self):
        return u"%s %s" %(self.category_name,self.catalogue)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Africas_Talking_Input(models.Model):
    """
    Represents an SMS from a user through Africa's Talking
    """

    raw_message = models.CharField(max_length=1000, verbose_name="Raw Message")

    timestamp = models.DateTimeField()

    source_telephone = models.CharField(max_length=20, verbose_name="Source Phone Number")

    def __unicode__(self):
        return str(self.source_telephone) + " " + str(self.timestamp)
    
    class Meta:
        verbose_name = "Africa's Talking Input"
        ordering = ['-timestamp']

class Africas_Talking_Output(models.Model):
    """
    Represents an SMS to a user through Africa's Talking
    """

    raw_message = models.CharField(max_length=1000, verbose_name="Raw Message")

    timestamp = models.DateTimeField()

    destination_telephone = models.CharField(max_length=20, verbose_name="Destination Phone Number")

    def __unicode__(self):
        return str(self.destination_telephone) + " " + str(self.timestamp)
    
    class Meta:
        verbose_name = "Africa's Talking Output"
        ordering = ['-timestamp']


class MessageNotSentException(Exception):
    """
    Flag a message that is not sent when the Africa's Talking API is called
    """

    STD_MESSAGE = "This message was not sent!"
    
    def __init__(self, msg=None):
        if msg is not None:
            self.msg = MessageNotSentException.STD_MESSAGE + '; ' + msg
        else:
            self.msg = MessageNotSentException.STD_MESSAGE

    def __str__(self):

        return self.msg\
        
class BasicInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __unicode__(self):
        return "{0} {1}".format(self.name, self.address)

class NearestManager(models.Manager):
    def get_query_set(self):
        return super(NearestManager, self).get_query_set().order_by('-id')

class Contact(models.Model):
    #product = models.ForeignKey(Product)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField( max_length=1000)
    status = models.BooleanField(default=False)


class Contact2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField( max_length=100)
    subject = models.CharField( max_length=100)
    status = models.BooleanField(default=False)

    objects = models.Manager()
    nearest = NearestManager()


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
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)
    date_out_of_stock = models.DateTimeField(auto_now=True)
    tax = models.ForeignKey(Tax)

    #def __str__(self):
        #return u"%s" %(self.product)

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




