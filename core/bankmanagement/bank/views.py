from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from django.template import loader

from .forms import ClientForm, AccountForm
from .models import Client, BankAccount


def get_adminitrator(user_id):
    """
    Gets and administrator.
    :param user_id: id of the administrator to get.
    :return: the SocialAccount object of the administrator.
    """
    try:
        return SocialAccount.objects.get(user_id=user_id)
    except SocialAccount.DoesNotExist:
        raise Http404()


def get_client(client_id):
    """
    Gets a client.
    :param client_id: id of the client.
    :return: the Client object of client_id.
    """
    try:
        return Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404()


def get_account(account_id):
    """
    Gets an account
    :param account_id: id of the account.
    :return: BankAccount object of account_id.
    """
    try:
        return BankAccount.objects.get(pk=account_id)
    except BankAccount.DoesNotExist:
        raise Http404()


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
            client = get_client(client_id)
            form = ClientForm(instance=client)

        return render(request, "bank/client_form.html", {"form": form})
    elif request.method == "POST":
        if not client_id:  # Insert operation
            form = ClientForm(request.POST, initial={'administrator': administrator})
        else:  # Update Operation
            client = get_client(client_id)
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
    client = get_client(client_id)
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
        client = get_client(client_id)
        form = AccountForm(initial={'owner': client})
        return render(request, "bank/account_form.html", {"form": form,
                                                          "owner": str(client),
                                                          "client_id": client_id,
                                                          "admin_id": admin_id, })
    else:
        client = get_client(client_id)
        form = AccountForm(request.POST, initial={'owner': client})
        if form.is_valid():
            form.save()
            return redirect("/bank/manager/" + str(admin_id) + "/clients/" + str(client_id) + "/list")
        return render(request, "bank/account_form.html", {"form": form,
                                                          "owner": str(client),
                                                          "client_id": client_id,
                                                          "admin_id": admin_id, })


def account_list(request, admin_id, client_id):
    """
    Lists the account of a client.
    :param request: http request.
    :param admin_id: administrator id.
    :param client_id: client ID
    :return: HttpResponse with the list of accounts
    """
    client = get_client(client_id)
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
    :param request: http request.
    :param admin_id: Admin deleting the account.
    :param client_id: Owner of the account.
    :param account_id: Id of the account
    :return:
    """
    account = get_account(account_id)
    administrator = get_adminitrator(admin_id)
    client = get_client(client_id)
    if client.administrator == administrator:
        account.delete()
    return redirect("/bank/manager/" + str(admin_id) + "/clients/" + str(client_id) + "/list")


def error_handler_404(request, exception):
    """
    Handler function for the 404 error.
    :param request: http request
    :param exception: caught exception
    :return:
    """
    context = {}
    return render(request, "bank/error.html", context)


def error_handler_500(request):
    """
    Handler function for the 500 error.
    :param request: http request
    :return:
    """
    context = {}
    return render(request, "bank/error.html", context)
