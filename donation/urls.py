from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from donation.views import DonationList, UserList

app_name = 'donation'
urlpatterns = [
    path('', DonationList.as_view(), name='index'),
    path('users/', UserList.as_view(), name='user_list'),
    path('accounts/login/', LoginView.as_view(extra_context={
        'next': reverse_lazy('product:list')
    }), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page=
        reverse_lazy('product:list')
    ), name='logout'),
]