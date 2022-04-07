
from django.urls import path
from book import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomeView, name ="home"),
    path('signup/', views.SignupView, name ="signup"),
    path('login/', views.LoginView, name ="login"),
    path('logout/', views.LogoutView, name ="logout"),
    path('dashboard/', views.Dashboard, name ="dashboard"),
    path('addbook/', views.AddbookView.as_view(), name ="addbook"),
    path('deletebook/<int:pk>', views.DeleteView.as_view(), name ="deletebook"),
    path('updatebook/<int:pk>', views.UpdateView.as_view(), name ="updatebook"),
    
]
