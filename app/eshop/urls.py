from eshop.views import IndexView, ProductCreateView, ProductView, ProductUpdateView, ProductDeleteView, ReviewAddView, ReviewDeleteView, ReviewEditView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='products'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name="product_edit"),
    path('products/deleted/<int:pk>', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<int:pk>/product_add_basket', IndexView.as_view(), name='products'),
    path('products/<int:pk>/review/add/', ReviewAddView.as_view(), name='review_create'),
    path('reviews/edit/<int:pk>', ReviewEditView.as_view(), name='review_edit'),
    path('reviews/deleted/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('reviews/deleted/<int:pk>', ReviewDeleteView.as_view(), name='confirm_delete_review'),
    path('reviews/add/', ReviewAddView.as_view(), name='review_create')
]