from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST': # 제출버튼을 누르면 POST방식으로 전송됨. POST 방식으로 전송이 됐다면,
        if request.POST['password1'] == request.POST['password2']: # password1과 password2가 같다면,
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1']) # auth의 models의 User라는 쿼리셋
                                            # username에서 적은 것을 username이라는 변수에 담겠다.
            auth.login(request, user) # login 함수
            return redirect('home') # login되면 바로 home으로 이동
    return render(request, 'signup.html') # 위에께 안되면 signup.hmtl에 머문다.

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password) # 회원이 맞는지 확인시켜주는 함수
        if user is not None: # 이미 존재하는 회원이라면 login시켜주고 home으로 이동
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')
