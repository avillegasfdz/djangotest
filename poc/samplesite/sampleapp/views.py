from django.http import HttpResponse
from django.template import loader
from django.shorcuts import render, redirect

from sampleapp.models import Customer, Administrator, Account

from .forms import CustomerForm

def index(request):
    if Administrator.objects.all():
        Customer.objects.all().delete()
        Administrator.objects.all().delete()

    admin1 = Administrator(name="Admin 1")
    admin1.save()

    admin2 = Administrator(name="Admin 2")
    admin2.save()

    customer1 = Customer(name="Juan", last_name="Perez", administrator_id=admin1.id)
    customer2 = Customer(name="Lucas", last_name="García", administrator_id=admin1.id)
    customer3 = Customer(name="Marta", last_name="Perez", administrator_id=admin2.id)

    customer1.save()
    customer2.save()
    customer3.save()

    acc1 = Account(owner=customer1, iban="DE89370400440532013000")
    acc2 = Account(owner=customer1, iban="DE89370400440532013150")
    acc3 = Account(owner=customer3, iban="DE89370400990532013000")

    acc1.save()
    acc2.save()
    acc3.save()

    # admins_str = " ".join(list(map(lambda elem: elem.name, Administrator.objects.all())))
    # customers_str = " ".join(list(
    #     map(lambda elem: elem.name + " " + elem.last_name + " " + str(elem.administrator_id), Customer.objects.all())))
    # accounts_str = " ".join(list(map(lambda elem: elem.iban + " " + str(elem.owner), Account.objects.all())))
    #
    # return HttpResponse("Hello, world! \n" + "ADMINS: " + admins_str + "\n" +
    #                     "CUSTOMERS: " + customers_str + "\n" +
    #                     "ACCOUNTS: " + accounts_str + "\n")

    administrator_list = [admin1, admin2]
    customer_list = [customer1, customer2, customer3]

    template = loader.get_template('sampleapp/index.html')
    context = {
        'administrators': administrator_list,
        'customers': customer_list,
    }
    return HttpResponse(template.render(context, request))


def customer_list(request):
    context = {"customer_list": Customer.objects.all()}
    return render(request, "sampleapp/customer_list.html", context)


def customer_form(request, id=None):
    if request.method == "GET":
        if not id:  # Insert operation
            form = CustomerForm()
        else:  # Update Operation
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)

        return render(request, "sampleapp/customer_form.html", {"form":form})
    else:
        if not id:  # Insert operation
            form = CustomerForm(request.POST)
        else:  # Update Operation
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance=customer)

        if form.is_valid():
            form.save()
        return redirect("/sampleapp/list")



def customer_delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect("/sampleapp/list")