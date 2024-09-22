from django.shortcuts import render, redirect
from .models import Menu  # Import the Menu model
from .forms import NewLoginForm

def index(request):
    # Fetch dishes categorized into Appetizers, Main Courses, and Desserts
    appetizers = Menu.objects.filter(category='Appetizers')
    main_courses = Menu.objects.filter(category='Main Courses')
    desserts = Menu.objects.filter(category='Desserts')

    return render(request, 'index.html', {
        "appetizers": appetizers,
        "main_courses": main_courses,
        "desserts": desserts
    })

def add_dish(request):
    appetizers = Menu.objects.filter(category='Appetizers')
    main_courses = Menu.objects.filter(category='Main Courses')
    desserts = Menu.objects.filter(category='Desserts')

    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('description')
        p = request.POST.get('price')
        c = request.POST.get('category')
        if n and d and p and c:
            menu = Menu(name=n, description=d, price=p, category=c)
            menu.save()
            # Fetch dishes categorized into Appetizers, Main Courses, and Desserts

            return render(request,'add_dish.html',{"appetizers": appetizers,"main_courses": main_courses,"desserts": desserts})
        else:
            pass

    return render(request, 'add_dish.html',{"appetizers": appetizers,"main_courses": main_courses,"desserts": desserts})



def new_login(request):
    form = NewLoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("add/")
        else:
            form.add_error(None, "Invalid username or password")
    return render(request, "index.html", {"form": form})
    
    # form = NewLoginForm(request, data=request.POST or None)
    # if request.method == "POST" and form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect("/add-dish")
    #     else:
    #         form.add_error(None, "Invalid username or password")
    # return render(request, "index.html", {"form": form})
    # form = NewLoginForm(request, data=request.POST or None)
    # if request.method == "POST" and form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect("/add-dish")
    #     else:
    #         form.add_error(None, "Invalid username or password")

    # form = NewLoginForm(request, data=request.POST or None)
    # if request.method == "POST" and form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect("/add-dish")
    #     else:
    #         form.add_error(None, "Invalid username or password")

    # form = NewLoginForm(request.POST or None)

    # if request.method == "POST" and form.is_valid():
    #     u = form.cleaned_data.get("username")
    #     p = form.cleaned_data.get("password")
    #     print("username----->", u)
    #     print("password----->", p)

    # form = NewLoginForm(request, data=request.POST)
    # u = form.cleaned_data.get("username")
    # p = form.cleaned_data.get("password")
    # print("username----->", u)
    # print("password----->", p)
