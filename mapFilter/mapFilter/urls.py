from django.urls import path
from django.conf.urls.static import static
from Nlp.views import *
from mapFilter import settings
from django.contrib import admin
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('my/', index, name='my'),
    path('add/', add, name='add'),
    path('pay/', pay, name='pay'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('admin/', admin.site.urls),
]


