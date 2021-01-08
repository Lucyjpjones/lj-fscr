from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, ThreadForm
from django.db.models.functions import Lower
from .models import Thread, Comment


@login_required
def all_threads(request):
    threads = Thread.objects.filter(status=1).order_by('-created_on')
    comments = Comment.objects.all
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'topic':
                sortkey = 'lower_topic'
                threads = threads.annotate(lower_topic=Lower('topic'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            threads = threads.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'threads': threads,
        'current_sorting': current_sorting,
        'comments': comments
    }

    return render(request, 'forum/forum.html', context)


@login_required
def thread_detail(request, slug):
    template_name = 'forum/thread_detail.html'
    thread = get_object_or_404(Thread, slug=slug)
    comments = thread.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.thread = thread
            # Get username
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
            # Clear comment field after save
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'thread': thread,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


@login_required
def add_thread(request):
    """ Add a post to the forum """

    form = ThreadForm()

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save()
            messages.success(request, 'Successfully added thread!')
            return redirect('forum')
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    template = 'forum/add_thread.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
