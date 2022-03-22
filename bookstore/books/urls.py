from django.urls import path

from . import views


app_name = 'books'
urlpatterns = [
    path('', views.ListBookView.as_view(), name='list-books'),
    path('<int:pk>/', views.DetailBookView.as_view(), name='detail-book'),
    path('create', views.CreateBookView.as_view(), name='create-book'),
    path('update/<int:pk>', views.UpdateBookView.as_view(), name='update-book'),
    path('delete/<int:pk>', views.delete_book, name='delete-book')
]