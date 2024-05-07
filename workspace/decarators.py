from django.shortcuts import redirect
from django.urls import reverse

def login_required(login_url=None):
   def decarator(func):
      def inner(request, *arrgs, **kwargs):
         if not request.user.is_authenticated:
            url = reverse('login') if login_url is None else login_url
            return redirect(url)
         return func(request, *arrgs, **kwargs)
      return inner
   return decarator
