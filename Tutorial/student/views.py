# from django.shortcuts import render

from django.http import HttpResponse

# from .models import Student

# Create your views here.
# def student_show(request):
#     x = []
#     for i in range(1,10):
#         x.append(i)
#     return HttpResponse('<h1>Django view </h1>The digits are {0}'.format(x))

# def student_show(request):
#     student = Student.objects.order_by('roll_no')
#     return render(request,'student/student_show.html',{'student':student})


def index(request):
    html = """ <h1>This is h1 tag in HTML </h1> You just config  the first URL."""
    return HttpResponse(html)