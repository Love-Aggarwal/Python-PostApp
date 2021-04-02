from django.shortcuts import render, get_object_or_404, get_list_or_404,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import datetime
from django.conf import settings
from .models import Author, Tag, Category, Post
from django.contrib import messages,auth
from .forms import FeedbackForm
from django.core.mail import mail_admins
from django_project import helpers

def index(request):
    #return HttpResponse("Hello ! How are you")
    Context={
    'dict': { 'uno': 'one', 'dos': 'two', 'tres': 'three', 'cuatro': 'four' },
    'num':1,
    'now':datetime.datetime.now(),
    'my_code':"<p>Thia is good work done by you</p>",
    }
    
    return render(request,'post.html',Context)

def today_is(request):
    now = datetime.datetime.now()
    return render(request,'datetime.html', {'now': now ,'base_dir': settings.BASE_DIR})
    #html = "<html><body>Current date and time: {0}</body></html>".format(now)
    #return HttpResponse(html)
# Create your views here.

def post_list(request):
    posts = Post.objects.order_by("-id").all()#latest first ,ollder last
    posts = helpers.pg_records(request, posts, 5)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    posts = helpers.pg_records(request, posts, 3)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    posts = helpers.pg_records(request, posts, 3)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})

def test_cookie(request):   
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue')
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))

def track_user(request):
    if not request.COOKIES.get('visits'):
        response = HttpResponse("This is your first visit to the site. "
                                "From now on I will track your vistis to this site.")
        response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
    else:
        visits = int(request.COOKIES.get('visits')) + 1
        response = HttpResponse("This is your {0} visit".format(visits))
        response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    return response

def stop_tracking(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("Cookies Cleared")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("We are not tracking you.")
    return response

def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Testing session cookie")


def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie test passed")
    else:
        response = HttpResponse("Cookie test failed")
    return response

def save_session_data(request):
    # set new data
    request.session['id'] = 1
    request.session['name'] = 'root'
    request.session['password'] = 'rootpass'
    return HttpResponse("Session Data Saved")


def access_session_data(request):
    response = ""
    if request.session.get('id'):
        response += "Id : {0} <br>".format(request.session.get('id'))
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))

    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)


def delete_session_data(request):
    try:
        del request.session['id']
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")


def lousy_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "root" and password == "pass":
            request.session['logged_in'] = True
            return redirect('lousy_secret')
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'blog/lousy_login.html')


def lousy_secret(request):
    if not request.session.get('logged_in'):
        return redirect('lousy_login')
    return render(request, 'blog/lousy_secret_page.html')


def lousy_logout(request):
    try:
        del request.session['logged_in']
    except KeyError:
        return redirect('lousy_login')
    return render(request, 'blog/lousy_logout.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')


def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('blog_login')

    return render(request, 'blog/admin_page.html')