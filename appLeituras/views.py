import datetime
from django.http import HttpResponse


def lista_leituras(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
