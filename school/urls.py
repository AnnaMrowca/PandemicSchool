
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school import views

router = DefaultRouter() #creates automatically methods below (urlpatterns) + it is necessary for viewsets like StudentViewSet
router.register(r'students', views.StudentViewSet)


urlpatterns = [
    path('presence-list/', views.studentPresenceList, name="presence-list"),
    path('presence-detail/<str:pk>/', views.studentPresenceDetail, name="presence-detail"),
    path('presence-create/', views.studentPresenceCreate, name="presence-create"),
    path('presence-update/<str:pk>/', views.studentPresenceUpdate, name="presence-update"),
    path('presence-delete/<str:pk>/', views.studentPresenceDelete, name="presence-delete"),
    path('', include(router.urls))
    ]