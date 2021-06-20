from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Django sessions</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Django<br> cookie createed")
    else:
        response = HttpResponse("Django<br> Your browser doesnot accept cookies")
    return response




    