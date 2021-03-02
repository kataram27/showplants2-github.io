from django.conf.urls import url
from show import views

urlpatterns =[
url(r'^$',views.show,name='show')
]
