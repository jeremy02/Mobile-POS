
from pos_app.models import Category,UserProfile,Person,Catalogue,Product,Product_Description,Tax,Sales_line_item,Pos_Users,Sales
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'firstname','value':'','placeholder' : 'Enter your first name', 'autocomplete' : 'off'}), help_text="Please enter firstname.")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'lastname','value':'', 'placeholder' : 'Enter your last name', 'autocomplete' : 'off'}),  help_text="Please enter lastname.")
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'username','value':'','placeholder' : 'Enter preffered username', 'autocomplete' : 'off'}), help_text="Please enter a username.")
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'email','value':'','placeholder' : 'Please enter the email address.', 'autocomplete' : 'off'}),  help_text="Please enter an email address.")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control' ,'id':'password','value':'','placeholder' : 'Enter preffered password', 'autocomplete' : 'off'}), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password']


class LoginForm(forms.Form):
    login_username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'login_username','value':'','placeholder' : 'Enter your username', 'autocomplete' : 'off'}), help_text="Please enter phone number.")
    login_password = forms.IntegerField(widget=forms.PasswordInput(attrs={'class' : 'form-control' ,'id':'login_password','value':'', 'placeholder' : 'Enter your password.', 'autocomplete' : 'off'}),  help_text="Enter your password")

    class Meta:
        fields = ['login_username','login_password']


class PosUsersForm(forms.ModelForm):
    phone_number= forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'phoneno','value':'','placeholder' : 'Enter your phone number', 'autocomplete' : 'off'}), help_text="Please enter phone number.")
    id_no = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'idno','value':'', 'placeholder' : 'Enter IDNO/Passport No.', 'autocomplete' : 'off'}),  help_text="Please enter an idno.")

    class Meta:
        model = Pos_Users
        fields = ['phone_number','id_no']

class UserProfileForm(forms.ModelForm):
    #website = forms.URLField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'placeholder' : 'Please enter the website', 'autocomplete' : 'off'}),help_text="Please enter your website.", required=False)
    #picture = forms.ImageField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'placeholder' : 'Upload profile image.', 'autocomplete' : 'off'}),help_text="Select a profile image to upload.", required=False)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the phone number.', 'autocomplete' : 'off'}),  help_text="Please enter a phonenumber.")

    class Meta:
        model = UserProfile
        fields = ['phone']

class PersonForm(forms.ModelForm):
    #first_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Please enter the first name.'}),  help_text="Please enter the first name.")
    first_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the first name.' ,'autocomplete' : 'off'}))
    last_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the second name.','autocomplete' : 'off'}))
    #id_no = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the id number'}), initial=0)
    id_no = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the id number' ,'autocomplete' : 'off'}))
    telephone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the phone number.', 'autocomplete' : 'off'}))
    email_address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'placeholder' : 'Please enter the email address.', 'autocomplete' : 'off'}))
    #date_added = forms.CharField(widget=forms.HiddenInput())
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Person
        fields = ['first_name', 'last_name','id_no','telephone_number','email_address']
class CatalogueForm(forms.ModelForm):
    catalogue_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Please enter the catalogue name here.', 'autocomplete' : 'off'}),  help_text="Please enter the catalogue name.")

    class Meta:
        model = Catalogue
        fields = ['catalogue_name']

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Please enter the category name.', 'autocomplete' : 'off'}),  help_text="Please enter the category name.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ['category_name','catalogue']
        exclude = ('catalogue',)

class ProductForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    product_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter the product name.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product name.")
    product_serial_code = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter the product serial code.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product serial code.")

    class Meta:
        model = Product
        fields = ('product_name', 'product_serial_code', 'category')
        exclude = ('category',)

class ProductDescriptionForm(forms.ModelForm):
    buying_price = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter the product buying price.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product buying price.")
    selling_price = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter the product selling price.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product selling price.")
    quantity = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter the product quantity.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product quantity.")
    description = forms.CharField(max_length=128,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Please enter the product description.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product description.")

    COLOR_CHOICES = [(c.id, c.tax_name) for c in Tax.objects.all()]
    COLOR_CHOICES.insert(0, ('', '-- choose a vehicle type first --'))
    
    tax = forms.ChoiceField(choices=COLOR_CHOICES, widget=forms.Select())

    class Meta:
        model = Product_Description
        fields = ('buying_price','selling_price','quantity','description', )
        exclude = ('product',)

class Sales_line_itemForm(forms.ModelForm):
    quantity = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'quantity','value':'','autocomplete':'off','placeholder':'Quantity(Numbers Only).'}))#,  help_text="Please enter the product quantity.")
    subtotal = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'subtotal','value':''}))#,  help_text="Displays the total cash amount.")
    tax_amount = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'tax_amount','value':''}))#,  help_text="Displays the total tax amount.")
    net_total = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'net_total','value':''}))#,  help_text="Displays the net amount.")
    
    #subject = forms.CharField(max_length=100)
    #message = forms.CharField(widget=forms.Textarea(), max_length=100)

    class Meta:
        model = Sales_line_item
        fields = ('quantity', 'subtotal','tax_amount','net_total')
        exclude = ('product','sales',)

class SalesForm(forms.ModelForm):
    totalnet = forms.FloatField(widget=forms.HiddenInput(attrs={'class': 'form-control','id':'totalnet','value':''}))
    totaltax = forms.FloatField(widget=forms.HiddenInput(attrs={'class': 'form-control','id':'totaltax','value':''}))
    totalsale = forms.FloatField(widget=forms.HiddenInput(attrs={'class': 'form-control','id':'totalsale','value':''}))
    transaction = forms.CharField(max_length=100,widget=forms.HiddenInput(attrs={'class': 'form-control','id':'transaction-no-duplicate1','value':'','name':'transaction-no-duplicate1'}))

    class Meta:
        model = Sales
        fields = ('totalnet','totaltax','totalsale','transaction',)
        #exclude = ('product',)

class TaxForm(forms.ModelForm):
    tax_code = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'tax-code','placeholder':'Please enter tax code.', 'autocomplete' : 'off','required':'required'}))
    tax_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'tax-name','placeholder':'Please enter tax name.', 'autocomplete' : 'off','required':'required'}))
    tax_rate = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','id':'tax-rate','placeholder':'Please enter tax rate.', 'autocomplete' : 'off','required':'required'}))
    class Meta:
        model = Tax
        fields = ('tax_name', 'tax_code','tax_rate')
        #exclude = ('date_added',)
"""
class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(), max_length=1000)
    class Meta:
        model = Contact
        fields = ('name', 'email','message')
        exclude = ('product',)


class ContactForm2(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(), max_length=100)

    class Meta:
        model = Contact2
        fields = ('name', 'email','subject','message')
        #exclude = ('product','status',)
"""