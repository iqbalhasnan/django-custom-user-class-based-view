#class based view import for list User
from django.views.generic.list import ListView
#class based view import for displaying User
from django.views.generic.detail import DetailView
#class based view import for editing User
from django.views.generic.edit import UpdateView

#method decorator
from django.utils.decorators import method_decorator

#import User models and User forms
from .forms import ProfileForm, AccountForm
from .models import User
from .mixins import LoginRequiredMixin



#From Views
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class that only allows authentic user to update their account
    username, email,is_private, location,latitude,longitude,country
    """
    model = User
    form_class = AccountForm
    template_name = "profiles/user_account_edit.html"
    success_url = "."

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class that only allows authentic user to update their profile
    Composed of first_name,last_name,date_of_birth,gender,website,twitter,description
    """
    model = User
    form_class = ProfileForm
    template_name = "profiles/user_profile_edit.html"
    success_url = "."

#List Views
class UserListView(ListView):
    model = User
    template_name = "profiles/user_list.html"
    context_object_name = "users"

# Detail Views
class UserDetailView(DetailView):
    model = User
    template_name = "profiles/user_detail.html"
    #use username instead of pk
    slug_field = "username"
    #override the context user object from user to user_profile
    context_object_name = "user_profile"
