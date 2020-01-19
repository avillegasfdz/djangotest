from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from .forms import ClientForm, AccountForm
from .models import Client, BankAccount


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
    """
    Deletes a client.
    :param request: http request.
    :param admin_id: administrator id.
    :param client_id: Id of the client to delete.
    :return: HttpResponse to the list of clients.
    """
    client = Client.objects.get(pk=client_id)
    administrator = get_adminitrator(admin_id)
    if client.administrator == administrator:
        client.delete()
    return redirect("/bank/manager/")


def account_form(request, admin_id, client_id):
    """
    Form to manage the bank accounts
    :param request: http request.
    :param admin_id: administrator id.
    :param client_id: client id.
    :return: HttpResponse with the form.
    """
    if request.method == "GET":
        client = Client.objects.get(pk=client_id)
        form = AccountForm(initial={'owner': client})
        return render(request, "bank/account_form.html", {"form": form,
                                                          "owner": str(client),
                                                          "client_id": client_id,
                                                          "admin_id": admin_id})
    else:
        client = Client.objects.get(pk=client_id)
        form = AccountForm(request.POST, initial={'owner': client})
        if form.is_valid():
            form.save()
        return redirect("/bank/manager/" + str(admin_id) + "/clients/" + str(client_id) + "/list")


def account_list(request, admin_id, client_id):
    """
    Lists the account of a client.
    :param request: http request.
    :param admin_id: administrator id.
    :param client_id: client ID
    :return: HttpResponse with the list of accounts
    """
    client = Client.objects.get(pk=client_id)
    admin = get_adminitrator(admin_id)
    accounts = filter(lambda elem: elem.owner == client, BankAccount.objects.all())
    context = {"account_list": accounts,
               "customer_name": str(client),
               "customer_id": client_id,
               "admin": admin,
               "editable": admin == client.administrator, }
    return render(request, "bank/account_list.html", context)


def account_delete(request, admin_id, client_id, account_id):
    """
    "Deletes a bank account
    :param request:
    :param admin_id:
    :param client_id:
    :param account_id:
    :return:
    """
    account = BankAccount.objects.get(pk=account_id)
    administrator = get_adminitrator(admin_id)
    client = Client.objects.get(pk=client_id)
    if client.administrator == administrator:
        account.delete()
    return redirect("/bank/manager/" + str(admin_id) + "/clients/" + str(client_id) + "/list")
