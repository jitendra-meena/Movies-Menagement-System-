from rest_framework.generics import ListAPIView , ListCreateAPIView
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Avg ,Sum
from django.shortcuts import get_object_or_404
from datetime import datetime
from datetime import timedelta
import datetime  
import requests
from .serializers import (
    Search_By_YearSerailizer,
    Search_By_IdSerailizer,
    Search_By_RatingSerailizer,
    Search_By_GenresSerailizer,               
    Search_By_TitleSerailizer 
    )
from movies.models import Movies

class Search_By_Year(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = Search_By_YearSerailizer

    def get(self, request,year):
        movies_obj = Movies.objects.filter(pub_date__year = year)
        if movies_obj:
            serializer = Search_By_YearSerailizer(movies_obj,many = True)
            return Response({'status':'200' , 'msg': 'Movies List by Year','data': serializer.data})
        else:
            return Response({'status':'200' , 'msg': 'No result Found By year'})


class Search_By_Id(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = Search_By_IdSerailizer

    def get(self, request,id):
        movies_obj = Movies.objects.get(id = id)
        if movies_obj:
            serializer = Search_By_IdSerailizer(movies_obj)
            return Response({'status':'200' , 'msg': 'Movies List by Id','data': serializer.data})
        else:
            return Response({'status':'200' , 'msg': 'No result Found By Id'})
    

class Search_By_Rating(ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = Search_By_RatingSerailizer

    def post(self, request):
        rating = request.data.get('rating')
        movies_obj = Movies.objects.filter(rating__icontains = rating)
        if movies_obj:
            print(movies_obj)
            serializer = Search_By_RatingSerailizer(movies_obj, many = True)
            print(serializer.data)
            return Response({'status':'200' , 'msg': 'Movies List by Rating','data': serializer.data})
        else:
            return Response({'status':'200' , 'msg': 'No result Found By Rating'})



class Search_By_Genres(ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = Search_By_GenresSerailizer

    def post(self, request):
        genres = request.data.get('genres')
        movies_obj = Movies.objects.filter(Q(genres__contains = genres))
        if movies_obj:
            serializer = Search_By_GenresSerailizer(movies_obj,many = True)
            return Response({'status':'200' , 'msg': 'Movies List by Genres','data': serializer.data})
        else:
            return Response({'status':'200' , 'msg': 'No result Found By Genres'})
    


class Search_By_Title(ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = Search_By_TitleSerailizer

    def post(self, request):
        title = request.data.get('title')
        movies_obj = Movies.objects.filter(title__exact = title)
        if movies_obj:
            serializer = Search_By_TitleSerailizer(movies_obj,many = True)
            return Response({'status':'200' , 'msg': 'Movies List by Genres','data': serializer.data})
        get_date()
        movies_obj = Movies.objects.filter(title__exact = title)
        if movies_obj:    
            serializer = Search_By_TitleSerailizer(movies_obj,many = True)
            return Response({'status':'200' , 'msg': 'Movies List by Genres','data': serializer.data})
        else:
            return Response({'status':'200' , 'msg': 'No result Found By Genres'})
    

def get_date():
    
    url = 'http://www.omdbapi.com/?i=tt3896198&apikey=2491a6b9'
    res = requests.get(url)
    data = res.json()
    result = data['Year']
    d = datetime.date(int(result), 10, 19)
    movies_obj = Movies.objects.create(title = data['Title'] ,pub_date = d,rating = data['imdbRating'],genres = data['Genre'])
    print(movies_obj)
    movies_obj.save()
    
        












