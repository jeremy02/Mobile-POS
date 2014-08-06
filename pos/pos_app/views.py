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

from django.shortcuts import redirect, render
from django.core.mail import mail_admins

import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.mail import mail_admins

from django.db.models import Q
from datetime import datetime


# Import the models
from pos_app.models import Category,Person,Catalogue,Product,Product_Description,Tax,Sales_line_item,BasicInfo,Sales,Contact

from pos_app.forms import CategoryForm,Sales_line_itemForm
from pos_app.forms import UserForm, UserProfileForm,PersonForm,CatalogueForm,ProductDescriptionForm,ProductForm,PosUsersForm,LoginForm,SalesForm,TaxForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from flynsarmy_paginator.paginator import FlynsarmyPaginator

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
    username_session=''

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
                request.session['username'] = username_session
                request.session.modified = True
                print user

                #login_success ="Welcome "+ login_username + ".You have been successfully Logged In"
                #redirect_to = '/pos_app/sales/'
                return HttpResponse("/pos_app/tax/")
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



    context_dict = {'login_success':login_success,'login_error':login_error,'login_form':login_form,'username_session':username_session}



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
            elif password == "":
                error = "Please enter the password"


            else:
                error='Enter all Password fields to make any changes'


    context_dict = { 'success':success,'error':error}



    return render(request, 'pos_app/form_results.html', context_dict)

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
        if request.method == "GET":
           # product_result = []
            search_text = request.GET['search_text']
            if search_text is not None and search_text != u"":
                search_text = request.GET['search_text']
                product_result = Product.objects.filter(product_name__startswith = search_text)
                #product_result = Product.objects.filter( Q(product_name__istartswith = search_text))
            #else:
                #product_result = []
        return render(request, 'pos_app/search.html', {'product_result':product_result})
        #return render(request, )
        #render the sales page but for now its empty

def sales(request):
        context = RequestContext(request)
        #render the sales form
        if request.POST:
            salesform=SalesForm()
        else:
            salesform=SalesForm()

        #get the id of the last sale to be added to the sales interface and database interaction
        transaction_no = Sales.objects.count()
        transaction_no +=1
        context_dict = {'transaction_no':transaction_no,'salesform':salesform}
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

def sales_list_add(request):
    sales_list_error=''
    sales_list_success=''

    if request.method == 'POST':
        form = Sales_line_itemForm(request.POST)
        if form.is_valid():
            id = request.POST['id']
            transaction = request.POST['transaction-no-duplicate']
            quantity_posted = request.POST['quantity']

            #transaction_no_secret = request.POST['transaction-no-secret']

            #save the form with these default values
            s = Sales(totalsale=0,totalnet = 0,totaltax=0,transaction=transaction)
            s.save()
            #delete all the sales object with transaction as transaction except the first one
            sales_objects_to_keep = Sales.objects.filter(transaction=transaction).order_by('id')[1:]
            #check_if_deleted = Sales.objects.exclude(transaction__in=list(sales_objects_to_keep)).delete()
            for deleted_sale in sales_objects_to_keep:
                deleted_sale.delete()

            #all objects were deleted except one
            #do not save the form yet
            sales_list_fmsave = form.save(commit=False)

            details1 = Product.objects.get(id = id)
            sales = Sales.objects.get(id =transaction)

            #update the quantity of the product
            #get the product description
            prod = Product_Description.objects.get(product__id=1)
            #get the current quantity
            quantity_db = prod.quantity
            #subtract the quantity
            quantity_now = int(quantity_db) - int(quantity_posted)
            #update the quantity
            prod.quantity = quantity_now
            prod.date_out_of_stock = datetime.now()
            prod.save()

            #prod.quantity =- quantity_posted
            #update the quantity and save
            #prod.quantity = quantity_now
            #prod.save()

            sales_list_fmsave.product = details1
            sales_list_fmsave.sales= sales
            check_if_saved = sales_list_fmsave.save()
            if not check_if_saved:
                sales_list_success='The item was added successfully to the sales List!!'
            else:
                sales_list_error='The item was not added to the sales list!!'

        else:
            sales_list_error='Please enter the quantity of product to add the item to the sales list'
    else:
        pass

    context_dict = { 'sales_list_error':sales_list_error,'sales_list_success':sales_list_success}

    return render(request, 'pos_app/formpostresults.html', context_dict)



def complete_sale(request):
    complete_sale_error=''
    complete_sale_success=''

    #complete_sale_success ='Just testing the messages'

    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            transaction = request.POST['transaction']

            totalsale = request.POST['totalsale']
            totalnet = request.POST['totaltax']
            totaltax = request.POST['totaltax']

            #search for the object with id as transaction and id as transaction and change its default values
            sale = Sales.objects.get(id=transaction,transaction=transaction)
            sale.totalsale = totalsale
            sale.totalnet = totalnet
            sale.totaltax = totaltax
            sale.transaction = transaction
            check_if_updated = sale.save()

            if not check_if_updated:
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
            salesList = Sales.objects.all()

            paginator = Paginator(salesList, 1)

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

    context_dict = {'sales_results_error':sales_results_error,'sales_results_success':sales_results_success,'sales_results_warning':sales_results_warning,'sales_list':sales_list,'page_numbers': page_numbers,}

    return render(request, 'pos_app/sales-results.html', context_dict)




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

    results_success=''

    results_success ='Just testing the messages'


    context_dict = {'results_success':results_success}
    # Render the response and return to the client.
    return render(request, 'pos_app/form_results.html', context_dict)

#@login_required(login_url='/pos_app/')
def store(request):
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

    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    if not request.user.is_authenticated():
        #return redirect('/pos_app/' % request.path)
        return HttpResponseRedirect('/pos_app/')

    else:
        if request.method == 'GET':
            #for products that are nearing to be out of stock
            out_of_stock_count = Product_Description.objects.filter(quantity__lte=20).count()
            #for products that are completely to be out of stock
            almost_out_of_stock_count = Product_Description.objects.filter(quantity__lte=20).count()
            #check if products with quantity less than zero exists
            if out_of_stock_count > 0:
                general_success ='Products out of stock exists'
                out_of_stock_list = Product_Description.objects.filter(quantity__lte=20).order_by('date_out_of_stock')
            #check if products with quantity less than twenty exists
            elif out_of_stock_count <= 0:
                general_warning ='Currently there is no product that is completely out of stock.'
            else:
                pass

            if almost_out_of_stock_count > 0:
                general_success_2 ='Products out of stock exists'
                almost_out_of_stock_list = Product_Description.objects.filter(quantity__lte=20).order_by('date_out_of_stock')
            elif almost_out_of_stock_count <= 0:
                general_warning_2 ='Currently there is no product that is nearing to be out of stock.'
            else:
                pass
        else:
            pass

        context_dict = {'general_error':general_error,'general_success':general_success,'general_warning':general_warning,'general_error_2':general_error_2,'general_success_2':general_success_2,'general_warning_2':general_warning_2,'out_of_stock_list':out_of_stock_list,'almost_out_of_stock_list':almost_out_of_stock_list}
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


def paginate_test(request):
    productList = Contact.objects.all()

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