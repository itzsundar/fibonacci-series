from django.conf.urls import url
from fib_series import views

urlpatterns = [
    url(r'^$', views.index, name='calculate_result'),
]