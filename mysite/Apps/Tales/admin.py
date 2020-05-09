from django.contrib import admin
from .models import *

admin.site.unregister(Tale)
admin.site.unregister(Sentence)

@admin.register(Tale)
class TaleAdmin(admin.ModelAdmin):
	list_display = ('id','TaleName', 'lastAuthorID','Length', 'dateStarted', 'dateFinished', 'isFinished', 'isBeingWritten')
	list_filter = ('id','TaleName', 'lastAuthorID','Length', 'dateStarted', 'dateFinished', 'isFinished', 'isBeingWritten')

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
	pass
	list_display = ('id', 'authorID', 'taleID', 'dateAdded', 'Sentence')
	list_filter = ('id', 'authorID', 'taleID', 'dateAdded', 'Sentence')
