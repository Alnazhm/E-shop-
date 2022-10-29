from django.views.generic import UpdateView, DeleteView, CreateView
from eshop.models import Review
from eshop.forms import ReviewForm


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
        form.instance.product_id = self.kwargs['pk']
        return super(ReviewAddView, self).form_valid(form)

