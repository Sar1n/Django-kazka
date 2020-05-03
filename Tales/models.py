import json
from django.db import models
from django.contrib.auth.models import User

class Tale(models.Model):
	length = models.IntegerField(default=0,	name='Length')
	isFinished = models.BooleanField(default=0, name='isFinished')
	lastAuthorID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lastAuthorID')
	dateStarted = models.DateTimeField(name='dateStarted')
	dateFinished = models.DateTimeField(name='dateFinished')
	TaleName = models.TextField(name="TaleName", max_length=50)

class Sentence(models.Model):
	authorID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='AuthorID')
	taleID = models.ForeignKey(Tale, on_delete=models.CASCADE, related_name='TaleID', )
	dateAdded = models.DateTimeField(name='dateAdded')
	sentence = models.TextField(name='Sentence', max_length=128)

	class Meta:
		indexes = [
			models.Index(fields=['taleID','authorID'])
		]