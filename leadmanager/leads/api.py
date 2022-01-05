from leads.models import Lead
from leads.serializers import LeadSerializer

from rest_framework import viewsets, permissions

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = LeadSerializer
