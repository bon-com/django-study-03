from django.shortcuts import render


def hello(request):
    """Hello Worldの表示"""
    return render(request, "hello.html")
