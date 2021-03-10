from Counter import views
from django.urls import path,include

app_name = 'counter'

urlpatterns = [
    path('',views.Counter,name='cnt'),
]
