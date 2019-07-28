from django.urls import path
from .views import topView ,barRankListView,upload ,loginfunc, signupfunc,listfunc

app_name = 'barRankCsv'
urlpatterns = [
    path('list/', barRankListView.as_view(),name='list'),
    path('login/',loginfunc,name='login'),
]
