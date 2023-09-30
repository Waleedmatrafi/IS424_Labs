from django.shortcuts import render
from django.http import HttpResponse
taxRate = float(0.15)
# Create your views here.

def index(request, **amount):
    return render(request, "tax_calculator/index.html")
taxRate

def tax(request, amount):
    result = amount + (amount * (taxRate))
    return render(request, "tax_calculator/tax.html", {"amount": amount, "result": result})


def taxrate(request):
    taxper = taxRate*100
    return render(request, "tax_calculator/tax_rate.html", {"taxrate": taxper})