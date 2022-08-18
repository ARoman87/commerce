from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *



def index(request):
    listings = Listing.objects.filter()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



# ------------ Create New Listing ----------  #

def create(request):
    form = CreateForm()
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            if "preview" in request.POST:
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect("preview", form.pk)  
            if "submit" in request.POST:
                form = form.save(commit=False)
                form.user = request.user
                form = form.save()
                return HttpResponseRedirect("/listings")

    return render(request, "auctions/create.html", {
        "form": form,
        
    })


# ---------- Previews Listing ------------   #

def preview(request, pk):
    listing = Listing.objects.get(id=pk)
    return render(request, "auctions/preview.html", {
        "list": listing
    })

def listings(request):
    listings = Listing.objects.filter(user=request.user)
    return render(request, "auctions/listings.html", {
        "listings": listings,
    })

def edit(request, pk):
    listing = Listing.objects.get(id=pk)
    form = CreateForm(instance=listing)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=listing)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/listings")
            
    return render(request, "auctions/edit.html", {
        "form": form,
        "list": listing
    })
    
def delete(request, pk):
    listing = Listing.objects.get(id=pk)
    if request.method == "POST":
        listing.delete()
        return HttpResponseRedirect("/listings")
    return render(request, "auctions/delete.html", {
        "list": listing,
    })

def search(request):
    search = request.POST["q"]
    title = Listing.objects.filter(title__icontains=search)
    return render(request, "auctions/search.html", {
        "search": search,
        "title": title,
    })

def listItem(request, pk):
    listings = Listing.objects.get(id=pk)
    return render(request, "auctions/list-item.html", {
        "listings": listings
    })


def wishlist(request):
    return render(request, "auctions/wishlist.html")