# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Cat
from django.contrib import messages

# Create your views here.
def index(request):
    cats = Cat.objects.all()
    cat_update = Cat.objects.all()
    context = {
        "cats":cats,
        "cats_to_edit":cat_update
    }
    return render(request, "cats_app/index.html", context)

def new(request):
    return render(request, "cats_app/new.html")

def create(request):
    errors = Cat.objects.validate_input(request.POST)
    if(len(errors) > 0):
        for error in errors:
            messages.error(request, error)
        return redirect("/new")
    else:
        new_cat = Cat.objects.create(name=request.POST["name"], age=request.POST["age"])
        return redirect("/")

def edit(request, id): #SHOWS US THE FORM
    cat = Cat.objects.filter(id = id).first()
    print cat
    context = {
        "cat":cat
    }
    return render(request, "cats_app/update.html", context)

def update(request, id): #HANDLES FORM SUBMISSION
    cat = Cat.objects.get(id = id)
    cat_name_to_update = request.POST["name"]
    cat_age_to_update = request.POST["age"]
    cat.name = cat_name_to_update
    cat.age = cat_age_to_update
    cat.save()
    return redirect("/cats")
