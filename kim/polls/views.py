from django.http import HttpResponse #django.http라는 모듈 안에서 HttpResponse라는 것을 import

def index(request):
    return HttpResponse("polls index.") #index라는 request받을거고 request 받으면 return Http포맷으로 리턴
   
def detail(request, question_id):
    return HttpResponse("You're looking at question %s" %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
