from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate =0.15
def index(request):
    return HttpResponse('<h2>this is a site to calculate tax<h2>')
def number(request,n):
    total = float(n) + float(n) *tax_rate 

    return HttpResponse(f'<h1>total with tax is {total}<h1>')

# def number(request,n):
#     total = n + n *tax_rate 

#     return HttpResponse(f'<h1>total with tax is {total}<h1>')

# def taxr(request):
#     return HttpResponse(f"tax rate is {tax_rate}")
def taxr(request):
    return HttpResponse(f"<h1>tax rate is {tax_rate} <h1>")


