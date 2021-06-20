from django.shortcuts import render

# Create your views here.
def page_count(request):
    count = request.session.get('count', 0)
    newcount = count+1
    request.session['count'] = newcount
    return render(request, 'page.html', {"count": newcount})