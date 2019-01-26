# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from models import validation,arecord_users
from forms import PostForm,PostForm1
import os 

@login_required
def home(request):
	#count= User.objects.count()
	#data = validation.objects.all()
	form = PostForm1()
	data = arecord_users.objects.values_list()
	return render(request,'home1.html',{'a':data,'form':form})

def signup(request):
    if request.method == 'POST':
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('home_page')
    else:
	form = UserCreationForm()
    context= {'form':form}
    return render(request,'registration/signup.html',context)

def ssl_valid(cert,pri,domain):
	with open('/tmp/%s_cert.key'%(domain),'w') as file1:
		file1.write(cert)
	with open('/tmp/%s_pri.key'%(domain),'w') as file1:
                file1.write(pri)
	try:
		data1=os.popen("openssl x509 -noout -modulus -in /tmp/%s_cert.key | openssl md5 "%(domain)).readlines()
		data2=os.popen("openssl rsa -noout -modulus -in /tmp/%s_pri.key | openssl md5 "%(domain)).readlines()
	except :
		return False
	if data1[0].strip() == data2[0].strip():
		return True 
		#base_dir= os.path.join('/opt/data',domain)
		#os.mkdir(base_dir)
		#os.mkdir(os.path.join(base_dir,'private'))
		#os.mkdir(os.path.join(base_dir,'public'))
	return False 
	
@login_required
def data2(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
	    domain = form.cleaned_data.get('domain_name')
            cert = form.cleaned_data.get('public_key')
            pri = form.cleaned_data.get('private_key')
            #if str(pub) == str(pri) :
	    if ssl_valid(cert,pri,domain):
            	form.save()
		#ssl_valid(pub,pri,domain)
         	print cert,pri
		print 'VALIDATION SUCCESS'
                #return redirect('home_page')
		form = PostForm1(request.POST)
		return render(request, 'model_form_upload.html',{'form':form,'error':'VALIDATION SUCCESS'})
            else :
		print 'VALIDATION FAILED' 
         	return render(request, 'model_form_upload.html',{'form':form,'error':'VALIDATION FAILED'})
    else:
        form = PostForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

@login_required
def data(request):
     if request.method == 'POST':
        form = PostForm1(request.POST)
        if form.is_valid():
		form.save()
	        form = PostForm1(request.POST)
		data = arecord_users.objects.values_list()
        	return render(request,'home1.html',{'a':data})
      	else :
                print 'VALIDATION FAILED'
	        return render(request, 'model_form_upload.html',{'form':form,'error':'VALIDATION FAILED'})	
     else:
        form = PostForm1()
	
	return render(request, 'model_form_upload.html', {
        'form': form
    })

def delete(request,del_id):
	data={}
	print del_id
	if request.method == 'POST':
		arecord_users.objects.get(id=del_id).delete()
		data['message']='deleted '+str(del_id)
	return JsonResponse(data)	




