from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects #객체들의 목록 = 쿼리셋
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한페이지로 자르기
    paginator = Paginator(blog_list, 3) 
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고), request.GET은 사전형객체
    page = request.GET.get('page') 
    #request된 페이지를 얻어온 뒤 return 해준다. 하나의 페이지 = post 에 담아줬다.
    posts = paginator.get_page(page) 
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts}) #{'key':value}

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) #어떤 class로 부터, pk = 검색조건
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() #Blog 라는 클래스로부터 blog라는 객체를 생성
    blog.title = request.GET['title'] #new.html form에서 입력한 내용을 가져와서 blog.title에 넣어준다
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리셋메소드, blog라는 객체에 title, body, pub_date에 넣은 내용을 저장
    return redirect('/blog/'+str(blog.id)) #redirect(URL) ,url로 넘기세요
    #blog.id는 int형인데 url은 str형이니깐, 형변환을 시켜줘야함

    #render와 redirect의 차이
    #render는 3번째로 key값을 받음, 요안에서 지지고 볶고
    #redirect는 아예 다른 url로 이동할 수도 있다. ex. google.com 이라고 적으면 구글이 나옴 

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST' : # 1
        form = BlogPost(request.POST)
        if form.is_valid(): # 아무것도 입력안하면 "이 입력란을 작성하세요"라고 뜬다.
            post = form.save(commit = False) # 모델객체를 반환하되 저장하지 않는다
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else : # 2
        form = BlogPost()
        return render(request, 'new.html', {'form':form})