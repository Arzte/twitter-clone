from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

from tweet.models import Tweet
from twitteruser.models import TwitterUser


@login_required
def index_view(request):
    following = request.user.following.all()
    timeline = []
    has_tweets = Tweet.objects.filter(author=request.user)
    if has_tweets:
        for tweet in has_tweets:
            timeline.append(tweet)

    for follower in following:
        follower_has_tweets = Tweet.objects.filter(author=follower)
        if follower_has_tweets:
            for tweet in follower_has_tweets:
                timeline.append(tweet)

    return render(request, 'index.html', {
        'timeline': timeline,
        'display_name': request.user.get_full_name()
    })


def user_detail_view(request, username):
    user = TwitterUser.objects.get(username=username)
    following = request.user.following.all().filter(username=username)
    tweet_count = Tweet.objects.filter(author=user).count()
    following_count = user.following.count()
    return render(request, 'user_detail.html', {
        'user': user,
        'following': following,
        'tweet_count': tweet_count,
        'following_count': following_count,
        'display_name': user.get_full_name()
    })


@login_required
def follow_user_view(request, username):
    user = TwitterUser.objects.get(username=username)
    following = user.following.all().filter(username=username)
    current_user = request.user
    if not following:
        user.followers.add(request.user)
        current_user.following.add(user)
        user.save()
        current_user.save()
    else:
        user.followers.remove(request.user)
        current_user.following.remove(user)
        user.save()
        current_user.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
