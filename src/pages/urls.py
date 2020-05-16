from django.urls import path

from .views import home_view, about_view, contact_view, info_view

app_name = 'pages'

urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view),
    path('cont/', contact_view),
    path('info/', info_view),
]