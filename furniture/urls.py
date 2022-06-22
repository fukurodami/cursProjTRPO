from django.urls import path
from furniture import views
from unicodedata import name


urlpatterns = [
    path("", views.MainView.as_view()),
    path("us/", views.UsView.as_view()),
    path("bedroom/", views.ItemsViewBedroom.as_view()),
    path("table/", views.ItemsViewTable.as_view()),
    path("livingroom/", views.ItemsViewLivingroom.as_view()),
    path("bed/", views.ItemsViewBed.as_view()),
    path("dresser/", views.ItemsViewDresser.as_view()),
    path("cupboard/", views.ItemsViewCupboard.as_view()),
    path("rack/", views.ItemsViewRack.as_view()),
    path("hallway/", views.ItemsViewHallway.as_view()),
    path("teenagers/", views.ItemsViewTeenagers.as_view()),
    path("<int:pk>/", views.OrderView.as_view()),
]