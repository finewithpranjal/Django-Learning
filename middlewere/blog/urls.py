from django.urls import path
from blog.views import home, math, user_info
urlpatterns = [
   path('', home, name='home'),
   path('math/', math, name='math'),
   path('user/', user_info, name='user_info'),
]