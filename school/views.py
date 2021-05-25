
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PresenceStatusSerializer, StudentSerializer, SubjectSerializer, StatusSerializer
from .models import PresenceStatus, Student, Subject, Status
from rest_framework.viewsets import ModelViewSet


#viewset created smart (CRUD) - does the same as the @api view
# for Presence List below (also CRUD)
#we overwrite viariables (zmienne), which are held in superior class = ModelViewSet (ta klaasa ma
# w sobie zdefiniowane metody

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PresenceStatusSet(ModelViewSet):
    queryset = PresenceStatus.objects.all()
    serializer_class = PresenceStatusSerializer


#REFACTORING - embedded code form Django Rest Framework above
# @api_view(['GET'])
# def schoolOverview(request):
#
#     school_urls = {
#         'List': '/students-list/',
#         'Detail View': '/student-detail/<str:pk>/',
#         'Create': '/student-create/',
#         'Update': '/student-update/<str:pk>/',
#         'Delete': '/student-delete/<str:pk>/',
#         }
#     return Response(school_urls)
#
# @api_view(['GET'])
# def studentPresenceList(request):
#     presence = PresenceStatus.objects.all()
#     serializer = PresenceStatusSerializer(presence, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def studentPresenceDetail(request, pk):
#     presence = PresenceStatus.objects.get(id=pk)
#     serializer = PresenceStatusSerializer(presence, many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def studentPresenceCreate(request):
#     serializer = PresenceStatusSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
# @api_view(['PUT'])
# def studentPresenceUpdate(request, pk):
#     presence = PresenceStatus.objects.get(id=pk)
#     serializer = PresenceStatusSerializer(instance=presence, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def studentPresenceDelete(request, pk):
#     presence = PresenceStatus.objects.get(id=pk)
#     presence.delete()

    # return Response('Item successfully deleted')

