from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.db.models.functions import Lower


@login_required
def all_posts(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    query = None
    sort = None
    direction = None
    post_type = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                posts = posts.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

        if 'post_type' in request.GET:
            categories = request.GET['post_type'].split(',')
            posts = posts.filter(post_type__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Get username
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
            # Clear comment field after save
            comment_form = CommentForm()
            # Redirect to avoid resubmission
            return redirect(reverse('post_detail', args=[post.slug]))
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


@login_required
def delete_own_comment(request, comment_id, slug):
    """ Delete own comment from the blog """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('post_detail', args=[post.slug]))
