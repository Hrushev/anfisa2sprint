from django.shortcuts import render, get_object_or_404

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.filter(
        is_published=True,
        category__is_published=True
        ),
        pk=pk
        )
    context = {
        'ice_cream': ice_cream
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
