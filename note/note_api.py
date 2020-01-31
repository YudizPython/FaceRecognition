from rest_framework import serializers
from .models import users,UserImages
from rest_framework import viewsets
import requests

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = users
        fields = '__all__'



class UserViewSet(viewsets.ModelViewSet):

    queryset = users.objects.all()
    # a = request.GET.get('username')
    # print("username is ", a)
    # print("query set is ",qu)
    serializer_class = UserSerializer

# def get_queryset(self):
#     longitude = self.request.query_params.get('username')
#     # latitude= self.request.query_params.get('latitude')
#     # radius = self.request.query_params.get('radius')

#     # location = Point(longitude, latitude)

#     queryset = users.objects.filter(username=longitude)

#     return queryset


class UserImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserImages
		fields = '__all__'


class UserImageViewSet(viewsets.ModelViewSet):

    queryset = UserImages.objects.all()
    # print("query set is ",qu)
    serializer_class = UserImageSerializer



# class TrainingViewSet(viewsets.ModelViewSet):

#     queryset = users.objects.all()
#     # print("query set is ",qu)
#     serializer_class = UserSerializer

