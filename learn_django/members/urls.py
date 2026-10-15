from django.urls import path
from .views import MemberListCreateAPIView

urlpattern = [
     path('api/members', MermerListCreateAPIView.as_View(), name = 'member-list-create'),
]