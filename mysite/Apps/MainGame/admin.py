from django.contrib import admin
from mysite.Apps.Tales.models import Tale, Sentence, User, UserlessSentence, UserlessTale

# Register your models here.
admin.site.register(Tale)
admin.site.register(Sentence)
admin.site.register(UserlessTale)
admin.site.register(UserlessSentence)