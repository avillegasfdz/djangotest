from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from .forms import ClientForm
from .models import Client


def get_adminitrator(user_id):
    """returns the administrator object given its user_id"""
    return SocialAccount.objects.get(user_id=user_id)


def welcome(request):
    """
    Shows the welcome template.
    :param request: http request.
    :return: HttpResponse with the welcome template.
    """
    template = loader.get_template('bank/welcome.html')
    context = {}
    return HttpResponse(template.render(context, request))


def client_list(request):
    """
    Renders a template with the client list.
    :param request: http request.
    :return: HttpResponse with the client list.
    """
    context = {"client_list": Client.objects.all()}
    return render(request, "bank/client_list.html", context)


def client_form(request, admin_id, client_id=None):
    """
    Manages the client form.
    :param request: http request.
    :param admin_id: administrator id.
    :param client_id: client id.
    :return: HttpResponse with the form
    """
    administrator = get_adminitrator(admin_id)
    if request.method == "GET":
        if not client_id:  # Insert operation
            form = ClientForm(initial={'administrator': administrator})
        else:  # Update Operation
            client = Client.objects.get(pk=client_id)
            form = ClientForm(instance=client)

        return render(request, "bank/client_form.html", {"form": form})
    elif request.method == "POST":
        if not client_id:  # Insert operation
            form = ClientForm(request.POST, initial={'administrator': administrator})
        else:  # Update Operation
            client = Client.objects.get(pk=client_id)
            form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
        return redirect("/bank/manager")


def client_delete(request, admin_id, client_id):
    client = Client.objects.get(pk=client_id)
    administrator = get_adminitrator(admin_id)
    if client.administrator == administrator:
        client.delete()
    return redirect("/bank/manager/")