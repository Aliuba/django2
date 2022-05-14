from django.urls import path

from users.views import ListCreateUsers, GetDeleteUpdate

urlpatterns=[
    path('', ListCreateUsers.as_view()),
    path('/<int:pk>', GetDeleteUpdate.as_view())
]
