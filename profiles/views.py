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
    username, email
    """
    model = User
    form_class = AccountForm
    template_name = "profiles/user_account_edit.html"
    success_url = "."

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class that only allows authentic user to update their profile
    Composed of first_name,last_name,date_of_birth,gender,
    """
    model = User
    form_class = ProfileForm
    template_name = "profiles/user_profile_edit.html"
    success_url = "."

#List Views
class UserListView(ListView):
    """
    Class to list all the user
    """
    model = User
    template_name = "profiles/user_list.html"
    context_object_name = "users"

# Detail Views
class UserDetailView(DetailView):
    """
    Class to display user profile in detail
    """
    model = User
    template_name = "profiles/user_detail.html"
    #use username instead of pk
    slug_field = "username"
    #override the context user object from user to user_profile, user {{ user_profile }} instead of {{ user }} in template
    context_object_name = "user_profile"
