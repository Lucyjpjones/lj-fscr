from django.shortcuts import render, get_object_or_404
from .models import Post
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

    return render (request, 'blog/blog.html', context)


def post_detail(request, slug):
    """ A view to show individual post details """

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)
