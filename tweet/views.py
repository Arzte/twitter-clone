import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser


class TweetDetailView(DetailView):
    model = Tweet
    template_name = "tweet_detail.html"


class CreateTweetView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['text']
    template_name = 'generic_form.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        regex = re.compile(r"@(\w*)")
        users = regex.findall(form.data.get('text'))
        for user in users:
            Notification.objects.create(
                tweet=form.save(),
                user=TwitterUser.objects.get(username=user),
                mentioned_by=self.request.user
            )

        return super().form_valid(form)
