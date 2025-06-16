from django.urls import path
from .views import RegisterView, LoginView,SubjectListCreateView, SubjectUpdateDeleteView, MarksListCreateView, MarksUpdateDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('subjects/', SubjectListCreateView.as_view()),
    path('subjects/<int:pk>/', SubjectUpdateDeleteView.as_view()),
    path('marks/', MarksListCreateView.as_view()),
    path('marks/<int:pk>/', MarksUpdateDeleteView.as_view()),
]