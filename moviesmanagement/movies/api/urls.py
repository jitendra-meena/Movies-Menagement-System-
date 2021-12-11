from django.contrib import admin
from django.urls import path
from movies.api.views import Search_By_Year, Search_By_Id, Search_By_Rating, Search_By_Genres, Search_By_Title

urlpatterns = [
    
    path('search_by_year/<int:year>',Search_By_Year.as_view(),name = 'search_by_year'),
    path('search_by_id/<int:id>',Search_By_Id.as_view(),name = 'search_by_id'),
    path('search_by_rating/',Search_By_Rating.as_view(),name = 'search_by_rating'),
    path('search_by_genres/',Search_By_Genres.as_view(),name = 'search_by_genres'),
    path('search_by_title/',Search_By_Title.as_view(),name = 'search_by_title'),







]