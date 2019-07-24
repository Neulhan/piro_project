from django.shortcuts import render
from bookmark.models import Bookmark
# Create your views here.

def home(request):
	urlList = Bookmark.objects.order_by('title')
	urlCount = Bookmark.objects.all().count()
	return render(request, 'list.html', {'urlList' :urlList, 'urlCount':urlCount})

	def form(request):
		print(request)
		ctx = {
		'first' : request.POST['first_input'],
		'second' : request.POST['second_input']
		}
		print(ctx)
		return render(request, 'form.html' ,ctx)

