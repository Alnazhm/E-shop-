from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView, CreateView
from eshop.models import Review
from eshop.forms import ReviewForm

from eshop.models import Product


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/'
    template_name = 'review_confirm_delete.html'


class ReviewEditView(UpdateView):
    template_name = 'review_edit.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    success_url = '/'



class ReviewAddView(CreateView):
    template_name = 'create_review.html'
    form_class = ReviewForm
    model = Review
    success_url = '/'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)

