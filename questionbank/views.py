from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, UserQuestionStatus
# Create your views here.
def index(request):
    filter_type = request.GET.get('filter', 'unsolved') #default unsolved
    search_query = request.GET.get('search', '').strip()  # Default to empty string
    toggle = request.GET.get('toggle', '').strip()
    print(toggle)
    if toggle:
        question = UserQuestionStatus.objects.filter(question =toggle)
        # print(question.values())
        for q in question.values():
            # print(q)
            if q['status'] == "Solved":
                UserQuestionStatus.objects.filter(question =toggle, 
                status = 'Solved').update()
            else:
                q['status'] = "Solved"
    if filter_type == 'unsolved':
        questions = Question.objects.filter(
            userquestionstatus__user = 1,
            userquestionstatus__status = 'Unsolved'
        )
    elif filter_type == 'solved':
        questions = Question.objects.filter(
            userquestionstatus__user = 1,
            userquestionstatus__status = 'Solved'
        )
    else:
        questions = Question.objects.all()
    if search_query:
        questions = questions.filter(title__icontains=search_query)
    context = {
               'questions':questions,
               'filter_type':filter_type,
               'search_query': search_query
               }
    return render(request, 'questionbank/index.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.info(request, "You have successfully logged in.")
            print("user Logged in")
            return redirect('index')  # Redirect to your home page
        else:
            messages.error(request, "Invalid username or password.")
            print("Invalid USER / Password")
    return render(request, 'questionbank/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
    return render(request, 'questionbank/signup.html')

