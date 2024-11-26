from django.urls import path
from . import views

urlpatterns = [
               path('', views.Hello, name="landing"), 
               path('home/', views.home, name="Home"),
               path('home/<int:id>', views.overview, name="overviews"),
               path('login/', views.login, name="login"),
               path('sinup/', views.signup, name='sinup'),
               path('dashboard/<int:id>', views.dashboard, name="dashboard"),
               path('sinup/coopinfo', views.complete_account, name="complete_acc"),
               path('notification/<int:id>', views.notification, name="notification"),
               path('management/<int:id>', views.stock_mngt, name="management"),
               path('scockManagement/add', views.add_mngt, name="add"),
               ]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

