from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import NoticeForm

# Create your views here.
@require_safe
def index(request):
    notices = Notice.objects.order_by('-pk')
    context = {
        'notices': notices,
    }
    return render(request, 'notice_board/index.html', context)

@login_required
@require_http_methods(['GET', 'POSTS'])
def create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save()
            return redirect('notice:detail', notice.pk)
    else:
        form = NoticeForm()
    context = {
        'form': form,
    }
    return render(request, 'notice_board/create.html', context)

@require_safe
def detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice': notice,
    }
    return render(request, 'notice_board/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        notice = get_object_or_404(Notice, pk=pk)
        notice.delete()
    return redirect('notice:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(reuqest.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice:detail', notice.pk)
    else:
        form = NoticeForm(instance=notice)
    context = {
        'form': form,
        'notice': notice,
    }
    return render(request, 'notice_board/update.html', context)