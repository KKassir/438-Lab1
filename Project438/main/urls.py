from django.urls import path
from . import views



app_name = "main"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('destroy/<int:id>', views.destroy, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatecontact/<int:id>', views.updatecontact, name='updatecontact'),
    path('searchname', views.searchbyname, name="searchname"),
    path('searchNT', views.searchNT, name="searchNT"),
    path('searchP', views.searchP, name="searchP"),
    path('comparepage', views.comparepage, name="comparepage"),
    path('compare', views.compare, name="compare"),
]