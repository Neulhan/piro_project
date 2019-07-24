###########################################################
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import User, Guest
# Create your views here.


def view_quiz_init(request, quiz_value):
	quiz = User.objects.get(code=quiz_value)
	# article = Article.objects.filter(id=1)
	# article = get_object_or_404(Article,id=1)
	print(quiz)
	return render(request, 'quiz/quiz_init.html', {'quiz': quiz, 'next_url': next_url})

def view_quiz1(request, quiz_value):
	
	pass

def view_quiz2(request, quiz_value):
	pass

def view_quiz3(request, quiz_value):
	pass

def view_quiz4(request, quiz_value):
	pass

def view_quiz5(request, quiz_value):
	pass

def view_quiz6(request, quiz_value):
	pass

def view_quiz7(request, quiz_value):
	pass

def view_quiz8(request, quiz_value):
	pass

def view_quiz9(request, quiz_value):
	pass

def view_quiz10(request, quiz_value):
	pass

def view_quiz_result(request, quiz_value):
	pass

def create_quiz1(request,quiz_value):

	pass

def create_quiz2(request,quiz_value):
	pass

def create_quiz3(request,quiz_value):
	pass

def create_quiz4(request,quiz_value):
	pass

def create_quiz5(request,quiz_value):
	pass

def create_quiz6(request,quiz_value):
	pass

def create_quiz7(request,quiz_value):
	pass

def create_quiz8(request,quiz_value):
	pass

def create_quiz9(request,quiz_value):
	pass

def create_quiz10(request,quiz_value):
	pass

def create_quiz_result(request,quiz_value):
	pass



def home(request):
	print('test')
	# if request.method == "GET":
	try:
		name = request.GET.get('name')
		code = request.GET.get('code')
		if code != None:
			return render(request, 'create_quiz1.html', {'name':name, 'code':code})
		else:
			next_url = 'http://127.0.0.1:8000/quiz/' + 'code' + '/create_quiz1'
			return render(request, "index.html", {'next_url': next_url})
	except:
		next_url = 'http://127.0.0.1:8000/quiz/' + 'code' + '/create_quiz1'
		return render(request, "index.html", {'next_url': next_url})
#################################
	

# def article_list(request):
# 	articles = Article.objects.all().order_by('-id')

# 	return render(request, 'quiz/article_list.html', {'articles': articles})


# def article_detail(request, pk):
# 	article = Article.objects.get(pk=pk)
# # article = Article.objects.filter(id=1)
# # article = get_object_or_404(Article,id=1)
# return render(request, 'quiz/article_detail.html', {'article': article})


# def article_create(request):
# 	if request.method == 'POST':
# 		print(request.POST)
# 		article = Article()
# 		article.title = request.POST['title']
# 		article.contents = request.POST['contents']
# 		article.author = request.POST['author']
# 		article.save()

# 		return redirect(reverse('quiz:article_detail',
# 			kwargs={'pk':article.pk}))
# 	elif request.method == 'GET':
# 		return render(request, 'quiz/article_create.html')


# def article_update(request, pk):
# 	if request.method == 'POST':
# 		article = get_object_or_404(Article, pk=pk)
#     #Article.objects.get(pk=pk)
#     article.title = request.POST['title']
#     article.contents = request.POST['contents']
#     article.author = request.POST['author']
#     article.save()
#     return redirect(reverse('quiz:article_detail',
#     	kwargs={'pk':article.pk}))
# 	elif request.method =='GET':
# 		return render(request, 'quiz/article_create.html')


# def article_delete(request, pk):
# 	article = get_object_or_404(Article, pk=pk)
# 	article.delete()
# 	return redirect(reverse('quiz:article_list'))


# #elif 부분의 get
# def article_create_page(request):
# 	return render(request, 'quiz/article_create.html')

# #if 부분 post
# def article_create_process(request):
# 	article = Article()
#     # article 객체 값 넣어주기
#     article.title = request.POST['title']
#     article.contents = request.POST['contents']
#     article.author = request.POST['author']

#     article.save()  #데이터베이스 저장
#     return render(request, 'quiz/article_list.html')




