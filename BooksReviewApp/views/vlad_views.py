# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LoginForm, BookRequestForm, ReviewForm
from ..models import BookRequest, Book, Writer
from .dan_views import WriterHelper

class SignUpView (CreateView, WriterHelper) :    
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
                context['error'] = 1
                context['error_message'] = 'Wrong username or password!'
        form = LoginForm()
        context['form'] = form
        context['writer_list'] = Writer.objects.all()
        return render(request, 'BooksReviewApp/Index.html', context)
        

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('log-user')

class SendRequestView(LoginRequiredMixin, CreateView, WriterHelper):
    form_class = BookRequestForm
    template_name = 'BooksReviewApp/sendrequest.html'
    success_url = reverse_lazy('home')
    login_url = "log-user"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(SendRequestView, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        
        context = super(SendRequestView,self).get_context_data()
        context['writers_list'] = self.getWriters()
        
        return context
        
class ApproveRequestView(LoginRequiredMixin, ListView,  WriterHelper):

    model = BookRequest
    context_object_name = 'request_list'
    template_name = 'BooksReviewApp/requests.html'
    login_url = "log-user"
    def get(self, request, *args, **kwargs):
        
        if self.request.user.has_perm('BooksReviewApp.add_Review'):
            return super(ApproveRequestView,self).get(self, request, *args, **kwargs)
        
        return redirect('home')
    
    def get_context_data(self, **kwargs):
        
        context = super(ApproveRequestView,self).get_context_data()
        context['writer_list'] = self.getWriters()
       
        
        return context


class AcceptRequestView(LoginRequiredMixin, CreateView,  WriterHelper):

    model = BookRequest
    template_name = 'BooksReviewApp/AddReview.html'
    login_url = "log-user"
    form_class = ReviewForm
    success_url = reverse_lazy('home')
    def get(self, request, *args, **kwargs):
        req = BookRequest.objects.get(id=self.kwargs['pk'])
        book = Book()
        writer = Writer()
        writer.name = req.writer
        writer.save()
        book.name = req.book_name
        book.save()
        book.writers.add(writer)
        book.save()
        req.delete()
        if self.request.user.has_perm('BooksReviewApp.add_Review'):
            return super(AcceptRequestView,self).get(self, request, *args, **kwargs)
        return redirect('home')

    
    def form_valid(self, form):
        form.instance.author_pk = self.request.user
        return super(AcceptRequestView, self).form_valid(form)
        

