from django.shortcuts import get_object_or_404, render, redirect
from .models import Notice, Board, Comment, Account
from .forms import BoardForm, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required
# from myapp.forms import CustomAccountForm
# from django_registration.backends.activation.views import RegistrationView as BaseRegistrationView

# Create your views here.
# 홈 화면 보여주는 함수
def home(request):
    return render(request, 'home.html')

# about 페이지 보여주는 함수
def about(request):
    return render(request, 'about.html')

# 게시판 글들 보여주는 함수
def board(request):
    boards = Board.objects
    board_list = Board.objects.all()
    paginator = Paginator(board_list, 10)
    page = request.GET.get('page','1')
    if page == '':
        page = '1'
    page = int(page)
    posts = paginator.get_page(page)
    return render(request, 'board.html', {'boards' : boards, 'posts' : posts})

# 게시판 구체적 내용 보여주는 함수
def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    # 댓글 form
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
            return redirect('board_detail', board.id)
    else:
        form = CommentForm()
    return render(request, 'board_detail.html', {'board' : board, 'form' : form})

def comment_delete(request, board_id, comment_id):
    board = get_object_or_404(Board, pk=board_id)
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('board_detail', board.id)

def board_create(request):
    # 게시판 글쓰기에서 입력받은 내용을 데이터베이스에 추가
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('board_detail', board.id)
    else:
        form = BoardForm()
    # 게시판 글쓰기 화면 띄워주는 함수
    return render(request, 'board_create.html', {'form': form})

# 게시글 삭제
def board_delete(request,board_id):
    board = Board.objects.get(pk=board_id)
    board.delete()
    return redirect('board')

def board_update(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    # 게시판 수정된 내용을 데이터베이스에 추가
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('board_detail', board.id)
    else:
        form = BoardForm(instance=board)
    # 게시글 수정화면 띄워주는 함수
    return render(request, 'board_update.html', {'board' : board, 'form': form})
    

# 공지 글들 보여주는 함수
def notice(request):
    notices = Notice.objects
    notice_list = Notice.objects.all()
    paginator = Paginator(notice_list, 5)
    page = request.GET.get('page','1')
    if page == '':
        page = '1'
    page = int(page)
    posts = paginator.get_page(page)
    return render(request, 'notice.html', {'notices': notices, 'posts' : posts})


# 공지 구체적 내용 띄워주는 함수
def notice_detail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice_detail.html', {'notice': notice_detail})

# registration
# class RegistrationView(BaseRegistrationView):
#     form_class = CustomAccountForm

#     def register(self, form):
#         new_user = BaseRegistrationView.register(self, form)
#         acc = Account()
#         acc.username = form.cleaned_data['username']
#         acc.user = new_user
#         # acc.status = 'created'
#         acc.save()
        
