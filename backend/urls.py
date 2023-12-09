from django.urls import path
from .views import ContactUsCreateView

urlpatterns = [
    path('contactus/', ContactUsCreateView.as_view(), name='ContactUsCreate'),
]
