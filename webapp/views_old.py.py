from django.shortcuts import render,HttpResponse

# Create your views here.
from .forms import BookForm
from .models import arecord

from django.shortcuts import render
from .models import Book
import datetime

def home(request):
    data = arecord.objects.all()
    return render(request, 'arecord.html', {'datas': data})

def create_data(request):
	if request.method == 'POST':
		doamin_name = request.POST['doamin_name']
		redirect_url = request.POST['redirect_url']
		region =request.POST['region']
		updated_date=str(datetime.datetime.now())
		user='Murugesan'

		Book.objects.create(
   		doamin_name=doamin_name,
    	redirect_url=redirect_url,
    	region= region,
    	updated_date=updated_date,
    	pages=pages,
    	user=user,
)
    
	return HttpResponse("")