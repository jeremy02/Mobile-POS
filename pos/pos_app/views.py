from _threading_local import local
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson

from django.core.urlresolvers import reverse

from django.shortcuts import redirect, render
from django.core.mail import mail_admins

import PIL
from PIL import Image

from PIL import Image, ImageOps

import Image
import ImageOps

import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.mail import mail_admins

from django.db.models import Q
from datetime import datetime,timedelta,date,time

from dateutil import parser

from django.forms.fields import DateField

# Import the models
from pos_app.models import Customer,Pos_Users,Category,Suppliers,Catalogue,Product,Product_Description,Tax,Sales_line_item,Sales,Document,UploadFile,Payment,Payment_Mode

from pos_app.forms import CategoryForm,Sales_line_itemForm,UploadFileForm
from pos_app.forms import UserForm, CustomerForm,CatalogueForm,ProductDescriptionForm,ProductForm,PosUsersForm,LoginForm,SalesForm,TaxForm,DocumentForm,PaymentForm,PaymentModeForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from flynsarmy_paginator.paginator import FlynsarmyPaginator

#for comparison purposes
from django.db.models import F
#aggregation
from django.db.models import Sum,Avg,Count

"""
def index(request):
    return HttpResponse("Rango says: Hello world! <a href='/pos_app/about'>About</a>")
"""


def about(request):
    return HttpResponse("Rango Says: Here is the about page")

