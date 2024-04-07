# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDetailsSerializer


from .models import User
from .serializers import ReferralSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"user_id": user.id, "message": "User registered successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    serializer = UserDetailsSerializer(request.user)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_referrals(request):
    referrals = User.objects.filter(referral_code=request.user.referral_code)
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(referrals, request)
    serializer = ReferralSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
