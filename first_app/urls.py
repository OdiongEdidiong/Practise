from django.urls import path
from . import views
urlpatterns=[
    path("", views.greet),
    path("jon/",views.greetjon ),
    path("greet/<str:name>/",views.greetanyone),
    path("sqr/<int:num>",views.findsqr),
    path("EorO/<int:num>",views.iseven),
    path("cube/<int:number>/", views.cube, name="find_cube"),
    path("year/",views.newyear,name="Isitnewyear"),
    path("login/",views.getinfo,name="getinfo"),
    path("football/",views.teams,name="teams"),
    path('sqr/', views.find_sqr, name='findsqr'),
    path("vote/",views.poll,name="voter"),
    path("results/",views.maxvote,name="results"),
    path('clear/', views.clear_votes, name='clear'),
    path("name/",views.tell,name="name")
]
