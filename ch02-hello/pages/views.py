from django.http import HttpResponse  # noqa: D100


def home_page_view(request):  # noqa: ANN001, ANN201, ARG001, D103
    return HttpResponse("Hello, World!")
