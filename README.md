# LittleLemonProject
Meta Capstone project 
URLS are as follows

http:127.0.0.1/restaurant/menu/
http:127.0.0.1/restaurant/menu/pk
http:127.0.0.1/restaurant/user/registration
http:127.0.0.1/restaurant/menu/bookings/
http:127.0.0.1/restaurant/menu/bookings/pk
 
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
    path('user/registration', views.UserRegistration.as_view(), name='user-registration'),
    path('bookings/', views.bookingview.as_view()),
    path('bookings/<int:pk>/', views.bookingDetail.as_view()),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu-test', views.menu,name='menu')
