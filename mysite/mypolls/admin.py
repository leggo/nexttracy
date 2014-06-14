from django.contrib import admin

#from mysite.mypolls.models import Object

# Register your models here.
#class ObjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'created', 'slug',)
	prepopulated_fields = {'slug': ('name',)}

#admin.site.register(Object, ObjectAdmin)