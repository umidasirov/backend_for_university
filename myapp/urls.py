from django.urls import path
from .views import upload_file,success_page,delete_file
urlpatterns =[
    path('',upload_file,name='data'),
    path('success_url/',success_page,name='success_url'),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
]