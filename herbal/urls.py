from django.conf.urls import url
from herbal import views

urlpatterns =[
url(r'^$',views.herbal,name='herbal')
]
