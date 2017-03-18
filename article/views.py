from django.shortcuts import render
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import auth
from django.core.paginator import Paginator

def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 3)
    return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})

@requires_csrf_token
def article(request, article_id=1, comment_number=1):
    all_comments = Comments.objects.filter(comments_article_id=article_id)
    current_comment = Paginator(all_comments, 3)
    comment_form = CommentForm
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = current_comment.page(comment_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article.html', args)

def addlike(request, article_id):
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    try:
        if article_id in request.COOKIES:
            return response
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response.set_cookie(article_id, "like")
            return response
    except ObjectDoesNotExist:
            raise Http404
    return response

def addcomment(request, article_id):
    if request.method == "POST" and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)