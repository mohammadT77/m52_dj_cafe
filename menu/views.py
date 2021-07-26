from django.shortcuts import render
from django.views import generic

# Create your views here.
from menu.models import MenuItem


class MenuItemDetail(generic.DetailView):
    pass


class MenuItemCardView(generic.DetailView):
    template_name = 'menu/menu_cardview.html'
    model = MenuItem
    context_object_name = 'menu_item'


class MenuItemIndexView(generic.TemplateView):
    template_name = 'menu/menu_index.html'
    extra_context = {
        'menu_items': MenuItem.objects.all()
    }

class MenuItemListView(generic.TemplateView):
    template_name = 'menu/menu_index.html'
    extra_context = {
        'menu_items': MenuItem.objects.all()
    }

