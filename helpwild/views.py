from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from .models import Quiz, Donate, Comments, Customer
from .forms import DonateForm, QuizForm, CommentsForm, CreateUserForm
from .quizFunctions import cria_grafico
from bs4 import BeautifulSoup

import stripe
import matplotlib
import requests

matplotlib.use('Agg')


stripe.api_key = "sk_test_51LH4PgAwFMTHlXsi1mRlkYlriTDYUqrPO62PgH8Mbv2O7VOGOfpvs6V0mHHRb992PCRSLREGJhf9JuBwcyvEecOJ00bzl2wtfg"

# Home Page


def home_page_view(request):

    home_news_header = []
    img = []

    url_home = 'https://www.nbcnews.com/animal-news/'
    response = requests.get(url_home)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines_home = soup.find('body').find_all(
        class_='wide-tease-item__headline')

    for i in headlines_home:
        home_news_header.append(i.text.strip())
    # print("news:",x.text.strip())

    images = soup.findAll('img')

    for image in images:
        # print image source
        img.append(image['src'])

    return render(request, 'helpwild/home.html', {'home_news_header': home_news_header, 'img': img})


def teams_page_view(request):
    return render(request, 'helpwild/teams.html')


def timeline_page_view(request):
    return render(request, 'helpwild/timeline.html')

# # ================================================Login&Register=============================================


def register_page_view(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            # Added username after video because of error returning customer name if not added
            Customer.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('helpwild:login')

    context = {'form': form}
    return render(request, 'helpwild/register.html', context)


def login_page_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('helpwild:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'helpwild/login.html', context)

@login_required
def profile_page_view(request):  

    

    context = {'customer': Customer.objects.all()}
    return render(request, 'helpwild/profile.html', context)


def logout_page_view(request):
    logout(request)
    return render(request, 'helpwild/home.html')


def rec_pass_page_view(request):
    return render(request, 'helpwild/recover_password.html')


# =========================================Login&Register==================================================


# =============================================Donations Page==============================================
# Donate Page

def donate_page_view(request):

    form = DonateForm(request.POST or None)

    count = 0

    for i in Donate.objects.all():
        count = count + i.value

    best3 = sorted(Donate.objects.all(), key=lambda i: i.value, reverse=True)

    context = {'value': count,
               'best3': best3[0:3], "form": form}

    return render(request, 'helpwild/donate.html', context)


# Charge Process


def charge(request):

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['value'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['cardname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description="Donation"
        )
        form = DonateForm(request.POST or None)
        if form.is_valid():
            form.save()
            customer = form.cleaned_data.get("customer")
            amount = form.cleaned_data.get("value")
            donate = authenticate(customer=customer, amount=amount)

            # return HttpResponseRedirect(reverse('helpwild:success'))

    return redirect(reverse('helpwild:success', args=[amount]))

# SuccessMsg Page


def successMsg_page_view(request, args):
    amount = args

    # form = DonateForm(request.POST)
    # if form.is_valid():
    #     form.save()

    return render(request, 'helpwild/success.html', {'amount': amount})

# ================================================Donations Page=============================================

# ================================================News Page===================================================

# Função que coleta noticias de um outro website e coloca-as filtrdas neste website


def news_page_view(request):

    news_header = []
    news_body = []
    news_header_big = []
    img = []
    link = []

    url = 'https://www.nbcnews.com/animal-news/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # ========NewsPage Headers=========
    headlines = soup.find('body').find_all(class_='wide-tease-item__headline')

    for x in headlines:
        news_header.append(x.text.strip())

    # ========NewsPage Bodys=========

    bodylines = soup.find('body').find_all(
        class_="wide-tease-item__description")
    for x in bodylines:
        news_body.append(x.text.strip())

    # ========NewsPage Headers BigNews========

    headlinesbig = soup.find('body').find_all(
        class_="tease-card__headline tease-card__title tease-card__title--news relative")

    for x in headlinesbig:
        news_header_big.append(x.text.strip())

    # ========NewsPage Images=========

    images = soup.findAll('img')

    for image in images:
        img.append(image['src'])

    # =========NewsPage Links to news on NBCNews========

    page_link = soup.findAll(class_='tease-card__picture-link', href=True)

    for i in page_link:
        link.append(i['href'])

    # ========NewsPage Filtragem da informação que vem do Link=========

    url2 = link[1]
    response2 = requests.get(url2)
    soups = BeautifulSoup(response2.text, 'html.parser')

    bodybigs = soups.find('body').find_all(
        class_='styles_articleDek__Icz5H')

    for xs in bodybigs:
        news_body_big = (xs.text.strip())

    # ========Context todas as funcionalidades===========

    context = {
        'news_header': news_header,
        'news_body': news_body,
        'news_header_big': news_header_big,
        'img': img,
        'link': link,
        'news_body_big': news_body_big
    }

    return render(request, 'helpwild/news.html', context)

# ===================================================News Page========================================================

# Quiz Page


def quiz_page_view(request):

    form = QuizForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = QuizForm()
    context = {'form': form, 'data': cria_grafico(
        Quiz.objects.all()), 'comment': Comments.objects.all()}

    return render(request, 'helpwild/quiz.html', context)


def new_Comments_view(request):
    form = CommentsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('helpwild:quiz'))

    context = {'form': form}
    return render(request, 'helpwild/newcomment.html', context)


def edit_Comments_view(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    form = CommentsForm(request.POST or None, instance=comment)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('helpwild:quiz'))

    context = {'form': form, 'comment_id': comment_id}
    return render(request, 'helpwild/editcomment.html', context)


@login_required
def delete_Comments_view(request, comment_id):
    Comments.objects.get(id=comment_id).delete()
    return HttpResponseRedirect(reverse('helpwild:quiz'))
