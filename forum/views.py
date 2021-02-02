from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, ThreadForm
from .models import Thread, Reply
from blog.decorators import login_required_message


@login_required_message(message="Sorry you need to be a registered \
                        user to access our forum")
@login_required
def all_threads(request):
    """
    A view to show all thread posts, filtered by active and
    ordered by date posted, user login required to access
    """
    threads = Thread.objects.filter(status=1).order_by('-created_on')
    replies = Reply.objects.all

    context = {
        'threads': threads,
        'replies': replies
    }

    return render(request, 'forum/forum.html', context)


@login_required
def thread_detail(request, slug):
    """
    A view that renders the thread details and shows active replies
    Creates reply object, assigns reply to current thread, gets
    username, saves reply to database then clears from and redirects
    the user
    [Code taken from 'https://djangocentral.com/creating-comments-
    system-with-django/']
    """
    template_name = 'forum/thread_detail.html'
    thread = get_object_or_404(Thread, slug=slug)
    replies = thread.replies.filter(active=True)
    new_reply = None

    if request.method == 'POST':
        reply_form = CommentForm(data=request.POST)
        if reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            new_reply.thread = thread
            new_reply.user = request.user
            new_reply.save()
            reply_form = CommentForm()
            messages.success(request, 'Successfully added response!')
            return redirect(reverse('thread_detail', args=[thread.slug]))
    else:
        reply_form = CommentForm()

    return render(request, template_name, {'thread': thread,
                                           'replies': replies,
                                           'new_reply': new_reply,
                                           'reply_form': reply_form})


@login_required
def add_thread(request):
    """
    If logged in can add a new thread to the forum
    Gets thread form, if user input is valid, saves thread and redirects
    user to the thread detail page
    """
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            thread.save()
            messages.success(request, 'Successfully added thread!')
            return redirect(reverse('thread_detail', args=[thread.slug]))
        else:
            messages.error(request, 'Failed to add thread. Please ensure the \
                form is valid.')

    form = ThreadForm()
    thread = None
    template = 'forum/add_thread.html'

    context = {
        'form': form,
        'thread': thread
    }

    return render(request, template, context)


@login_required
def edit_thread(request, slug):
    """
    If logged in can edit own thread in the forum
    Gets thread form by thread slug, if user input is valid, updates
    thread form and redirects user to the thread detail page
    """
    thread = get_object_or_404(Thread, slug=slug)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated thread!')
            return redirect(reverse('thread_detail', args=[thread.slug]))
        else:
            messages.error(request, 'Failed to update thread. Please ensure \
                the form is valid.')
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
def delete_own_reply(request, reply_id, slug):
    """
    Delete own reply from the thread,
    gets reply by thread slug and comment id
    """
    thread = get_object_or_404(Thread, slug=slug)
    reply = get_object_or_404(Reply, pk=reply_id)
    reply.delete()
    messages.success(request, 'Response deleted!')
    return redirect(reverse('thread_detail', args=[thread.slug]))
