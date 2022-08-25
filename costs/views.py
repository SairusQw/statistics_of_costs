from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from costs.forms import DataSearch, CustomUserCreationForm
from costs.models import Cost, CustomUser


@login_required
def index(request):
    """View function for the home page of the site."""
    cla = Cost.objects.all()
    slov = {}

    for i in cla:
        if i.category in slov:
            slov[i.category] += i.price
        else:
            slov[i.category] = i.price

    context = {
        "slov": slov
    }
    return render(request, "costs/index.html", context=context)


class CostListView(LoginRequiredMixin, generic.ListView):
    model = Cost
    queryset = Cost.objects.all()
    template_name = "costs/cost_list.html"
    context_object_name = "cost_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CostListView, self).get_context_data(**kwargs)

        data = self.request.GET.get("data", "")

        context["search_form"] = DataSearch(
            initial={
                "data": data
            }
        )

        return context

    def get_queryset(self):
        form = DataSearch(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                data__icontains=form.cleaned_data["data"]
            )

        return self.queryset


class CostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cost
    fields = "__all__"
    template_name = "costs/cost_form.html"
    success_url = reverse_lazy("costs:cost_list")


class CostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cost
    fields = "__all__"
    success_url = reverse_lazy("costs:cost_list")


class CostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cost
    success_url = reverse_lazy("costs:cost_list")


def delete_all(request):
    Cost.objects.all().delete()
    return render(request, "costs/cost_list.html")


class CustomUserListView(generic.ListView):
    model = CustomUser
    paginate_by = 2
    queryset = CustomUser.objects.all()


class CustomUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    queryset = CustomUser.objects.all()


class CustomUserCreateView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm


class CustomUserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CustomUser
    success_url = reverse_lazy("")
