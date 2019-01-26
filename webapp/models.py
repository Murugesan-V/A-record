from django.db import models

class arecord(models.Model):

    domain_name=models.CharField(max_length=50)
    redirect_url=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    ssl_cert=models.TextField(blank=True, null=True)
    pub_key=models.TextField(blank=True, null=True)
    chain_key=models.TextField(blank=True, null=True)
    updated_date=models.CharField(max_length=50,null=True)
    comment=models.TextField(blank=True, null=True)
    user=models.CharField(max_length=50,blank=True, null=True)
    protocol=models.CharField(max_length=50,blank=True, null=True)
    