def views(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render_to_response('pos_app/views.html', context_dict, context)

def user_register(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    error=''
    success=''
    login_error=''
    login_success=''

    user_form = UserForm()
    posapp_profile_form = PosUsersForm()
    login_form = LoginForm()

    # If it's a HTTP POST, we're interested in processing form data.
    """if request.GET:
        login_form = LoginForm(data=request.GET)

        #login_username = request.GET['login_username']
        #login_password = request.GET['login_password']
        success = "You have been successfully Logged In"
        #login_success='New user was  sucessfully created!'"""
    """
    if request.POST:


        if user_form.is_valid() and posapp_profile_form.is_valid():
            # Imaginable form purpose. Post to admins.

            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            user_profile = posapp_profile_form.save(commit=False)
            user_profile.user = user

            # Now we save the UserProfile model instance.
            user_profile.save()

            success='New user was  sucessfully created!!'

            # Only executed with jQuery form request
            if request.is_ajax():
                return HttpResponse('OK')
                messages.success(request, 'User Sucessfully Created.')
            else:
                # render() a form with data (No AJAX)
                # redirect to results ok, or similar may go here
                pass
        else:
            if first_name == "":
                error = "Please enter your first name"
            elif last_name == "":
                error = "Please enter your last name"
            elif username == "":
                error = "Please enter your username"
            elif email == "":
                error = "Please enter your email address"
            elif phone_number == "":
                error = "Please enter your phone number"
            elif id_no == "":
                error = "Please enter your id no"
            elif password == "":
                error = "Please enter the password"


            else:
                error='Enter all Password fields to make any changes'
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        posapp_profile_form = PosUsersForm()
        login_form = LoginForm()
    """
    # Render the template depending on the context.
    context_dict = {'user_form': user_form, 'posapp_profile_form':posapp_profile_form,'login_form':login_form,'error':error,'success':success,'login_success':login_success,'login_error':login_error}


    # Render the response and return to the client.
    return render_to_response('pos_app/index.html', context_dict, context)

def pos_login(request):
    login_error=''
    login_success=''

    # If it's a HTTP POST, we're interested in processing form data.
    if request.GET:
        login_form = LoginForm(data=request.GET)

        login_username = request.GET['login_username']
        login_password = request.GET['login_password']

        if login_form.is_valid():
            user = authenticate(username=login_username, password=login_password)

            if (not user is None) and (user.is_active):
                login(request, user)
                # Set Session Expiry to 0 if user clicks "Remember Me"
                #request.session['username'] = username_session


                return HttpResponse("/pos_app/settings/")
            else:
                login_error = "There was an error logging you in. Please Try again"
            #login_success = "You have been successfully Logged In"

        else:
            if login_username == "":
                login_error = "Please enter your username/email address"
            elif login_password == "":
                login_error = "Please enter your account password"
            else:
                pass



    context_dict = {'login_success':login_success,'login_error':login_error,'login_form':login_form}#,'username_session':username_session}



    return render(request, 'pos_app/form_results.html', context_dict)


def pos_register(request):
    error=''
    success=''

    # If it's a HTTP POST, we're interested in processing form data.
    if request.POST:
        user_form = UserForm(data = request.POST)
        posapp_profile_form = PosUsersForm(data=request.POST)

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        phone_number=request.POST['phone_number']
        id_no=request.POST['id_no']

        if user_form.is_valid() and posapp_profile_form.is_valid():
            # Imaginable form purpose. Post to admins.

            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            user_profile = posapp_profile_form.save(commit=False)
            user_profile.user = user

            # Now we save the UserProfile model instance.
            user_profile.save()

            success = 'New user was  sucessfully created!!'

            # Only executed with jQuery form request
            """if request.is_ajax():
                #return HttpResponse('OK')
                success = 'User Sucessfully Created.'
            else:
                # render() a form with data (No AJAX)
                # redirect to results ok, or similar may go here
                pass"""
        else:
            if first_name == "":
                error = "Please enter your first name"
            elif last_name == "":
                error = "Please enter your last name"
            elif username == "":
                error = "Please enter your username"
            elif email == "":
                error = "Please enter your email address"
            elif phone_number == "":
                error = "Please enter your phone number"
            elif id_no == "":
                error = "Please enter your id no"
            else :
                error = "Please enter the password"
    else:
        "Please check your internet connection"



    context_dict = { 'success':success,'error':error}



    return render(request, 'pos_app/form_results.html', context_dict)
"""
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'pos_app/index.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
"""
def user_login(request):
    #obtain the context for the user's request
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        #Gather the username and password provided by the user
        #This information is obtained form the login form
        username = request.POST['username']
        password = request.POST['password']

        ## Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username,password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            #Is the account active? It could have been disabled
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request,user)
                return HttpResponseRedirect('/pos_app/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango Account is disabled")

        else:
            #Bad login details were provided,so we cant log in the user.
            print "Invalid login details:{0},{1}".format(username,password)
            return HttpResponse("Invalid login details were provided")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render_to_response('pos_app/login.html',{},context)


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    #return HttpResponse("Since you're logged in, you can see this text!")
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.

    return HttpResponseRedirect('/pos_app/')


def add_person(request):
    # Get the context from the request.
    context = RequestContext(request)

    registered = False

    # A HTTP POST?
    if request.method == 'POST':
        form = PersonForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Update our variable to tell the template registration was successful.
            registered = True

            # Now call the index() view.
            # The user will be shown the homepage.
            #return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = PersonForm()


    #this allow us to view the table for the most recently added persons ordered by the date or time added
    # Query for categories - add the list to our context dictionary.
    users_list = Person.objects.order_by('-date_added')[:5]
    #context_dict = {'categories': category_list}

    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    #for category in category_list:
     #   category.url = category.name.replace(' ', '_')

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).


    context_dict = {'form': form, 'users': users_list, 'registered': registered}
    return render_to_response('pos_app/user_register.html',context_dict , context)

def testing(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    return render_to_response('pos_app/testing.html', {}, context)

def add_catalogue(request):
    # Get the context from the request.
    context = RequestContext(request)

    catalogue_added = False

    #catalogue_registered = Category.objects.all().count()

    #check that the catalogue should be only one in the database


    # A HTTP POST?
    if request.method == 'POST':
        form = CatalogueForm(request.POST)

        # Have we been provided with a valid form?

        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            catalogue_added = True

            # Now call the index() view.
            # The user will be shown the homepage.
            #return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors

    else:
        # If the request was not a POST, display the form to enter details.
        form = CatalogueForm()

    #get the list of Catalogues in the system

    #catalogues_list = Catalogue.objects.order_by('id')[:5]
    # Query for catalogues - add the list to our context dictionary.
    catalogue_list = Catalogue.objects.order_by('id')[:5]

    #get the total number of catalogues in the system
    category_number = Category.objects.all().count()

    # The following two lines are new.
    # We loop through each catalogue returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for catalogue in catalogue_list:
        catalogue.url = catalogue.catalogue_name.replace(' ', '_')

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).

    context_dict = {'form': form, 'catalogues': catalogue_list,'catalogue_added': catalogue_added,'category_number':category_number}
    #context_dict = {'form': form, 'catalogues': catalogues_list}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('pos_app/catalogue.html', context_dict, context)

"""
    # This function Changes underscores in the name provided to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
"""
def decode_url(name):
    url = name.replace('_',' ')
    return url


def catalogue(request, catalogue_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # call the function to decode the name in the url
    catalogue_name = catalogue_name = decode_url(catalogue_name_url)

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'catalogue_name': catalogue_name}

    #this handles the category form displaying and saving the data
    category_added = False
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            cat_form = form.save(commit=False)

            # Retrieve the associated Catalogue object so we can add it.
            # Wrap the code in a try block - check if the category actually exists!
            try:
                cat = Catalogue.objects.get(catalogue_name=catalogue_name)
                cat_form.catalogue = cat
            except Catalogue.DoesNotExist:
                # If we get here, the category does not exist.
                # Go back and render the add category form as a way of saying the category does not exist.
                #return render_to_response('rango/add_category.html', {}, context)
                pass

            # Also, create a default value for the number of views.
            #page.views = 0

            # With this, we can then save our new model instance.
            cat_form.save()
            category_added = True

            # Now that the page is saved, display the category instead.
            #return catalogue(request, category_name_url)
        else:
            print form.errors
    else:
        form = CategoryForm()

    context_dict['form'] = form
    #find if the catalogue exists and then list the associated categories
    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        catalogue = Catalogue.objects.get(catalogue_name=catalogue_name)

        # Retrieve all of the associated categories.
        # Note that filter returns >= 1 model instance.
        categories = Category.objects.filter(catalogue=catalogue)

        # Adds our results list to the template context under name categories.
        context_dict['categories'] = categories

        # Retrieve all of the associated categories.
        # Note that filter returns >= 1 model instance.
        recent_categories = Category.objects.filter(catalogue=catalogue).order_by('date_added')[:5]

        # Adds our results list to the template context under name categories.
        context_dict['recent_categories'] = recent_categories

        # We loop through each category returned, and create a URL attribute.
        # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
        for category in categories:
            category.url = category.category_name.replace(' ', '_')

        # We also add the catalogue object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['catalogue'] = catalogue

    except Catalogue.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('pos_app/category.html', context_dict, context)


def add_product(request, category_name_url):
    context = RequestContext(request)

    # call the function to decode the name in the url
    category_name = decode_url(category_name_url)

    context_dict = {'category_name': category_name}

    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        product_form = ProductForm(data=request.POST)
        product_desc_form = ProductDescriptionForm(data=request.POST)

        # If the two forms are valid...
        if product_form.is_valid() and product_desc_form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            product = product_form.save(commit=False)

            # Retrieve the associated Category object so we can add it.
            # Wrap the code in a try block - check if the category actually exists!
            category = Category.objects.get(category_name=category_name)
            product.category = category      
            # With this, we can then save our new model instance.
            product.save()

            # Now sort out the Product Description instance.
            # Since we need to set the product description ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            prod_desc = product_desc_form.save(commit=False)
            #show the relationship with the product
            prod_desc.product = product

            #show the relationship with tax
            tax_input = request.POST['tax']
            #tax = product_desc_form.cleaned_data['tax']
            tax = Tax.objects.get(id = tax_input)
            prod_desc.tax = tax

            # Now we save the Product Description model instance.
            prod_desc.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print product_form.errors, product_desc_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        product_form = ProductForm()
        product_desc_form = ProductDescriptionForm()

    # Render the template depending on the context.

    context_dict['product_form'] = product_form
    context_dict['product_desc_form'] = product_desc_form


    #find if the category exists and then list the associated products
    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(category_name=category_name)

        # Retrieve all of the associated products.
        # Note that filter returns >= 1 model instance.
        products = Product.objects.filter(category=category)
        products = Product_Description.objects.filter(product=products)

        # Adds our results list to the template context under name product.
        context_dict['products'] = products

        # Retrieve all of the associated products but latest five products added.
        # Note that filter returns >= 1 model instance.
        recent_products = Product.objects.filter(category=category)[:5]
        recent_products = Product_Description.objects.filter(product=recent_products)[:5]
        #recent_products = Product.objects.filter(category=category)[:5]

        # Adds our results list to the template context under name categories.
        context_dict['recent_products'] = recent_products

        # We loop through each category returned, and create a URL attribute.
        # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
        #for product in products:
            #product.url = product.product.product_name.replace(' ', '_')

        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass


    #context_dict = {'category_name_url': category_name_url,'category_name': category_name, 'product_form' :product_form, 'product_desc_form' :product_desc_form}

    return render_to_response( 'pos_app/products.html',context_dict,context)



"""This is for searching  a product when making a sale"""
def suggest_product(request):
    search_success = ''
    search_warning = ''
    search_error = ''

    if request.method == "GET":
        search_text = request.GET['search_text']

        if search_text =="":
            search_error = 'Please enter the product to search'
        else:
            #search_success = 'Yes theres text.'
            product_result = Product.objects.filter(product_name__startswith = search_text)
            if product_result:
                search_success = 'Yes the product exists.'
            else:
                search_warning = "The product doesn't exist.Search again."

    else:
        pass

    context_dict = {'product_result':product_result,'search_error':search_error,'search_success':search_success,'search_warning':search_warning}
    # Render the response and return to the client.
    return render(request, 'pos_app/search.html', context_dict)

def sales(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        #render the sales form
        if request.POST:
            salesform=SalesForm()
            paymentForm= PaymentForm()
        else:
            salesform=SalesForm()
            paymentForm= PaymentForm()

        #get the id of the last sale to be added to the sales interface and database interaction
        transaction_no = Sales.objects.count()
        transaction_no +=1
        context_dict = {'transaction_no':transaction_no,'salesform':salesform,'paymentForm':paymentForm}
    #sales_id = sales_id__set.count()
    return render_to_response('pos_app/sales.html', context_dict, context)




#This is for returning the product details when making a sale
def product_details(request):
    #render the sales line item form
    if request.POST:
        form = Sales_line_itemForm(request.POST)
    else:
        form = Sales_line_itemForm()

    if request.is_ajax():
         # If it was a GET
         if request.method == 'GET':
             search_text = request.GET['search_text']
             if search_text is not None and search_text != u"":
                 search_text = request.GET['search_text']
                 details = Product_Description.objects.filter( Q(product__id__iexact = search_text))
                 #transaction_id = Sales.objects.count()
                 #transaction_id +=1
                 #sales_id = sales_id__set.count()


    context_dict = { 'details':details,'form':form}



    return render(request, 'pos_app/search.html', context_dict)

def check_quantity(request):
    #just for json responses
    error_code=''
    #store_hell

    if request.method == 'GET':
        #get these values as you type the quantity
        id = request.GET['id']
        sale_quantity = request.GET['quantity']
        #check if the product has such quantity
        product_exists = Product_Description.objects.filter(product__id=id, quantity__gte=sale_quantity).exists()
        #quantity_db = product.quantity
        #get the remaining quantity and pass it to the templates
        p1 = Product_Description.objects.filter(product__id=id).get()
        product = p1.quantity
        if product_exists:
            error_code=1
        else:
            error_code=0

    else:
        pass

    context_dict = {'error_code':error_code,'product':product}
    return HttpResponse(simplejson.dumps(context_dict), mimetype='application/javascript')

    return render(request, 'pos_app/search.html', context_dict)

def check_cat_prod_exist(request):
    #just for json responses
    error_code=''
    #store_hell

    if request.method == 'GET':
        #get these values as you type the into the inputs
        catalogue_name = request.GET['catalogue_name']
        category_name = request.GET['category_name']
        product_name = request.GET['product_name']
        product_serial_code = request.GET['product_serial_code']
        if catalogue_name:
            catalogue_exists= Catalogue.objects.filter(catalogue_name__icontains=catalogue_name).exists()
            if catalogue_exists:
                error_code = 1
            else:
                error_code = 2
        elif category_name:
            category_exists= Category.objects.filter(category_name__icontains=category_name).exists()
            if category_exists:
                error_code = 3
            else:
                error_code = 4
        elif product_name:
            product_exists= Product.objects.filter(product_name__icontains=product_name).exists()
            if product_exists:
                error_code = 5
            else:
                error_code = 6
        elif product_serial_code:
            product_exists= Product.objects.filter(product_serial_code__icontains=product_serial_code).exists()
            if product_exists:
                error_code = 7
            else:
                error_code = 8
        else:
            pass
    else:
        pass


    context_dict = {'error_code':error_code}
    return HttpResponse(simplejson.dumps(context_dict), mimetype='application/javascript')

    return render(request, 'pos_app/store_management.html', context_dict)

def sales_list_add(request):
    #sales_list_error=''
    #sales_list_success=''

    error_code = ''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:

        if request.method == 'POST':
            form = Sales_line_itemForm(request.POST)
            #print request.POST
            if form.is_valid():
                id = request.POST['id']
                transaction = request.POST['transaction-no-duplicate']
                quantity_posted = request.POST['quantity']

                username = request.POST['username']
                userid = request.POST['user-id']

                #get the current user
                current_user = Pos_Users.objects.get(user__username=username)
                #print current_user
                #save the form with these default values
                s = Sales(totalsale=0,totalnet = 0,totaltax=0,transaction=transaction,users=current_user)
                s.save()
                #delete all the sales object with transaction as transaction except the first one

                sales_objects_to_keep = Sales.objects.filter(transaction=transaction,users=current_user)[1:]
                #delete all the sales object except the first one
                for deleted_sale in sales_objects_to_keep:
                    deleted_sale.delete()



                #all objects were deleted except one
                #do not save the form yet
                sales_list_fmsave = form.save(commit=False)

                details1 = Product.objects.get(id = id)
                sales = Sales.objects.get(id =transaction)

                #update the quantity of the product
                #get the product description
                prod = Product_Description.objects.get(product__id=details1.id)

                #get the current quantity
                quantity_db = prod.quantity
                #subtract the quantity
                quantity_now = int(quantity_db) - int(quantity_posted)
                #update the quantity
                prod.quantity = quantity_now
                #prod.date_out_of_stock = datetime.now()
                prod.save()

                sales_list_fmsave.product = details1
                sales_list_fmsave.sales= sales
                check_if_saved = sales_list_fmsave.save()
                if not check_if_saved:
                    error_code = 1
                else:
                    error_code = 2


            else:
                #sales_list_error='Please enter the quantity of product to add the item to the sales list'
                #error_code = 3
                pass

        else:
            pass

    context_dict = { 'error_code':error_code}

    return HttpResponse(simplejson.dumps(context_dict), mimetype='application/javascript')

    return render(request, 'pos_app/search.html', context_dict)



def complete_sale(request):
    complete_sale_error=''
    complete_sale_success=''

    #complete_sale_success ='Just testing the messages'

    if request.method == 'POST':
        form = SalesForm(request.POST)
        paymentform = PaymentForm(request.POST)
        if form.is_valid():
            transaction = request.POST['transaction']

            totalsale = request.POST['totalsale']
            totalnet = request.POST['totalnet']
            totaltax = request.POST['totaltax']
            username = request.POST['username']
            userid = request.POST['user-id']
            username = request.POST['username']
            payment_id = request.POST['payment']

            #get the payment method
            payment_mode = Payment_Mode.objects.get(id=payment_id)
            #print payment

            #search for the object with id as transaction and id as transaction and change its default values
            sale = Sales.objects.get(id=transaction,transaction=transaction)
            sale.totalsale = totalsale
            sale.totalnet = totalnet
            sale.totaltax = totaltax
            sale.transaction = transaction
            check_if_updated = sale.save()

            #save the payment details
            payment = paymentform.save(commit=False)
            payment.payment_mode = payment_mode
            payment.sales = sale

            check_if_paid = payment.save()

            if not check_if_updated and not check_if_paid:
                complete_sale_success='The sale has been succesfully completed.'
            else:
                complete_sale_error='There is an error in completing the sale.Please try again!!'

        else:
            complete_sale_error="There's an error while performing the sales.No items are in the list"
    else:
        pass


    context_dict = {'complete_sale_error':complete_sale_error,'complete_sale_success':complete_sale_success}

    return render(request, 'pos_app/formpostresults.html', context_dict)

#get the sales results and show to the client
def sales_results(request):
    sales_results_error=''
    sales_results_success=''
    sales_results_warning=''
    sales_list = ''

    #sales_results_error ='Just testing the messages'
    if request.method == 'GET':
        #sales_results_success ='Its a get'
        sales_count = Sales.objects.all().count()
        if sales_count > 0:
            sales_results_success ='There are sales that have been made'

            #start of pagination function
            salesList = Sales.objects.all().order_by('-id')

            paginator = Paginator(salesList, 10)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                sales_list = paginator.page(page)
            except PageNotAnInteger:
                sales_list = paginator.page(1)
            except EmptyPage:
                sales_list = paginator.page(paginator.num_pages)


            startPage = max(page - 2, 1)
            if startPage <= 3: startPage = 1
            endPage = page + 2 + 1
            if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
            page_numbers = [n for n in range(startPage, endPage) \
                    if n > 0 and n <= paginator.num_pages]
            #End of pagination function
        else:
            sales_results_warning ='No sales have been made so far in the system.'
    else:
        #sales_results_error ='Not a get'
        pass

    context_dict = {'sales_results_error':sales_results_error,'sales_results_success':sales_results_success,'sales_results_warning':sales_results_warning,'sales_list':sales_list,'page_numbers': page_numbers}

    return render(request, 'pos_app/sales-results.html', context_dict)


def making_sales(request):
    final_sales_error=''
    final_sales_success=''
    final_sales_warning=''
    sales_list = ''

    #sales_results_error ='Just testing the messages'
    if request.method == 'GET':
        #sales_results_success ='Its a get'
        category_count = Category.objects.all().count()
        if category_count > 0:

            #start of pagination function
            categoryList = Category.objects.all()

            paginator = Paginator(categoryList, 10)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                category_list = paginator.page(page)
            except PageNotAnInteger:
                category_list = paginator.page(1)
            except EmptyPage:
                category_list = paginator.page(paginator.num_pages)

            #End of pagination function

            final_sales_success='There are categories and products that exist'
        else:
            final_sales_warning ='No categories have been created so far in the system.'
    else:
        pass


    context_dict = {'final_sales_error':final_sales_error,'final_sales_success':final_sales_success,'final_sales_warning':final_sales_warning,'category_list':category_list}

    return render(request, 'pos_app/search.html', context_dict)

def tax(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)


    if request.POST:
        tax_form = TaxForm()
    else:
        tax_form = TaxForm()

    context_dict = {'tax_form': tax_form}


    # Render the response and return to the client.
    return render_to_response('pos_app/tax-registration.html', context_dict, context)

def tax_registration(request):
    general_error=''
    general_success=''
    general_warning=''
    tax_name =''
    tax_code=''
    tax_rate=''

    #general_error ='Just testing the messages'

    if request.method == 'POST':
        form = TaxForm(request.POST)
        #general_success ='method is a post'
        tax_name = request.POST['tax_name']
        tax_code = request.POST['tax_code']
        tax_rate = request.POST['tax_rate']

        if form.is_valid():
            #general_success ='form is valid'
            #save the form and the tax details
            tax_form_save = form.save()
            if tax_form_save:
                general_success ='The tax category was successfully added.Thank you.'
            else:
                general_warning ='Sorry.The tax category was not saved.Please try again.'

        else:
            test = tax_rate.isnumeric()

            if tax_name =="":
                general_error ='Please enter the name of tax category'
            elif tax_code =="":
                general_error ='Please enter a code for the tax category'
            elif tax_rate == "":
                general_error ='Please enter the rate of the tax category'
            elif test == False:
                general_error ="The tax rate must be a number"
            else:
                pass


    else:
        general_error ='Not a post.Refresh the app.'

    context_dict = {'general_error':general_error,'general_success':general_success,'general_warning':general_warning}

    return render(request, 'pos_app/form_results.html', context_dict)

def get_tax_categories(request):

    tax_results_success=''
    tax_results_warning=''
    tax_results_error=''

    if request.method == 'GET':
        #tax_results_success = 'Its a get method'

        tax_cat_list = Tax.objects.all()

        if tax_cat_list.count() > 0:
            tax_results_success = 'Tax categories exist.'
            #get the data and add pagination

            paginator = Paginator(tax_cat_list, 2)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                tax_list = paginator.page(page)
            except PageNotAnInteger:
                tax_list = paginator.page(1)
            except EmptyPage:
                tax_list = paginator.page(paginator.num_pages)


            startPage = max(page - 2, 1)
            if startPage <= 3: startPage = 1
            endPage = page + 2 + 1
            if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
            page_numbers = [n for n in range(startPage, endPage) \
                    if n > 0 and n <= paginator.num_pages]


        else:
            tax_results_warning = 'Sorry.No tax categories exist yet.'
    else:
        #tax_results_error ='Not a get.Server error.'
        pass



    context_dict = {'tax_results_success':tax_results_success,'tax_results_error':tax_results_error,
                    'tax_results_warning':tax_results_warning,'tax_list':tax_list,'page_numbers': page_numbers}
    # Render the response and return to the client.
    return render(request, 'pos_app/form_results.html', context_dict)

#@login_required(login_url='/pos_app/')
def store(request):
    """
    #for products that are completely out of stock
    general_error=''
    general_success=''
    general_warning=''
    out_of_stock_list=''
    #for products that are nearing to be out of stock
    general_error_2=''
    general_success_2=''
    general_warning_2=''
    almost_out_of_stock_list=''
    """

    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        # A HTTP POST?
        if request.method == 'POST':
            catalogue_form = CatalogueForm(request.POST)
            category_form = CategoryForm(request.POST)
            product_form = ProductForm(data=request.POST)
            product_desc_form = ProductDescriptionForm(data=request.POST)

        else:
            # If the request was not a POST, display the form to enter details.
            catalogue_form = CatalogueForm()
            category_form = CategoryForm()
            product_form = ProductForm()
            product_desc_form = ProductDescriptionForm()
        #else:
            #pass

        context_dict = {'catalogue_form':catalogue_form,'category_form':category_form,'product_form':product_form,'product_desc_form':product_desc_form}
    # Render the response and return to the client.
    return render_to_response('pos_app/store_management.html', context_dict, context)

def stock_update(request):

    stock_results_success=''
    stock_results_error=''
    stock_results_warning=''
    total_stock = ''
    product_id = ''

    if request.POST:
        #stock_results_success ='Its a post'
        total_stock = request.POST['total-stock']
        product_id = request.POST['product-id']
        get_product = Product_Description.objects.filter(product__id=product_id).count()
        #return get_product.buying_price
        if get_product > 0:
            #stock_results_success ='The product exists'
            product = Product_Description.objects.get(product__id=product_id)
            product.quantity = total_stock
            product.date_out_of_stock = datetime.now()
            stock_updated = product.save()
            if not stock_updated:
                stock_results_success ='The product was succesfully updated'
            else:
                stock_results_warning ='There is an error in updating the stock'
        else:
            stock_results_error ='Sorry the product does not exist.Try later.'

    else:
        #stock_results_error ='Not a post'
        pass



    context_dict = {'stock_results_success':stock_results_success,'stock_results_error':stock_results_error,'stock_results_warning':stock_results_warning}
    # Render the response and return to the client.
    return render(request, 'pos_app/form_results.html', context_dict)

@login_required
def check_stock(request):
    #check_stock_error=''
    check_stock_success=''
    check_stock_warning=''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')
    else:
        # A HTTP GET?
        if request.method == 'GET':
            #for products that are nearing to be out of stock.i.e the quantity is nearing to be 10 to reach restock value
            nearing_out_of_stock = Product_Description.objects.extra(where=["quantity - restock_value < 10"]).order_by('date_out_of_stock')

            #if such a product exists where quantity-restock_value is less than ten
            if nearing_out_of_stock.exists():
                check_stock_success = 'Products nearing out of stock exists.'
            else:
                check_stock_warning = 'Currently there is no product that is nearing to be out of stock.'
        else:
            pass


    context_dict = {'check_stock_success':check_stock_success,'check_stock_warning':check_stock_warning,'nearing_out_of_stock':nearing_out_of_stock}

    return render(request, 'pos_app/store-results.html', context_dict)


@login_required
def check_stock_out(request):
    check_stock_success_out=''
    check_stock_warning_out=''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')
    else:
        # A HTTP GET?
        if request.method == 'GET':
            #for products that are completely to be out of stock i.e quantity is less than the restock value
            out_of_stock = Product_Description.objects.filter(quantity__lte=F('restock_value'))
            if out_of_stock.exists():
                check_stock_success_out= 'Products completely out of stock exists.'

            else:
                check_stock_warning_out = 'Currently there is no product that is be out of stock.'

        else:
            pass


    context_dict = {'out_of_stock':out_of_stock,'check_stock_success_out':check_stock_success_out,'check_stock_warning_out':check_stock_warning_out}

    return render(request, 'pos_app/store-results.html', context_dict)

def get_catalogues(request):
    catalogue_error=''
    catalogue_success=''
    catalogue_warning=''

    if request.method == 'GET':
         # If it was a GET
         catalogue_count = Catalogue.objects.count()

         if catalogue_count > 0:
             catalogue_success = 'Catalogues exist.'

             catalogue_list = Catalogue.objects.all()
             paginator = Paginator(catalogue_list, 2)

             page = request.GET.get('page')
             try:
                 page = int(request.GET.get('page', '1'))
             except ValueError:
                 page = 1

             try:
                 catalogue = paginator.page(page)
             except PageNotAnInteger:
                 catalogue = paginator.page(1)
             except EmptyPage:
                 catalogue = paginator.page(paginator.num_pages)

         else:
             catalogue_warning = 'Currently there are no catalogues  that exist.Add one to use the app.'
    else:
        pass

    context_dict = {'catalogue_error':catalogue_error,'catalogue_success':catalogue_success,'catalogue_warning':catalogue_warning,'catalogue':catalogue}

    return render(request, 'pos_app/store-results.html', context_dict)

def get_categories(request):
    category_error=''
    category_success=''
    category_warning=''

    if request.method == 'GET':
        #category_success='A get'

        category_list = Category.objects.all()
        if category_list:
            paginator = Paginator(category_list, 2)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                category = paginator.page(page)
            except PageNotAnInteger:
                category = paginator.page(1)
            except EmptyPage:
                category = paginator.page(paginator.num_pages)

            category_success = 'Catalogues exist.'

        else:
            category_warning = 'Currently there are no categories that exist.Add one to use the app.'
    else:
        pass
        #category_error = "Yes"
    context_dict = {'category_error':category_error,'category_success':category_success,'category_warning':category_warning,'category':category}

    return render(request, 'pos_app/store-results.html', context_dict)

def get_products(request):
    product_error=''
    product_success=''
    product_warning=''

    if request.method == 'GET':
        #product_success='A get'

        product_list = Product.objects.all()
        if product_list:

            paginator = Paginator(product_list, 10)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                product = paginator.page(page)
            except PageNotAnInteger:
                product = paginator.page(1)
            except EmptyPage:
                product = paginator.page(paginator.num_pages)

            product_success = 'Products exist.'
        else:
            product_warning = 'Currently there are no products that exist.Add one to use the app.'
    else:
        pass
        #product_error = "Not a get.Fatal error"
    context_dict = {'product_error':product_error,'product_success':product_success,'product_warning':product_warning,'product':product}

    return render(request, 'pos_app/store-results.html', context_dict)

#adding catalogues
def catalogue_add(request):
    store_error=''
    store_success=''
    store_warning=''

    if request.method == 'POST' and request.POST:
        #check if we are adding a catalogue
        if 'catalogue_name' in request.POST:
            catalogue_form = CatalogueForm(data=request.POST)
            catalogue_name=request.POST['catalogue_name']

            if catalogue_form.is_valid():
                # Save the catalogue's form data to the database.
                form = catalogue_form.save()
                store_success = 'New catalogue was successfully created!!'

            else:
                if catalogue_name == "":
                    store_error = "Please enter the catalogue name"
                else:
                    pass

        #check if we are adding a category
        elif 'category_name' in request.POST:
            category_form = CategoryForm(data=request.POST)
            #the posted data
            category_name=request.POST['category_name']
            catalogue_id=request.POST['catalogue-cat-id']

            if category_form.is_valid():
                #get the associated catalogue
                cat = Catalogue.objects.get(id=catalogue_id)
                # This delays saving the model until we're ready to avoid integrity problems.
                form = category_form.save(commit=False)

                form.catalogue = cat
                # Save the catalogue's form data to the database.
                form.save()

                #was the form saved??
                store_success = 'New catalogue was successfully created!!'
            else:
                if category_name == "":
                    store_error = "Please enter the category name"
                else:
                    pass

        #check if we are adding a product
        elif 'product_name' in request.POST:
            # Attempt to grab information from the raw form information.
            # Note that we make use of both ProductForm and ProductDescForm.
            product_form = ProductForm(data=request.POST)
            product_desc_form = ProductDescriptionForm(data=request.POST)
            #the posted data
            product_cat_id = request.POST['product-cat-id']

            # If the two forms are valid...
            if product_form.is_valid() and product_desc_form.is_valid():
                # This time we cannot commit straight away.
                # Not all fields are automatically populated!
                product = product_form.save(commit=False)

                # Retrieve the associated Category object so we can add it.
                # Wrap the code in a try block - check if the category actually exists!
                category = Category.objects.get(id=product_cat_id)
                product.category = category
                # With this, we can then save our new model instance.
                product.save()

                # Now sort out the Product Description instance.
                # Since we need to set the product description ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                prod_desc = product_desc_form.save(commit=False)
                #show the relationship with the product
                prod_desc.product = product

                #show the relationship with tax
                tax_input = request.POST['tax']
                #tax = product_desc_form.cleaned_data['tax']
                tax = Tax.objects.get(id = tax_input)
                prod_desc.tax = tax

                # Now we save the Product Description model instance.
                prod_desc.save()

                # Update our message to tell the product addition was successful.

                store_success ='The product was succesfully added'


            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
            else:
                store_error ='The forms have errors.Please try again later.'


        else:
            pass
    else:
        pass

    context_dict = {'store_error':store_error,'store_success':store_success,'store_warning':store_warning}

    return render(request, 'pos_app/store-results.html', context_dict)



def delete_catalogue(request):
    store_error=''
    store_success=''
    store_warning=''

    #store_warning = 'Testing'

    if request.method == 'POST':
        catalogue_id=request.POST['id']

        #get the catalogue
        cat = Catalogue.objects.filter(id__exact =catalogue_id)
        #catalogue_name = cat.catalogue_name
        confirm_delete = cat.delete()

        if not confirm_delete:
            store_success = 'The catalogue was successfully deleted.'
        else:
            store_error='The catalogue was not deleted.Try later.'

    else:
        #store_error = "Not a post.Fatal error"
        pass

    context_dict = {'store_error':store_error,'store_success':store_success,'store_warning':store_warning}

    return render(request, 'pos_app/store-results.html', context_dict)

def product_edit(request):
    edit_code = ''

    if request.method == 'GET':
        productId = request.GET['productId']
        productName = request.GET['productName']
        productSerial = request.GET['productSerial']
        productStock = request.GET['productStock']
        productSale = request.GET['productSale']

        #get the product
        product= Product.objects.get(id=productId)

        productDesc= Product_Description.objects.get(product__id=productId)

        if productName != "":
            product.product_name = productName
            saved = product.save()
            if not saved:
                edit_code = 'name1'
            else:
                edit_code = 'name0'
        else:
            productDesc.quantity = productStock
            saved = productDesc.save()
            if not saved:
                edit_code = 'stock1'
            else:
                edit_code = 'stock0'

    else:
        pass

    context_dict = {'edit_code':edit_code}
    return HttpResponse(simplejson.dumps(context_dict), mimetype='application/javascript')

    return render(request, 'pos_app/store-results.html', context_dict)



def list(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    # Handle file upload

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image = UploadFileForm(request.FILES['file'])

            form.save()
            return HttpResponseRedirect('/pos_app/list/')
    else:
        form = UploadFileForm()
        documents = UploadFile.objects.all()
    context_dict = {'form': form,'documents': documents}
    return render_to_response('pos_app/upload.html', context_dict, context)


    """if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/pos_app/list/')
    else:
        form = UploadFileForm()
        documents = UploadFile.objects.all()
    """
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect('/pos_app/list/')
    else:
        form = DocumentForm() # A empty, unbound form
        # Load documents for the list page
        documents = Document.objects.all()
        # Render list page with the documents and the form
    """
    #return render_to_response('pos_app/upload.html',{'documents': documents, 'form': form}, context_instance=RequestContext(request))

def store_summary(request):
    catalogue_code=''
    category_code=''
    product_code=''

    catalogue_count=0
    category_count=0
    product_count=0

    if request.method == 'GET':
        #checking if catalogue exists
        cat_exist = Catalogue.objects.exists()
        #checking if category exists
        category_exist = Category.objects.exists()
        #checking if product exists
        product_exist = Product.objects.exists()

        #does the catalogue exist??
        if cat_exist:
            catalogue_code= 1
            catalogue_count = Catalogue.objects.all().count()
            #print catalogue_count

        #does the product exist??
        if product_exist:
            product_code= 1
            product_count = Product.objects.all().count()
            #print product_count

        if category_exist:
            category_code = 1
            category_count = Category.objects.all().count()
            #print category_count

        else:
            pass
    else:
        pass

    context_dict = {'catalogue_count':catalogue_count,'catalogue_code':catalogue_code,'category_code':category_code,'category_count':category_count,'product_code':product_code,'product_count':product_count}
    return HttpResponse(simplejson.dumps(context_dict), mimetype='application/javascript')

    return render(request, 'pos_app/store-results.html', context_dict)

def paginate_test(request):
    productList = Category.objects.all()

    paginator = Paginator(productList, 3)

    page = request.GET.get('page')
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    startPage = max(page - 2, 1)
    if startPage <= 3: startPage = 1
    endPage = page + 2 + 1
    if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
    page_numbers = [n for n in range(startPage, endPage) \
            if n > 0 and n <= paginator.num_pages]


    results_success=''

    results_success ='Just testing the messages'


    context_dict = {'results_success':results_success,'products': products,'page_numbers': page_numbers}
    # Render the response and return to the client.
    return render(request, 'pos_app/form_results.html', context_dict)

def reports(request):
    context = RequestContext(request)

    context_dict = {}
    #sales_id = sales_id__set.count()
    return render_to_response('pos_app/reports.html', context_dict, context)

def all_sales_reports(request):
    sales_error=''
    sales_success=''
    sales_warning=''

    sales=''
    page_numbers=''

    if request.method == 'GET':
        #store_success = 'Its a get.'
        sales_count = Sales.objects.all().count()

        if sales_count > 0:
            pages = request.GET['pages']
            #if the filter has been clicked pick the startdates and end dates
            if "startDate" in request.GET:
                startDate = request.GET['startDate']
                endDate = request.GET['endDate']

                #convert the strings to date format
                parsedstart = parser.parse(startDate)
                parsedend = parser.parse(endDate)

                """
                #format the last day to be upto midnight
                fld = DateField()
                start = fld.to_python(parsedstart)
                end = fld.to_python(parsedend)+timedelta(days=1)
                """
                #get the smallest and largest time for the days
                min_date_time = datetime.combine(parsedstart, time.min)
                max_date_time = datetime.combine(parsedend, time.max)

                salesList = Sales.objects.filter(date_added__range=[min_date_time, max_date_time])

            #otherwise just show the results without filtering
            else:
                salesList = Sales.objects.all()
            #paginate all the results
            paginator = Paginator(salesList, pages)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                sales = paginator.page(page)
            except PageNotAnInteger:
                sales = paginator.page(1)
            except EmptyPage:
                sales = paginator.page(paginator.num_pages)

            startPage = max(page - 2, 1)
            if startPage <= 3: startPage = 1
            endPage = page + 2 + 1
            if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
            page_numbers = [n for n in range(startPage, endPage) \
                    if n > 0 and n <= paginator.num_pages]

            sales_success = 'There are sales.'

        else:
            sales_warning = 'Sorry.No sales have been made in the system.'

    else:
        #store_error = "Not a get.Fatal error"
        pass

    context_dict = {'sales_success':sales_success,'sales_warning':sales_warning,'sales':sales}

    return render(request, 'pos_app/reports-results.html', context_dict)

def sales_by_product(request):
    sales_error=''
    sales_by_product_success=''
    sales_warning=''

    if request.method == 'GET':
        #sales_by_product_success = 'Its a get.'
        sales_count = Sales.objects.all().count()
        if sales_count > 0:

            pages = request.GET['pages']
            #if the filter has been clicked pick the startdates and end dates
            if "startDate" in request.GET:

                startDate = request.GET['startDate']
                endDate = request.GET['endDate']

                #convert the strings to date format
                parsedstart = parser.parse(startDate)
                parsedend = parser.parse(endDate)

                #get the smallest and largest time for the days
                min_date_time = datetime.combine(parsedstart, time.min)
                max_date_time = datetime.combine(parsedend, time.max)

                salesByProductList = Sales_line_item.objects.filter(sales__date_added__range=[min_date_time, max_date_time]).values('product','product__product_name').annotate(tax = Sum('tax_amount'),net =  Sum('net_total'),total = Sum('subtotal'),quantity = Sum('quantity'))

            #otherwise just show the results without filtering
            else:
                salesByProductList = Sales_line_item.objects.values('product','product__product_name').annotate(tax = Sum('tax_amount'),net =  Sum('net_total'),total = Sum('subtotal'),quantity = Sum('quantity'))

            paginator = Paginator(salesByProductList, 10)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)


            startPage = max(page - 2, 1)
            if startPage <= 3: startPage = 1
            endPage = page + 2 + 1
            if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
            page_numbers = [n for n in range(startPage, endPage) \
                    if n > 0 and n <= paginator.num_pages]

            sales_by_product_success = 'sales exist.'
        else:
            sales_warning = 'Sorry.No sales have been made in the system.'

    else:
        #store_error = "Not a get.Fatal error"
        pass

    context_dict = {'sales_by_product_success':sales_by_product_success,'sales_warning':sales_warning,'page_numbers': page_numbers,'results':results}

    return render(request, 'pos_app/reports-results.html', context_dict)

def user_sales_reports(request):
    sales_error=''
    sales_by_user_success=''
    sales_warning=''

    if request.method == 'GET':
        #sales_by_user_success = 'Its a get.'
        sales_count = Sales.objects.all().count()
        if sales_count > 0:
            salesByUserList = Sales.objects.values('users__user__username','users__user__id').annotate(tax = Sum('totalsale'),net =  Sum('totalnet'),total = Sum('totalsale'))
            #print salesByUserList

            paginator = Paginator(salesByUserList, 10)

            page = request.GET.get('page')
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)


            startPage = max(page - 2, 1)
            if startPage <= 3: startPage = 1
            endPage = page + 2 + 1
            if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
            page_numbers = [n for n in range(startPage, endPage) \
                    if n > 0 and n <= paginator.num_pages]

            sales_by_user_success = 'sales exist.'

        else:
            sales_warning = 'Sorry.No sales have been made in the system.'

    else:
        #store_error = "Not a get.Fatal error"
        pass

    context_dict = {'sales_by_user_success':sales_by_user_success,'sales_warning':sales_warning,'page_numbers': page_numbers,'results':results}

    return render(request, 'pos_app/reports-results.html', context_dict)

def get_open_close_stock(request):
    sales_error=''
    stock_open_close_success=''
    sales_warning=''
    if request.method == 'GET':
        # Query for products - add the list to our context dictionary.
        prodCount = Product_Description.objects.all().count()
        #if the product exists??
        if prodCount > 0:
             #Query all the products and
            #for each product calculate the total quantity sold

            product_stock = Product_Description.objects.all()
            for item in product_stock:
                #calculation of total products sold per product
                sales_item = Sales_line_item.objects.filter(product=item.product).aggregate(sold_stock=Sum('quantity'))
                #obtain the sold stock
                item.sold_stock =sales_item['sold_stock']
                #add the sold stock to the product quantity to get the opening stock
                item.opening_stock = (int(item.sold_stock)+int(item.quantity))
                #print item.opening_stock

                stock_open_close_success='The products exist'
        #if the product doesnt exist??
        else:
            sales_warning ='The products exist'
    else:
        pass
    context_dict = {'stock_open_close_success':stock_open_close_success,'sales_warning':sales_warning,'product_stock':product_stock}

    return render(request, 'pos_app/reports-results.html', context_dict)

#the settings views template
def settings(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        #render the sales form
        if request.POST:
            payment_form=PaymentModeForm()
            tax_form = TaxForm()
        else:
            payment_form=PaymentModeForm()
            tax_form = TaxForm()

        context_dict = {'payment_form':payment_form,'tax_form':tax_form}
    return render_to_response('pos_app/settings.html', context_dict, context)

def settings_post(request):
    settings_success = ''
    settings_warning = ''
    settings_error = ''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        #render the sales form
        if request.POST:
            if 'payment_name' in request.POST:
                form = PaymentModeForm(request.POST)
                if form.is_valid():
                    form.save()
                    settings_success = 'The payment mode has been saved.'
                else:
                    settings_warning = 'Please enter the payment mode name.'
            elif 'tax_name' in request.POST:
                form = TaxForm(request.POST)
                tax_name = request.POST['tax_name']
                tax_code = request.POST['tax_code']
                tax_rate = request.POST['tax_rate']

                if form.is_valid():
                    #general_success ='form is valid'
                    #save the form and the tax details
                    tax_form_save = form.save()
                    if tax_form_save:
                        settings_success='The tax category was successfully added.Thank you.'
                    else:
                        settings_warning ='Sorry.The tax category was not saved.Please try again.'

                else:
                    test = tax_rate.isnumeric()

                    if tax_name =="":
                        settings_error ='Please enter the name of tax category'
                    elif len(tax_name) < 2:
                        settings_error ='The category must be more than 2 characters.'
                    elif tax_code =="":
                        settings_error ='Please enter a code for the tax category'
                    elif tax_rate == "":
                        settings_error ='Please enter the rate of the tax category'
                    elif test == False:
                        settings_error ="The tax rate must be a number"
                    else:
                        pass

            else:
                settings_error = 'Error!!!Please refresh the current page.'
        else:
            pass
        context_dict = {'settings_success':settings_success,'settings_warning':settings_warning,'settings_error':settings_error}
    return render(request, 'pos_app/settings-results.html', context_dict)

def filter_test(request):
    settings_success = ''
    settings_warning = ''
    settings_error = ''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        if request.method=="GET":
            startDate = request.GET['startDate']
            endDate = request.GET['endDate']

            sales= Sales.objects.filter(date_added__range=(startDate, endDate))

            #samples = Sales.objects.filter(date_added__gte=datetime.date(startDate),date_added__lte=datetime.date(endDate))

            print sales

        else:
            print "Its a runtime error"

    context_dict = {}
    return render(request, 'pos_app/settings-results.html', context_dict)

def payments_reports(request):
    payments_success = ''
    payments_warning = ''
    payments_error = ''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        if request.method=="GET":
            #startDate = request.GET['startDate']
            #endDate = request.GET['endDate']

            payments_count = Payment.objects.all().count()

            if payments_count > 0:
                pages = request.GET['pages']
                #if the filter has been clicked pick the startdates and end dates
                if "startDate" in request.GET:
                    startDate = request.GET['startDate']
                    endDate = request.GET['endDate']

                    #convert the strings to date format
                    parsedstart = parser.parse(startDate)
                    parsedend = parser.parse(endDate)

                    #get the smallest and largest time for the days
                    min_date_time = datetime.combine(parsedstart, time.min)
                    max_date_time = datetime.combine(parsedend, time.max)

                    paymentsList = Payment.objects.filter(sales__date_added__range=[min_date_time, max_date_time])

                #otherwise just show the results without filtering
                else:
                    paymentsList = Payment.objects.all()

                paginator = Paginator(paymentsList, 10)

                page = request.GET.get('page')
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1

                try:
                    payments = paginator.page(page)
                except PageNotAnInteger:
                    payments = paginator.page(1)
                except EmptyPage:
                    payments = paginator.page(paginator.num_pages)

                """

                startPage = max(page - 2, 1)
                if startPage <= 3: startPage = 1
                endPage = page + 2 + 1
                if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
                page_numbers = [n for n in range(startPage, endPage) \
                        if n > 0 and n <= paginator.num_pages]

                """

                payments_success = 'There are payments.'

            else:
                payments_warning = 'Sorry.No sales have been made in the system.'

        else:
            pass

    context_dict = {'payments_success':payments_success,'payments_warning':payments_warning,'payments':payments}

    return render(request, 'pos_app/reports-results.html', context_dict)

def payment_by_mode(request):
    payment_by_mode_success = ''
    payments_warning = ''
    payments_error = ''

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        if request.method=="GET":
            #startDate = request.GET['startDate']
            #endDate = request.GET['endDate']

            payments_count = Payment.objects.all().count()

            if payments_count > 0:
                paymentsList = Payment.objects.values('payment_mode__payment_name').annotate(amount = Sum('amount_paid'),no_of_transactions = Sum('id'))

                payment_by_mode_success = 'There are payments.'

            else:
                payments_warning = 'Sorry.No sales have been made in the system.'

        else:
            pass

    context_dict = {'payment_by_mode_success':payment_by_mode_success,'payments_warning':payments_warning,'paymentsList':paymentsList}

    return render(request, 'pos_app/reports-results.html', context_dict)


