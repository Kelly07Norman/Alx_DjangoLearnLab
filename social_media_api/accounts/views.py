from rest_framework import generics, permissions, status, Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
    from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = CustomUser.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({"message": "You are now following {}".format(user_to_follow.username)})

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = CustomUser.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": "You have unfollowed {}".format(user_to_unfollow.username)})
