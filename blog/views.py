from urllib import request
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Post,Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog.html'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['popular_posts'] = Post.objects.order_by('-hit_count_generic__hits')[:3]
        return context


class PostDetail(HitCountDetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['popular_posts'] = Post.objects.order_by('-hit_count_generic__hits')[:3]
        comments_connected = Comment.objects.filter(
            blogpost_connected=self.get_object()).order_by('-date_created')
        context['comments'] = comments_connected
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)

        

        # return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(comment_field=request.POST.get('comment_field'),
                                  name=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

