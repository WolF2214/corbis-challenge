from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from .models import Item
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('items')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('items')
        return super(RegisterPage, self).get(*args, **kwargs)
 
class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'item_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = context['items'].filter(user=self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['items'] = context['items'].filter(name__startswith=search_input)
        context['search_input'] = search_input
        return context

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['code', 'name', 'tipe', 'price', 'quantity']
    success_url = reverse_lazy('items')
    template_name = 'item_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['code', 'name', 'tipe', 'price', 'quantity']
    success_url = reverse_lazy('items')
    template_name = 'item_form.html'
    
class ItemDeleted(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('items')
    template_name = 'item_confirm_delete.html'