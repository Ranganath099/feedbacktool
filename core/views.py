from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Feedback, User
from .serializers import FeedbackSerializer, RegisterSerializer, UserSerializer
from .permissions import IsManager, IsEmployee
from rest_framework.decorators import api_view, permission_classes
class FeedbackView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'manager':
            return Response({'error': 'Only managers can submit feedback.'}, status=403)
        data = request.data
        data['manager'] = request.user.id
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        if request.user.role == 'manager':
            feedbacks = Feedback.objects.filter(manager=request.user)
        else:
            feedbacks = Feedback.objects.filter(employee=request.user)
        return Response(FeedbackSerializer(feedbacks, many=True).data)

class AcknowledgeFeedback(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]

    def patch(self, request, pk):
        feedback = Feedback.objects.get(id=pk)
        if feedback.employee != request.user:
            return Response({'error': 'Not allowed'}, status=403)
        feedback.acknowledged = True
        feedback.save()
        return Response({'message': 'Acknowledged'})


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only managers or staff can see all users
        if request.user.role != 'manager' and not request.user.is_staff:
            return Response({'error': 'Access denied'}, status=403)

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def team_members(request):
    print("DEBUG >> User:", request.user.username)
    print("DEBUG >> Authenticated:", request.user.is_authenticated)
    print("DEBUG >> Role:", getattr(request.user, "role", None))

    if request.user.role == 'manager':
        team = User.objects.filter(manager=request.user)
        return Response(UserSerializer(team, many=True).data)

    return Response({'detail': 'Not authorized'}, status=403)

@api_view(['GET'])
def public_managers_list(request):
    managers = User.objects.filter(role='manager')
    serializer = UserSerializer(managers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)