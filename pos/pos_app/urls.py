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
    url(r'^register/$', views.register, name='register'),
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
    url(r'^stock_update/$', views.stock_update, name='stock_update'),
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
