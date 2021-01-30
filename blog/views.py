from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.db.models.functions import Lower
from .decorators import login_required_message


@login_required_message(message="Sorry you need to be a registered \
                        user to access our blogs")
@login_required
def all_posts(request):
    """
    A view to show all blog posts, including sorting and filtering by
    post type
    """
    posts = Post.objects.filter(status=1).order_by('-created_on')
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                posts = posts.annotate(lower_title=Lower('title'))
            if sortkey == 'created':
                sortkey = 'created_on'

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
        'current_sorting': current_sorting,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def post_detail(request, slug):
    ''' A view that renders the post details and shows active comments
    Creates comment object, assigns comment to current post, gets
    username, saves comment to database then clears from and redirects
    the user
    [Code taken from 'https://djangocentral.com/creating-comments-
    system-with-django/']
    '''

    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('post_detail', args=[post.slug]))
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


@login_required
def delete_own_comment(request, comment_id, slug):
    """
    Delete own comment from the blog,
    gets comment by post slug and comment id
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('post_detail', args=[post.slug]))
