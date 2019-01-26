# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class arecord_users(models.Model):
    domain_name = models.CharField(max_length=200)
    redirect_to_url = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    permanent = models.CharField(max_length=200)
    parameter_copy = models.CharField(max_length=200)
    request_path = models.CharField(max_length=200)
    domain_type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    updated_date = models.CharField(max_length=200)
    ssl_status = models.CharField(max_length=200)

class validation(models.Model):
	domain_name=models.CharField(max_length=200,null = True)
	public_key=models.TextField()
	private_key=models.TextField()
	
	def __str__():
		return self.domain_name,self.public_key,self.private_key
