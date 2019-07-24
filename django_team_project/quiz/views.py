from django.shortcuts import render
from bookmark.models import Bookmark
###########################################################
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article
# Create your views here.




def article_detail(request, pk):
	article = Article.objects.get(pk=pk)
    # article = Article.objects.filter(id=1)
    # article = get_object_or_404(Article,id=1)
    return render(request, 'quiz/article_detail.html', {'article': article})

def home(request):
	return render(request, 'quiz/home.html')

####################################


def article_list(request):
	articles = Article.objects.all().order_by('-id')

	return render(request, 'quiz/article_list.html', {'articles': articles})


	def article_detail(request, pk):
		article = Article.objects.get(pk=pk)
    # article = Article.objects.filter(id=1)
    # article = get_object_or_404(Article,id=1)
    return render(request, 'quiz/article_detail.html', {'article': article})


    def article_create(request):
    	if request.method == 'POST':
    		print(request.POST)
    		article = Article()
    		article.title = request.POST['title']
    		article.contents = request.POST['contents']
    		article.author = request.POST['author']
    		article.save()

    		return redirect(reverse('quiz:article_detail',
    			kwargs={'pk':article.pk}))
    	elif request.method == 'GET':
    		return render(request, 'quiz/article_create.html')


    		def article_update(request, pk):
    			if request.method == 'POST':
    				article = get_object_or_404(Article, pk=pk)
        #Article.objects.get(pk=pk)
        article.title = request.POST['title']
        article.contents = request.POST['contents']
        article.author = request.POST['author']
        article.save()
        return redirect(reverse('quiz:article_detail',
        	kwargs={'pk':article.pk}))
    elif request.method =='GET':
    	return render(request, 'quiz/article_create.html')


    	def article_delete(request, pk):
    		article = get_object_or_404(Article, pk=pk)
    		article.delete()
    		return redirect(reverse('quiz:article_list'))


#elif 부분의 get
def article_create_page(request):
	return render(request, 'quiz/article_create.html')

#if 부분 post
def article_create_process(request):
	article = Article()
    # article 객체 값 넣어주기
    article.title = request.POST['title']
    article.contents = request.POST['contents']
    article.author = request.POST['author']

    article.save()  #데이터베이스 저장
    return render(request, 'quiz/article_list.html')




