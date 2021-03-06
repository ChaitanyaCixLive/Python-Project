import datetime

from django.shortcuts import render
from .models import Article, Feed
from .froms import FeedForm
from django.shortcuts import redirect
import feedparser as fp
# Create your views here.


def articles_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'news/articles_list.html', context)


def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})


def feed_new(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            feedDate = fp.parse(feed.url)

            # set some fields
            feed.title = feedDate.feed.title
            form.save()

            for entry in feedDate.entries:
                artile = Article()
                artile.title = entry.title
                artile.url = entry.link
                artile.description = entry.description

                d = datetime.datetime(*(entry.published_parsed[0:6]))
                dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                artile.publication_date = dateString
                artile.feed = feed
                artile.save()

            return redirect('/news/feeds/feeds_list.html')
    else:
        form = FeedForm()
        return render(request, 'news/new_feed.html', {'form': form})

