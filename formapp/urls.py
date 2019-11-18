from django.urls import path
from formapp import views
app_name="formapp"
urlpatterns=[
    path('',views.get_name,name='get_name'),
]

