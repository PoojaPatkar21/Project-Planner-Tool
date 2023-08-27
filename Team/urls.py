from django.urls import path
from Team.views import TeamBase

urlpatterns = [
    path('', TeamBase.as_view(), name='get/createTeam'),
    path('<int:pk>/', TeamBase.as_view(), name='getspecificTeam'),
]
