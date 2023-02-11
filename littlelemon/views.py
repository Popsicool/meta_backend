from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# @authentication_classes([TokenAuthentication])
def msg(request):
    return "ping"