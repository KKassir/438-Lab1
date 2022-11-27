from django.shortcuts import (render,redirect)
from .forms import TelephoneForm
from .models import Telephone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db.models import Q


# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = TelephoneForm(request.POST)
    if form.is_valid():
      form.save()
  contacts = Telephone.objects.all().order_by('name','profession').values()
  form = TelephoneForm()
  return render(request, "home.html", {"form": form, "contacts":contacts})



def destroy(request, id):
  contact = Telephone.objects.get(id=id)
  contact.delete()
  return(redirect('/'))


def update(request, id):
  contact = Telephone.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'contact': contact,
  }
  return HttpResponse(template.render(context, request))


def updatecontact(request, id):
  name = request.POST['name']
  profession = request.POST['profession']
  tel_num = request.POST['tel_num']
  mob_num = request.POST['mob_num']
  contact = Telephone.objects.get(id=id)
  contact.name = name
  contact.profession= profession
  contact.tel_num= tel_num
  contact.mob_num= mob_num
  contact.save()
  return(redirect('/'))

def searchbyname(request):
  return render(request,'searchname.html',{})

def searchNT(request):
  if request.method == "POST":
    searched = request.POST.get('searched')
    contacts= Telephone.objects.filter(Q(name__contains=searched) | Q(tel_num__contains=searched)).order_by('name','profession').values()
    return render(request, "searchname.html", {'searched':searched, 'contacts':contacts})
  else:
    return render(request, "searchname.html", {})

def searchP(request):
  if request.method == "POST":
    searched1 = request.POST.get('searched1')
    contacts= Telephone.objects.filter(profession__contains=searched1).order_by('name','profession').values()
    return render(request, "searchname.html", {'searched1':searched1, 'contacts':contacts})
  else:
    return render(request, "searchname.html", {})


def comparepage(request):
  return render(request,'compare.html',{})


def compare(request):
  if request.method == "POST":
    fname = request.POST.get('fname')
    contacts1= Telephone.objects.filter(Q(name__contains=fname)).order_by('name','profession').values()
    sname = request.POST.get('sname')
    contacts2= Telephone.objects.filter(Q(name__contains=sname)).order_by('name','profession').values()
    return render(request, "compare.html", {'contacts1':contacts1, 'contacts2':contacts2 , 'fname':fname , 'sname' : sname})
  else:
    return render(request, "compare.html", {})
