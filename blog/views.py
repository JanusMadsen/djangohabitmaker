from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Record
from .functions import checkday, create_record, streakfunc
from.forms import RegistrationForm, EditForm, EdithabitForm

# Create your views here.


def indexpage(request):
    return redirect('/main/')

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/main/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutpage(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/main/')


def signuppage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            p1 = Profile(user=user)
            p1.save()
            p2 = Record(user=user)
            p2.save()
            login(request, user)
            return redirect('/main/')
    else:
        form = RegistrationForm()
    return render(request, "signup.html", {"form": form})

@login_required(login_url='/login/')
def mainpage(request):
    profiles = request.user.followers.all()
    if request.method == "POST":
        if request.user.profile.color == "#32CD32":
            request.user.profile.color = "#FF0000"
            request.user.profile.hovercolor = "#da190b"
            request.user.profile.streak -= 1
        elif request.user.profile.color == "#FF0000":
            request.user.profile.color = "#32CD32"
            request.user.profile.hovercolor = "#228B22"
            request.user.profile.streak += 1
        request.user.profile.save()
        hotstreak = streakfunc(request.user.profile)
        liste = create_record(request.user)
    else:
        liste = create_record(request.user)
        checkday(request.user.profile)
        hotstreak = streakfunc(request.user.profile)
        for i in profiles:
            checkday(i)
        checkday(request.user.profile)



    return render(request, 'main.html', {'liste': liste, "profiles": profiles, "streak": hotstreak})

@login_required(login_url='/login/')
def followerpage(request):
    context = {}
    profiles = Profile.objects.all()
    if request.method == "POST":
        id = request.POST["userprofile"]
        following = request.POST["following"]
        profile = Profile.objects.get(id= id)
        if following == "following":
            profile.followers.remove(request.user)
        elif following == "notfollowing":
            profile.followers.add(request.user)
    else:
        pass
    is_following = request.user.followers.all()
    context['profiles'] = profiles
    context["following"] = is_following
    return render(request, 'following.html', context)

@login_required(login_url='/login/')
def profilepage(request):
    if request.method == 'POST':
        id = request.POST["action"]
        if id == 'profile':
            return redirect('edit/')
        elif id == 'password':
            return redirect('password/')

    return render(request, 'profilepage.html', {})

@login_required(login_url='/login/')
def profileeditpage(request):
    if request.method == 'POST':
        formstandard = EditForm(request.POST, instance=request.user)
        formhabit = EdithabitForm(request.POST, instance=request.user.profile)
        if formhabit.is_valid() and formstandard.is_valid():
            formhabit.save()
            formstandard.save()
            return redirect('/profilepage/')
    else:
        formstandard = EditForm(instance=request.user)
        formhabit = EdithabitForm(instance=request.user.profile)


    return render(request, 'profileedit.html', {'formstandard': formstandard, 'formhabit': formhabit})


@login_required(login_url='/login/')
def changepasswordpage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profilepage/')

        else:
            return redirect('/profilepage/password/')


    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "changepassword.html", {"form": form})

