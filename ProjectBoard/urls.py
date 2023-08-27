from django.urls import path
from ProjectBoard.views import ProjectBoardBase

urlpatterns = [
    path('', ProjectBoardBase.as_view(), name='get/createteam'),
    path('<int:pk>/', ProjectBoardBase.as_view(), name='getspecificteam'),
]

