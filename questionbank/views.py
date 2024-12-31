from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, UserQuestionStatus, UserSolvedQuestion
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    uid = request.user.id
    print("USER:",uid)
    filter_type = request.GET.get('filter', 'unsolved') #default unsolved
    search_query = request.GET.get('search', '').strip()  # Default to empty string
    toggle = request.GET.get('toggle', '').strip()
    
    print(toggle)
    if toggle:
        qid = int(toggle)
        solved_q = UserSolvedQuestion.objects.filter(question_id = qid, user_id = uid)
        # print(question.values())
        if solved_q:
            solved_q.delete()
        else:
            UserSolvedQuestion.objects.create(user_id = uid,
            question_id = qid)
        
    if filter_type == 'unsolved':
        questions = Question.objects.exclude(
            usersolvedquestion__user = uid
        )
    elif filter_type == 'solved':
        questions = Question.objects.filter(
            usersolvedquestion__user = uid
        )
    else:
        questions = Question.objects.all()
    if search_query:
        questions = questions.filter(title__icontains=search_query)
    solved_questions = Question.objects.filter(
            usersolvedquestion__user = uid
        )
    print("QUESTIONS:", questions)
    print("SOLVED QUES:", solved_questions)
    context = {
               'questions':questions,
               'solved_questions':solved_questions,
               'filter_type':filter_type,
               'search_query': search_query
               }
    return render(request, 'questionbank/index.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
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
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')
def user_signup(request):
    if  request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

    return render(request, 'questionbank/signup.html')

