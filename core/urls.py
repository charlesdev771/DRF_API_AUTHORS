from django.urls import path
from core.views import Create_And_View, UpdateAndDelete
urlpatterns = [
    path('', Create_And_View.as_view()),
    path('<int:pk>/', UpdateAndDelete.as_view()),
]
