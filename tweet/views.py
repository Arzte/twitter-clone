from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

from tweet.forms import CreateTweetForm
from tweet.models import Tweet


def tweet_detail_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {
        'tweet': tweet,
        'display_name': tweet.author.get_full_name()
    })


@login_required
def create_tweet_view(request):
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()

            return HttpResponseRedirect(reverse('homepage'))

    form = CreateTweetForm()
    return render(request, 'generic_form.html', {'form': form})
