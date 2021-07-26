from django.urls import path

from menu.views import *

urlpatterns = [
    path('', MenuItemIndexView.as_view()),
    path('<int:pk>', MenuItemCardView.as_view()),
]
