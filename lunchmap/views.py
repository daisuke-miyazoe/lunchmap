from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from .serializers import CategorySerializer, ShopSerializer

from .models import Shop, Category


# class CategoryView(generic.ListView):
#     model = Shop
#     template_name = 'lunchmap/shop_list.html'
#
#     def get_queryset(self, **kwargs):
#         category = Category.objects.get(name=self.kwargs['category'])
#         queryset = Shop.objects.filter(category=category)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_key'] = self.kwargs['category']
#         return context

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ListView(generic.ListView):
    model = Shop
    # template_name = 'lunchmap/shop_list.html'
    # queryset = Shop.objects.filter(address__contains="横浜")
    # e = queryset
    paginate_by = 2

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        keyword = self.request.GET
        if (k := keyword.get('q')) is not None:
            queryset = queryset.filter(name__contains=k)

        return queryset



class DetailView(generic.DetailView):
    model = Shop


class CreateView(generic.CreateView):
    model = Shop
    # fields = (
    #     'name',
    #     'address',
    #     'author',
    # )
    fields = "__all__"

class UpdateView(generic.edit.UpdateView):
    model = Shop
    fields = "__all__"


class DeleteView(generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy("main:list")
