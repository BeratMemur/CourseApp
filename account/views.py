from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from account.fomrs import ChangePasswordForm, LoginUserForm, NewUserForm
from django.contrib.auth.forms import PasswordChangeForm

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error": "Yetkiniz Yok"})
    
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş Başarılı")
                nexturl = request.GET.get("next", None)
                if nexturl is None:
                    return redirect("home")
                else:
                    return redirect(nexturl)
            else:
                return render(request, "account/login.html", {"form":form})
        else:
            return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})


def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"] 
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password = password)
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form": form})


def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Parola Güncellendi")
            return redirect("change_password")
        else:
            return render(request, "account/change-password.html", {"form": form})

    else:
        form = ChangePasswordForm(request.user)
        return render(request, "account/change-password.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Çıkış Yapıldı")
    return redirect("home")