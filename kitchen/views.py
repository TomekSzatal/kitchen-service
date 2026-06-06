from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm
from kitchen.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = (self.request.GET.get("q") or "").strip()

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = (self.request.GET.get("q") or "").strip()

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class CookDetailView(generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = (self.request.GET.get("q") or "").strip()

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dishtype-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dishtype-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dishtype-list")

