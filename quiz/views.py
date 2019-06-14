from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Question, Answer

# Create your views here.


def signin(request):
    return render(request, 'quiz/home.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['username']
        pas = request.POST['password']

        user = User.objects.create_user(name, pas)
        user.save()

        user.is_active = True
        return redirect('home')
    else:
        return render(request, 'quiz/signup.html')


def loginview(request):
    if request.method == 'POST':
        name = request.POST['username']
        pas = request.POST['password']
        user = authenticate(username=name, password=pas)
        if user is not None:
            login(request, user)
            return redirect('quiz')
        else:
            data = "You are not a authorized user"
            context = {'data': data}
            return render(request, 'quiz/signup.html', context)


def logoutview(request):
    logout(request)
    return redirect('home')


def quiz(request):
    if not request.user.is_authenticated:
        context = {'message': "You are not logged In Please Sign in First"}
        return render(request, 'quiz/home.html', context)
    var = Question.objects.all()

    context = {'data': var}

    # return HttpResponse(var.statement)
    return render(request, 'quiz/quiz.html', context)


def submit(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')
    # request.add("skjd","hkwh")
    stri = "/submit/" + str(pk) + "/result/"
    context = {'data': stri}
    return render(request, 'quiz/submit.html', context)


def process(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        ans = request.POST.get('answer')
        ques = Question.objects.get(pk=pk)
        answer = Answer.objects.create(question=ques, ans_statement=ans)
        answer.save()
        return HttpResponse("<h2>Your response is submitted</h2>")

