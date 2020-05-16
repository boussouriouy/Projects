from django.urls import path
from .views import creat_form_view,cart_list_item, cart_detail_view

app_name = 'product'
urlpatterns = [
    path('form/', creat_form_view),
    path('list/', cart_list_item),
    path('detail/<int:id>/', cart_detail_view, name='list_items'),
]
