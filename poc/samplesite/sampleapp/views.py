from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount

from sampleapp.models import Customer, Account

from .forms import NameForm, AccountForm
from .forms import CustomerForm


def get_adminitrator(admin_id):
    return SocialAccount.objects.get(uid=admin_id)


def index(request):
    # if Administrator.objects.all():
    #     Customer.objects.all().delete()
    #     Administrator.objects.all().delete()
    #
    # admin1 = Administrator(name="Admin 1")
    # admin1.save()
    #
    # admin2 = Administrator(name="Admin 2")
    # admin2.save()
    #
    # customer1 = Customer(name="Juan", last_name="Perez", administrator_id=admin1.id)
    # customer2 = Customer(name="Lucas", last_name="García", administrator_id=admin1.id)
    # customer3 = Customer(name="Marta", last_name="Perez", administrator_id=admin2.id)
    #
    # customer1.save()
    # customer2.save()
    # customer3.save()
    #
    # acc1 = Account(owner=customer1, iban="DE89370400440532013000")
    # acc2 = Account(owner=customer1, iban="DE89370400440532013150")
    # acc3 = Account(owner=customer3, iban="DE89370400990532013000")
    #
    # acc1.save()
    # acc2.save()
    # acc3.save()

    # admins_str = " ".join(list(map(lambda elem: elem.name, Administrator.objects.all())))
    # customers_str = " ".join(list(
    #     map(lambda elem: elem.name + " " + elem.last_name + " " + str(elem.administrator_id), Customer.objects.all())))
    # accounts_str = " ".join(list(map(lambda elem: elem.iban + " " + str(elem.owner), Account.objects.all())))
    #
    # return HttpResponse("Hello, world! \n" + "ADMINS: " + admins_str + "\n" +
    #                     "CUSTOMERS: " + customers_str + "\n" +
    #                     "ACCOUNTS: " + accounts_str + "\n")

    administrator_list = SocialAccount.objects.all()
    customer_list = Customer.objects.all()

    template = loader.get_template('sampleapp/index.html')

    form = NameForm()

    context = {
        'administrators': administrator_list,
        'customers': customer_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def added(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        #     new_admin = Administrator(name=form.cleaned_data['your_name'])
        #     new_admin.save()

        template = loader.get_template('sampleapp/added.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        pass


def customer_list(request, admin_id):
    admin = get_adminitrator(admin_id)
    context = {"customer_list": Customer.objects.all(),
               "admin": admin}
    return render(request, "sampleapp/customer_list.html", context)


def customer_form(request, admin_id, id=None):
    administrator = get_adminitrator(admin_id)
    if request.method == "GET":
        if not id:  # Insert operation
            form = CustomerForm(initial={'administrator': administrator})
        else:  # Update Operation
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)

        return render(request, "sampleapp/customer_form.html", {"form": form, "admin": administrator})
    else:
        if not id:  # Insert operation
            form = CustomerForm(request.POST, initial={'administrator': administrator})
        else:  # Update Operation
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
        return redirect("/sampleapp/" + str(admin_id) + "/list")


def customer_delete(request, admin_id, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect("/sampleapp/" + str(admin_id) + "/list")


def account_delete(request, admin_id, id, account_id):
    account = Account.objects.get(pk=account_id)
    account.delete()
    return redirect("/sampleapp/" + str(admin_id) + "/list")


def account_form(request, admin_id, id):
    if request.method == "GET":
        customer = Customer.objects.get(pk=id)
        form = AccountForm(initial={'owner': customer})
        return render(request, "sampleapp/account_form.html", {"form": form,
                                                               "owner": str(customer),
                                                               "customer_id": id,
                                                               "admin_id": admin_id})
    else:
        customer = Customer.objects.get(pk=id)
        form = AccountForm(request.POST, initial={'owner': customer})
        if form.is_valid():
            form.save()
        return redirect("/sampleapp/" + str(admin_id) + "/customers/" + str(id) + "/list")


def account_list(request, admin_id, id):
    customer = Customer.objects.get(pk=id)
    admin = get_adminitrator(admin_id)
    accounts = filter(lambda elem: elem.owner == customer, Account.objects.all())  # FIXME
    context = {"account_list": accounts,
               "customer_name": str(customer),
               "customer_id": id,
               "admin": admin,
               "editable": admin == customer.administrator, }
    return render(request, "sampleapp/account_list.html", context)
