from django.http import HttpResponse

# Create your views here.
def index(request):
    test1 = request.session.get('test1')
    if not test1:
        request.session['test1'] = 'kourosh'

    print( request.session.get('test1') )
    return HttpResponse("<h1>website index</h1>")