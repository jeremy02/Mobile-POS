
from pos_app.models import Category,Customer,Suppliers,Catalogue,Product,Product_Description,Tax,Sales_line_item,Pos_Users,Sales,Document,UploadFile,Payment,Payment_Mode
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

class CustomerForm(forms.ModelForm):
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter the phone number.', 'autocomplete' : 'off'}),  help_text="Please enter a phonenumber.")

    class Meta:
        model = Customer
        fields = ['phone']

class CatalogueForm(forms.ModelForm):
    catalogue_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Catalogue Name','id':'catalogue-name','autocomplete':'off'}),help_text="Please enter the catalogue name.")

    class Meta:
        model = Catalogue
        fields = ['catalogue_name']
        exclude = ('date_added',)

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' :'Please enter the category name.','id':'category-name', 'autocomplete' : 'off'}),  help_text="Please enter the category name.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ['category_name','catalogue']
        exclude = ('catalogue',)

class ProductForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    product_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'product-name','placeholder':'Please enter the product name.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product name.")
    product_serial_code = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'product-serial-code','placeholder':'Please enter the product serial code.' , 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product serial code.")

    class Meta:
        model = Product
        fields = ('product_name', 'product_serial_code', 'category')
        exclude = ('category',)

class ProductDescriptionForm(forms.ModelForm):
    buying_price = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'buying-price','placeholder':'Please enter the product buying price.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product buying price.")
    selling_price = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'selling-price','placeholder':'Please enter the product selling price.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product selling price.")
    quantity = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'quantity','placeholder':'Please enter the product quantity.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product quantity.")
    restock_value = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'restock-value','placeholder':'Please enter the restock quantity.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the restock quantity.")
    description = forms.CharField(max_length=128,widget=forms.Textarea(attrs={'class': 'form-control sm','id':'description','rows':'3','placeholder':'Please enter the product description.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the product description.")

    COLOR_CHOICES = [(c.id, c.tax_name) for c in Tax.objects.all()]
    COLOR_CHOICES.insert(0, ('', '-- choose a tax category first --'))
    
    tax = forms.ChoiceField(choices=COLOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control','id':'tax-select'}))

    class Meta:
        model = Product_Description
        fields = ('buying_price','selling_price','quantity','restock_value','description', )
        exclude = ('product','user',)

class Sales_line_itemForm(forms.ModelForm):
    quantity = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','id':'quantity','value':'','autocomplete':'off','placeholder':'Quantity(Numbers Only).'}))#,  help_text="Please enter the product quantity.")
    subtotal = forms.CharField(max_length=100,widget=forms.HiddenInput(attrs={'class': 'form-control','id':'subtotal','value':''}))#,  help_text="Displays the total cash amount.")
    tax_amount = forms.CharField(max_length=100,widget=forms.HiddenInput(attrs={'class': 'form-control','id':'tax_amount','value':''}))#,  help_text="Displays the total tax amount.")
    net_total = forms.CharField(max_length=100,widget=forms.HiddenInput(attrs={'class': 'form-control','id':'net_total','value':''}))#,  help_text="Displays the net amount.")

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

class UploadFileForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField(label='Select a file')

    class Meta:
        model = UploadFile
        fields = ('title', 'file')

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

class PaymentModeForm(forms.ModelForm):
    payment_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control','id':'payment-name','placeholder':'payment name.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the payment name.")


    class Meta:
        model = Payment_Mode
        fields = ('payment_name',)

class PaymentForm(forms.ModelForm):
    amount_paid  = forms.CharField(max_length=128,widget=forms.HiddenInput(attrs={'class': 'form-control','id':'payment_form_amount','placeholder':'Amount Paid.', 'autocomplete' : 'off','required':'required'}),  help_text="Please enter the payment amount.")

    PAYMENT_CHOICES = [(c.id, c.payment_name) for c in Payment_Mode.objects.all()]
    #PAYMENT_CHOICES.insert(0, ('', '-- cHOOS --'))

    payment = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control','id':'payment-select'}))

    class Meta:
        model = Payment
        fields = ('amount_paid','payment',)