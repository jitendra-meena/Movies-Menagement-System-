from rest_framework import serializers
from movies.models import Movies


class Search_By_YearSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class Search_By_IdSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields ='__all__'        


class Search_By_RatingSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields =['id','title','rating','genres']     


class Search_By_GenresSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields =['id','title','rating','genres']


class Search_By_TitleSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields =['id','title','rating','genres']    