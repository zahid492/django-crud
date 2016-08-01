from rest_framework import serializers

from rawApi.models import Task,City,State,Country,Zip


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id','name','state_abbr')

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id','name')

class ZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zip
        state = StateSerializer(many=True)
        city = CitySerializer(many=True)
        country = CountrySerializer(many=True)
        fields = ('id','zipcode','state','city','country',)

class ZipSerializerShow(serializers.ModelSerializer):
    state = StateSerializer()
    city = CitySerializer()
    country = CountrySerializer()


    class Meta:
        model = Zip
        fields = ('id','zipcode','state','city','country',)