from django.conf.urls import patterns, url

#from django.conf.urls.defaults import patterns, url
#from django.views.generic.simple import direct_to_template

from pos_app import views

urlpatterns = patterns('',
    url(r'^$', views.user_register, name='user_register'),
    url(r'^about/$', views.about, name='about'),    
    url(r'^views/$', views.views, name='views'),
    url(r'^catalogue/(?P<catalogue_name_url>\w+)$', views.catalogue, name='catalogue'),
    url(r'^category/(?P<category_name_url>\w+)$', views.add_product, name='category'),
    #url(r'^register/$', views.register, name='register'),
    url(r'^pos_register/$', views.pos_register, name='pos_register'),
    url(r'^pos_login/$', views.pos_login, name='pos_login'),
    url(r'^sales_list_add/$', views.sales_list_add, name='sales_list_add'),
    url(r'^complete_sale/$', views.complete_sale, name='complete_sale'),
    url(r'^sales_results/$', views.sales_results, name='sales_results'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^tax/$', views.tax, name='tax'),
    url(r'^tax_registration/$', views.tax_registration, name='tax_registration'),
    url(r'^get_tax_categories/$', views.get_tax_categories, name='get_tax_categories'),
    url(r'^store/$', views.store, name='store'),
    #check the products that are nearing to be out of stock
    url(r'^check_stock/$', views.check_stock, name='check_stock'),
    #check the products that are completely out of stock
    url(r'^check_stock_out/$', views.check_stock_out, name='check_stock_out'),
    #list these in the store management dashboard
    url(r'^get_catalogues/$', views.get_catalogues, name='get_catalogues'),
    url(r'^delete_catalogue/$', views.delete_catalogue, name='delete_catalogue'),
    url(r'^get_categories/$', views.get_categories, name='get_categories'),
    url(r'^get_products/$', views.get_products, name='get_products'),
    url(r'^stock_update/$', views.stock_update, name='stock_update'),
    #add catalogue,category,products using ajax
    url(r'^catalogue_add/$', views.catalogue_add, name='catalogue_add'),
    #add category using ajax
    #url(r'^category_add/$', views.category_add, name='category_add'),
    url(r'^store_summary/$', views.store_summary, name='store_summary'),
    #edit the products
    url(r'^product_edit/$', views.product_edit, name='product_edit'),
    url(r'^paginate_test/$', views.paginate_test, name='paginate_test'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #New urls
    url(r'^add_person/$', views.add_person, name='add_person'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^add_catalogue/$', views.add_catalogue, name='add_catalogue'),
    #for product search when making a sale
    url(r'^suggest_product/$', views.suggest_product, name='suggest_product'),
    #when a product searched is clicked return the description using this view
    url(r'^product_details/$', views.product_details, name='product_details'),
    #check if the quantity can be sold
    url(r'^check_quantity/$', views.check_quantity, name='check_quantity'),

    #check if a product name,product serial,ctaegory,or catalogue exists
    #url(r'^check_cat_prod_exist/$', views.check_cat_prod_exist, name='check_cat_prod_exist'),
    #testing image upload
    url(r'^list/$', views.list, name='list'),
    #Now we are doing the reports
    url(r'^reports/$', views.reports, name='reports'),
    #all sales i.e the reports
    url(r'^all_sales_reports/$', views.all_sales_reports, name='all_sales_reports'),
    #sales by product reports
    url(r'^sales_by_product/$', views.sales_by_product, name='sales_by_product'),
    #sales by user reports
    url(r'^user_sales_reports/$', views.user_sales_reports, name='user_sales_reports'),
    #opening/closing stock reports
    url(r'^get_open_close_stock/$', views.get_open_close_stock, name='get_open_close_stock'),
    #all payments reports
    url(r'^payments_reports/$', views.payments_reports, name='payments_reports'),
    #all payment_by_mode reports
    url(r'^payment_by_mode/$', views.payment_by_mode, name='payment_by_mode'),

    #url(r'^all_sales_reports2/$', views.all_sales_reports2, name='all_sales_reports2'),


    #check final sales page template
    url(r'^making_sales/$', views.making_sales, name='making_sales'),
    #settings page template
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings_post/$', views.settings_post, name='settings_post'),
    url(r'^filter_test/$', views.filter_test, name='filter_test'),
    """
    url(r'^paginate_test/$', views.paginate_test, name='paginate_test'),
    """
    """
    url(r'^contact_form/$', views.contact_form, name='contact_form'),
    url(r'^contact_form2/$', views.contact_form2, name='contact_form2'),
    """
    )

#urlpatterns = patterns('pos_app.views',

#)
