from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.db.models.functions import Lower


def all_posts(request):
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

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'current_sorting': current_sorting,
    }

    return render (request, 'forum/forum.html', context)


def post_detail(request, slug):
    template_name = 'forum/post_detail.html'
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
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def add_post(request):
    """ Add a post to the forum """

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    template = 'forum/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
