from rest_framework import generics
from .models import ContactUs
from .serializers import ContactUsSerializer

class ContactUsCreateView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer 