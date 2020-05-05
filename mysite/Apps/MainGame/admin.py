from django.contrib import admin
from mysite.Apps.Tales.models import Tale, Sentence, TestData, User

# Register your models here.
admin.site.register(Tale)
admin.site.register(Sentence)
admin.site.register(TestData)