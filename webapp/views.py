from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import arecord
import os
import datetime

from django.core import serializers
from django.http import HttpResponse

@login_required

def ajax(request):
        my_model = arecord.objects.all().values('id','domain_name','redirect_url','region','protocol','updated_date','user','comment')
        #response = serializers.serialize("json", my_model)
        # HttpResponse(response, content_type='application/json')

        users_list = list(my_model)  # important: convert the QuerySet to a list object
        return JsonResponse(users_list, safe=False)

@login_required
def home(request):
        #count= User.objects.count()
        data = arecord.objects.all()#.values()
        #return render(request,'main_ajax.html',{'datas':data})
	#return render(request,'arecord.html',{'datas':data})
	return render(request,'main_ajax.html',{'datas':data})
        #all_data = list(data)  main_ajax.html
        #return JsonResponse(all_data, safe=False)
        
@login_required
def edit_record_details(request,edit_id):
    #data={'status':False}
    if request.method == 'GET':
            val = arecord.objects.filter(id=edit_id).values()
            print (val)
            data=list(val)
            #data['status']=True
    return JsonResponse(data ,safe=False)

@login_required
def update_record(request,pk_id):
    data={'status':False}
    print ('id to be updated :',pk_id)
    if request.method == 'POST': 
        qs=arecord.objects.get(id=pk_id)
        qs.domain_name = request.POST['domain_name']
        qs.redirect_url = request.POST['redirect_url']
        qs.region =request.POST['region']
        qs.updated_date=str(datetime.datetime.now())[0:16]
        qs.user=request.user.username
        qs.comment=request.POST.get('comment','N/A')
        qs.protocol=request.POST['protocol']
        
        domain_name=request.POST.get('domain_name')
        ssl_cert=request.POST.get('ssl_certificate')
        pub_key=request.POST.get('public_key')
        chain_key=request.POST.get('chain_key')
        
        if request.POST['protocol'] == 'https':
            if  ssl_cert != '' and pub_key != '' : 
                if ssl_valid(ssl_cert,pub_key,domain_name):
                    qs.ssl_cert=ssl_cert
                    qs.pub_key=pub_key
                    qs.chain_key=chain_key
                    qs.save()
                    data['status']=True
                else:
                    data['status']=False
            else:
                data['status']=False            

        if request.POST['protocol'] == 'http':
            qs.ssl_cert=""
            qs.pub_key=""
            qs.chain_key=""
            qs.save()          
            data['status']=True
    return JsonResponse(data)




@login_required
def delete(request,del_id):
        data={'status':False}
        print ('id to be deleted :',del_id)
        if request.method == 'GET':
                #arecord.get_object_or_404(id=del_id).delete()
                arecord.objects.get(id=del_id).delete()
                data['message']='deleted '+str(del_id)
                data['status'] = True
        return JsonResponse(data)

@login_required
def create(request):
    data={'status':False}#,'id_data':'','comment':request.POST.get('comment','N/A'),'user':request.user.username,'updated_date':str(datetime.datetime.now())[0:16]}
    if request.method == 'POST':
        print (request.POST['domain_name'])
        domain_name = request.POST['domain_name']
        redirect_url = request.POST['redirect_url']
        region =request.POST['region']
        updated_date=str(datetime.datetime.now())[0:16]
        user=request.user.username
        comment=request.POST.get('comment','N/A')
        protocol=request.POST['protocol']
        ssl_cert=request.POST.get('ssl_certificate')
        pub_key=request.POST.get('public_key')
        chain_key=request.POST.get('chain_key')
        if protocol == 'https':
          if  ssl_cert != '' and pub_key != '' and chain_key != '' : 
            if ssl_valid(ssl_cert,pub_key,domain_name):
                data['status']=True
                arecord.objects.create(domain_name=domain_name,
                            redirect_url=redirect_url,
                            region= region,
                            updated_date=updated_date,
                            comment=comment,
                            user=user,
                            protocol=protocol,
                            ssl_cert=ssl_cert,
                            pub_key=pub_key,
                            chain_key=chain_key,
                            )
            else:
                data['status']=False
          else:
            data['status']=False
        else:
            data['status']=True
            arecord.objects.create(domain_name=domain_name,
                            redirect_url=redirect_url,
                            region= region,
                            updated_date=updated_date,
                            comment=comment,
                            user=user,
                            protocol=protocol)
        #entry_data = arecord.objects.get(domain_name=domain_name)
        #data['id_data']=entry_data.id
    return JsonResponse(data)

def ssl_valid_dup(cert,pri,domain):
        if cert == pri :
            return True
        else :
            return False

def ssl_valid(cert,pri,domain):
	print len(cert),len(pri)
        with open('/tmp/%s_cert.key'%(domain),'w') as file1:
                file1.write(cert)
        with open('/tmp/%s_pri.key'%(domain),'w') as file1:
                file1.write(pri)
        try:
                data1=os.popen("openssl x509 -noout -modulus -in /tmp/%s_cert.key | openssl md5 "%(domain)).readlines()
                data2=os.popen("openssl rsa -noout -modulus -in /tmp/%s_pri.key | openssl md5 "%(domain)).readlines()
        except Exception as e :
                return False
	print '-------',data1
	print '-------',data2
	if 'unable to load certificate' in data1 and 'unable to load certificate' in data2:
		return False
        if data1[0].strip() == data2[0].strip():
                return True
                #base_dir= os.path.join('/opt/data',domain)
                #os.mkdir(base_dir)
                #os.mkdir(os.path.join(base_dir,'private'))
                #os.mkdir(os.path.join(base_dir,'public'))
        return False
'''
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



'''
