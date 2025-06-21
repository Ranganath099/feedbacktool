from django.urls import path
from .views import FeedbackView, AcknowledgeFeedback,RegisterUser, UserListView, CustomTokenView,team_members, public_managers_list, users_list

urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    path('feedback/<int:pk>/ack/', AcknowledgeFeedback.as_view()),
    path('register/', RegisterUser.as_view()),
    path('users/', UserListView.as_view()),
    path("token/", CustomTokenView.as_view(), name="token_obtain_pair"),
    path("team/", team_members, name="team-members"),
    path('managers/', public_managers_list, name="managers_list"), 
    path('users_list/', users_list, name="users_list"), 
]
