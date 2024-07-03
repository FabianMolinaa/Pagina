from django.urls import path
from PAGINA_WEB import views

urlpatterns = [
    path("", views.index, name="index"),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register,name="register"),
    path('Akuyaku_Reijou/', views.Akuyaku, name='akuyaku'),
    path('black_clover/', views.black_clover, name='black_clover'),
    path('blue_lock/', views.blue_lock, name='blue_lock'),
    path('chainsaw_man/', views.chainsaw_man, name='chainsaw_man'),
    path('jujutsu_kaisen/', views.jujutsu_kaisen, name='jujutsu_kaisen'),
    path('sousou_no_frieren/', views.sousou, name='sousou'),
    path('spyxfamily/', views.spy, name='spy'),
    path('yofukashi/', views.yofukashi, name='yofukashi'),
    path("crud/", views.crud, name="crud"),
    path("add_manga/",views.add_manga,name="add_manga"),
    path("del_manga/<str:titulo>", views.del_manga, name="del_manga"),
]