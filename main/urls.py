from django.urls import path
from .views import links_srt, home_srt, redirect_srt

urlpatterns = [
    path('api/v1', links_srt, name=''),
    path('', home_srt, name='home_page'),
    path('l/<str:link>', redirect_srt, name='redirect')
]