from django.urls import path
from .views import SignUpView,ProfilePageView, ProfileEditPageView

urlpatterns = [
    path('', SignUpView.as_view(), name='profile'),
    path('profile_edit/', ProfileEditPageView, name='profile_edit')
]