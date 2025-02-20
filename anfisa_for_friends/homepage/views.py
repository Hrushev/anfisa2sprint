from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.select_related(
        'category'
        ).filter(
        is_published=True,
        category__is_published=True
        ).order_by(
        'category'
        )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
