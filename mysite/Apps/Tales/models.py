import json
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tale(models.Model):
	length = models.IntegerField(default=0,	name='Length')
	isFinished = models.BooleanField(default=0, name='isFinished')
	lastAuthorID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lastAuthorID')
	dateStarted = models.DateTimeField(name='dateStarted')
	dateFinished = models.DateTimeField(name='dateFinished', null=True, blank=True)
	TaleName = models.TextField(name="TaleName", max_length=50, default="defaultTaleName")
	isBeingWritten = models.BooleanField(default=0, name='isBeingWritten')

	def __str__(self):
		return self.TaleName
	def get_absolute_url(self):
		return reverse('tale', args=[str(self.id)])


class Sentence(models.Model):
	authorID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorID')
	taleID = models.ForeignKey(Tale, on_delete=models.CASCADE, related_name='taleID', )
	dateAdded = models.DateTimeField(name='dateAdded')
	sentence = models.TextField(name='Sentence', max_length=128)

	class Meta:
		indexes = [
			models.Index(fields=['taleID','authorID'])
		]

	def __str__(self):
		return self.id

#Классы тупо для теста, ибо я пока не врубаюсь как работать с юзерами
class UserlessTale(models.Model):
	length = models.IntegerField(default=0,	name='Length')
	isFinished = models.BooleanField(default=0, name='isFinished')
	dateStarted = models.DateTimeField(name='dateStarted')
	dateFinished = models.DateTimeField(name='dateFinished', null=True, blank=True)
	TaleName = models.TextField(name="TaleName", max_length=50, default="defaultTaleName")
	isBeingWritten = models.BooleanField(default=0, name='isBeingWritten')
	def __str__(self):
		return self.TaleName
	def get_absolute_url(self):
		return reverse('tale', args=[str(self.id)])


class UserlessSentence(models.Model):
	taleID = models.ForeignKey(UserlessTale, on_delete=models.CASCADE, related_name='taleID')
	dateAdded = models.DateTimeField(name='dateAdded')
	sentence = models.TextField(name='Sentence', max_length=128)
	class Meta:
		indexes = [
			models.Index(fields=['taleID'])
		]
	def __str__(self):
		return self.id