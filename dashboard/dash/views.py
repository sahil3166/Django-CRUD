from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')

    if request.method == 'POST':
        username = request.POST.get('email')
        print(username)
        # user = authenticate(request, username=username)
        # print(user,'fffffffffff')
        user = User.objects.filter(username=username)

        if not user:
            User.objects.create(
                                first_name=request.POST.get('name'),
                                username=request.POST.get('email'),
                                password=make_password(request.POST.get('password')))
            messages.success(request, f"New account created")
            return redirect(signup)

        else:
            messages.error(request, f"Account Already Present!!")
            return redirect(signup)


def user_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            messages.error(request, f"User Not Present!!")
            return redirect(user_login)


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'home/tables.html')


def user_logout(request):
    logout(request)
    return redirect(user_login)


@login_required(login_url='/login/')
def category(request):
    if request.method == 'GET':
        crud = Category.objects.all()
        paginator = Paginator(crud, 3)
        page_num = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request, 'home/icons.html', {'cruds': crud, 'page_obj': page_obj})


@login_required(login_url='/login/')
def products(request):
    crud = Products.objects.all()

    if request.method == 'GET':
        paginator = Paginator(crud, 4)
        page_num = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        print(crud)
        return render(request, 'home/map.html', {'cruds': crud, 'page_obj': page_obj})


def read(request):
    if request.method == 'POST':
        crud = Category.objects.all()
        return render(request, 'home/icons.html', {'cruds': crud})


def delete(request):
    if request.method == 'POST':
        name = request.POST.get("delete")
        crud = Category.objects.filter(name=name)
        crud.delete()

        return render(request, "home/icons.html", {"cruds": crud})


def update(request):
    name = request.POST.get("update")
    crud = Category.objects.get(name=name)
    if request.method == 'POST':
        crud.name = name


        crud.save()

    return render(request, 'home/icons.html')


@login_required(login_url='/login/')
def categoryAdd(request):
    if request.method == 'GET':
        return render(request, 'home/categoryAdd.html')

    if request.method == 'POST':
        name = request.POST.get('category')
        cat = Category.objects.filter(name=name)

        if not cat:
            Category.objects.create(
                                    name=request.POST.get('category'),
            )
            return redirect(category)

        else:
            messages.error(request, f"Category Already Present!!")
            return redirect(categoryAdd)


def categoryDelete(request, id):
    if request.method == 'GET':
        cat = Category.objects.get(id=id)
        # crud = Category.objects.filter(name=cat)
        print(cat)
        cat.delete()
        return redirect(category)


def categoryUpdate(request, id):
    crud = Category.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'home/categoryUpdate.html', {'cruds': crud})

    if request.method == 'POST':
        name = request.POST.get('category')
        crud.name = name
        crud.save()
        return redirect(category)


def productAdd(request):
    crud = Category.objects.all()
    if request.method == "GET":
        return render(request, 'home/productAdd.html', {'cruds': crud})

    if request.method == 'POST':

        print(request.FILES.getlist('image'),'ddd')

        # raise
        product=Products.objects.create(
                                name=request.POST.get('name'),
                                price=request.POST.get('price'),
                                category_name_id=request.POST.get('category'),
                                description=request.POST.get('description'),
        )
        for i in request.FILES.getlist('image'):
            ProductImage.objects.create(product=product,image=i)
        return redirect(products)


# def productImage(request, id):
#     pro = Products.objects.get(id=id)
#     images = pro.images.all()
#     if request.method == 'GET':
#         return render(request, 'home/productAdd.html')
#
#     if request.method == 'POST':
#         ProductImage.objects.create(
#
#         )





def productDelete(request, id):
    if request.method == 'GET':
        pro = Products.objects.get(id=id)
        print(pro)
        pro.delete()
        return redirect(products)


def productUpdate(request, id):
    crud = Products.objects.get(id=id)
    cat = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'home/productUpdate.html', {'cruds': crud, 'cats': cat})

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_name_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.POST.get('image')
        crud.name = name
        crud.price = price
        crud.category_name_id = category_name_id
        crud.description = description
        crud.image = image
        crud.save()
        return redirect(products)


def productView(request, id):
    crud = Products.objects.get(id=id)
    # prod = Products.objects.all()
    # cat = Category.objects.all()

    # print(ProductImage.objects.filter(product=crud))
    if request.method == 'GET':
        return render(request, 'home/productView.html', {'cruds': crud})


def profile(request):
    user = User.objects.all()
    if request.method == 'GET':
        return render(request, 'home/profile.html', {'users': user})

    if request.method == 'POST':
        User.objects.create(
                            email=request.POST.get('email'),
                            first_name=request.POST.get('first_name'),
                            last_name=request.POST.get('last_name'),
                            address=request.POST.get('address'),
                            city=request.POST.get('city'),
                            country=request.POST.get('country'),
                            pincode=request.POST.get('pincode'),
                            aboutme=request.POST.get('aboutme')
        )
        return redirect(profile)