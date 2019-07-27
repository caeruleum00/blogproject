from django.contrib import admin
from django.urls import path, include #blogapp의 url로부터 불러오기위헤 include
import blogapp.views
import portfolio.views
from django.conf import settings    # 밑에 두 줄 암기
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
