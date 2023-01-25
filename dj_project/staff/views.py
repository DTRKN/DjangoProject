from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World')

def detail(request, article_id):
    return HttpResponse("You're looking at staff %s." % article_id)

def result(request, article_id):
    responce = "You're looking at result staff %s."
    return HttpResponse(responce % article_id)

def vote(request, article_id):
    return HttpResponse("You're voting on staff %s." % article_id )