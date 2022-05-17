from django.urls import path
from songs.views import SongDetailView
from songs.views import SongsView

urlpatterns = [
    path('', SongsView.as_view(), name='songs'),
    path('<str:id>/', SongDetailView.as_view(), name='song_detail')
]
