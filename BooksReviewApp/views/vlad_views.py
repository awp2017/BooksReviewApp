# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import    View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LoginForm, BookRequestForm

class SignUpView ( CreateView ) :    
    form_class = UserCreationForm
    template_name = 'BooksReviewApp/signup.html'
    success_url = reverse_lazy( 'log-user' )
    
    
class SignInView(View):
    
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'BooksReviewApp/signin.html',{'form':form })    
    
    def post(self, request, *args, **kwargs):
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('home')
            else:
                context['error_message'] = 'Wrong username or password!'
        form = LoginForm()
        context['form'] = form
        context['error'] = 1
        return render(request, 'BooksReviewApp/Index.html', context)
        

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class SendRequestView(CreateView):
    form_class = BookRequestForm
    template_name = 'BooksReviewApp/sendrequest.html'
    success_url = reverse_lazy('home')