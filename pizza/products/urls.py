from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',homepage,name='home'),
    path('about_us/',aboutus_page,name='about_us'),
    path('register/',register,name='register'),
    path('users/',user_list,name='users'),
    path('create_order/<int:product_id>/',create_order,name='create_order'),
    path('update_order/<int:order_id>/',update_order),
    path('delete_order/<int:order_id>/',delete_order),
    path('signin/',sign_in,name='login'),
    path('logout/',logout_page,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')

]


