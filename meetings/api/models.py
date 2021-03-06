from __future__ import unicode_literals
from django.contrib.auth.models import User, Group

from django.db import models

# Create your models here.

class Node(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	contributors = models.ForeignKey(Group)
	description = models.TextField()
	keywords = models.CharField(max_length=500)

	class Meta:
		ordering = ('created',)

class SubmissionEval(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	premise = models.IntegerField()
	research = models.IntegerField()
	style = models.IntegerField()
	comment = models.TextField()
	total = models.IntegerField()
	
	class Meta:
		ordering = ('created',)

class Meeting(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	submission_date = models.DateField()
	close_date = models.DateField()
	logo_url = models.CharField(max_length=500)
	tags = models.CharField(max_length=500)
	sponsors = models.CharField(max_length=500)
	description = models.TextField()

	class Meta:
		ordering = ('created',)