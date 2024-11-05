from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from account.fomrs import LoginUserForm

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
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return render(request, "account/register.html",
            {
                "error":"Parolalar Eşleşmiyor",
                "email":email,
                "username":username,
            })
        
        if User.objects.filter(username = username).exists():
            return render(request, "account/register.html",
            {
                "error":"Kullanıcı adı zaten kullanılıyor",
                "email":email,
                "username":username,
            })
        
        if User.objects.filter(email = email).exists():
            return render(request, "account/register.html",
            {
                "error":"Bu email ile zaten bir hesap açılmış.",
                "email":email,
                "username":username,
            })
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        return redirect("user_login")

    else:
        return render(request, "account/register.html")

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Çıkış Yapıldı")
    return redirect("home")