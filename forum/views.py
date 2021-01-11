from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, ThreadForm
from django.db.models.functions import Lower
from .models import Thread, Reply


@login_required
def all_threads(request):
    threads = Thread.objects.filter(status=1).order_by('-created_on')
    replies = Reply.objects.all
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
        'replies': replies
    }

    return render(request, 'forum/forum.html', context)


@login_required
def thread_detail(request, slug):
    template_name = 'forum/thread_detail.html'
    thread = get_object_or_404(Thread, slug=slug)
    replies = thread.replies.filter(active=True)
    new_reply = None

    # Comment posted
    if request.method == 'POST':
        reply_form = CommentForm(data=request.POST)
        if reply_form.is_valid():
            # Create Comment object but don't save to database yet
            new_reply = reply_form.save(commit=False)
            # Assign the current post to the comment
            new_reply.thread = thread
            # Get username
            new_reply.user = request.user
            # Save the comment to the database
            new_reply.save()
            # Clear comment field after save
            reply_form = CommentForm()
    else:
        reply_form = CommentForm()

    return render(request, template_name, {'thread': thread,
                                           'replies': replies,
                                           'new_reply': new_reply,
                                           'reply_form': reply_form})


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
            messages.error(request, 'Failed to add thread. Please ensure the form is valid.')

    template = 'forum/add_thread.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_thread(request, thread_id):
    """ Edit a thread in the forum """

    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated thread!')
            return redirect(reverse('forum'))
        else:
            messages.error(request, 'Failed to update thread. Please ensure the form is valid.')
    else:
        form = ThreadForm(instance=thread)
        messages.info(request, f'You are editing {thread.topic}')

    template = 'forum/edit_thread.html'
    context = {
        'form': form,
        'thread': thread,
    }

    return render(request, template, context)


@login_required
def delete_own_reply(request, reply_id):
    """ Delete own comment from the blog """
    reply = get_object_or_404(Reply, pk=reply_id)
    reply.delete()
    messages.success(request, 'Reply deleted!')
    return redirect('forum')
