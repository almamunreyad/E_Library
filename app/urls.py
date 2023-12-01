from django.urls import path
from .import views 



urlpatterns = [
    path('', views.home, name="homepage"), 
    path('signup/', views.signup, name="signuppage"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logoutpage"),
    path('about/', views.about, name="aboutpage"), 
    path('library/', views.library, name="librarypage"), 
    path('contact/', views.contact, name="contactpage"), 
    path('cse/', views.cse, name="csepage"),
    path('eee/', views.eee, name="eeepage"),
    path('bba/', views.bba, name="bbapage"),
    path('eng/', views.eng, name="engpage"),
    path('law/', views.law, name="lawpage"),
    path('civil/', views.civil, name="civilpage"),
    path('pharmacy/', views.pharmacy, name="pharmacypage"),
    
] 