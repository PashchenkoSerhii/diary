
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Nlp.forms import AddPostForm, RegisterUserForm, LoginUserForm
from Nlp.models import diary_entries
from Nlp.utils import DataMixin

menu = [{'title': "Додати запис", 'url_name': 'add'},
        {'title': "Мої записи", 'url_name': 'my'},
        {'title': "Про сайт", 'url_name': 'about'},
        {'title': "Підписка", 'url_name': 'pay'}
        ]

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Nlp/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        #  Use set_password here
        user.set_password(password)
        user.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'Nlp/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вхід")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def add(request):
    if request.method == 'POST':

        form = AddPostForm(request.POST)
        query = " "
        if request.POST.get("sub"):
            if form.is_valid():
                text = form.cleaned_data['text']

                diary_entries(text=form.cleaned_data['text'], user_id=request.user.id).save()

                return redirect('home')

        elif request.POST.get("rec"):
           """ r = sr.Recognizer()

            with sr.Microphone(device_index=1) as source:
                audio = r.listen(source)
            if audio:
                try:
                    query = r.recognize_google(audio, language='ru-RU')# uk-UA
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
            text = ''
            if form.is_valid():
                text = form.cleaned_data['text'] + " "
            text = text + query
            data = {'text': text}
            form = AddPostForm(initial=data)
            """
    else:
        data = {'text': ' '}
        form = AddPostForm(initial=data)
    return render(request, 'Nlp/add.html', {'form': form, 'menu': menu, 'title': 'Запис'})


def logout_user(request):
    logout(request)
    return redirect('login')

def about(request):
    context = {
        'menu': menu,
        'title': 'Про сайт'
    }
    return render(request, 'Nlp/about.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(diary_entries, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
    }
    return render(request, 'Nlp/post.html', context=context)


@login_required
def index(request):
    posts = diary_entries.objects.filter(user_id=request.user.id)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка'
    }
    return render(request, 'Nlp/index.html', context=context)

def pay(request):
    context = {
        'menu': menu,
        'title': 'Тариф'
    }
    return render(request, 'Nlp/pay.html', context=context)

