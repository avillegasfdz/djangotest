from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def welcome(request):
    """
    Shows the welcome template.
    :param request: http request
    :return: HttpResponse with the welcome template.
    """
    template = loader.get_template('bank/welcome.html')
    context = {}
    return HttpResponse(template.render(context, request))
