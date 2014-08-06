from django.contrib import admin

# Register your models here.
from pos_app.models import Category,UserProfile,Person,Catalogue

#from django.contrib import admin
#from djangoapp.addressbook.models import Contacts

#admin.site.register(Person)
admin.site.register(Category)
#admin.site.register(Page)
admin.site.register(UserProfile)
admin.site.register(Person)
admin.site.register(Catalogue)
# Register your models here.
#admin.site.register(Question)
#class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date','question_text']
#admin.site.register(Question,QuestionAdmin)


#admin.site.register(Choice)

