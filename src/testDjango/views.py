from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there"
    context = {"title": my_title}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,3,4,5]}
    return render(request, "home_page.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About Page"})

def contact_page(request):
    return render(request, "home_page.html", {"title": "Contact Page"})

def example_page(request):
    context         = {"title": "Hello There!"}
    template_name  = "home_page.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))