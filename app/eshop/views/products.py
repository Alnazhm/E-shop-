from django.contrib.auth.mixins import UserPassesTestMixin
from eshop.models import Product
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from eshop.forms import ProductForm
from django.urls import reverse
from django.urls import reverse_lazy
from eshop.models import Review
from django.db.models import Avg


class GroupPermission(UserPassesTestMixin):
    groups = []
    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class IndexView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'




class ProductView(DetailView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        avg_rate = Review.objects.filter(product=product).aggregate(avg=Avg('score'))
        reviews = Review.objects.filter(is_deleted=False, product=product)
        context['reviews'] = reviews
        context['avg_rate'] = avg_rate
        return context

class ProductCreateView(GroupPermission, CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product
    groups = ['moderators']

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(GroupPermission, UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    groups = ['moderators']

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})



class ProductDeleteView(GroupPermission, DeleteView):
    template_name = 'delete_confirm_page.html'
    model = Product
    success_url = reverse_lazy('products')
    groups = ['moderators']


