from django.urls import path
from . import views

app_name = "library"
urlpatterns = [
    path('', views.library, name='library_index'),
    path('list/', views.library_list, name='library_list'),
    path('detail1/<library_id>', views.library_detail_1, name='library_detail_1'),
    path('detail2/', views.library_detail_2, name='library_detail_2'),
    path('detail/', views.library_detail, name='library_detail')

]
