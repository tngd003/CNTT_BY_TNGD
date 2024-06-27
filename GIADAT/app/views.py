from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
import requests

def dangky(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dangnhap')
    context = {'form': form}
    return render(request, 'app/dangky.html', context)

def dangnhap(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu không đúng!')
    
    context = {}
    return render(request, 'app/dangnhap.html', context)

def dangxuat(request):
    logout(request)
    return redirect('dangnhap')





def index(request):
    danh_muc = TheLoai.objects.filter(is_sub = False)
   
    active_danhmuc = request.GET.get('danhmuc','')
    books = Sach.objects.all()
    context={'danh_muc' :danh_muc,'books':books} 
    return render(request, 'app/index.html',context)




def copyright_info_view(request):
    context = {}
    return render(request, 'app/copyright.html', context)


def read_book(request):
        chaps = ChapBook.objects.all()
        context ={'chaps': chaps}
        return render(request,'app/read.html',context)


def best_sellers_view(request):
    api_key = 'lIWe0vwxbnzjFWGMIQJpTNCSOsXwUvor'  # Thay thế bằng API Key của bạn từ New York Times
    
    # Endpoint API để lấy danh sách sách bán chạy nhất hiện tại (current best sellers list)
    endpoint = 'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json'
    
    # Thêm API Key vào các tham số của yêu cầu GET
    params = {'api-key': api_key}
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Nếu có lỗi trong yêu cầu, raise HTTPError
        
        data = response.json()  # Chuyển đổi dữ liệu nhận được thành JSON
        
        # Xử lý dữ liệu và trả về template
        books = data['results']['books']  # Lấy danh sách các cuốn sách từ dữ liệu nhận được
        
        return render(request, 'books/best_sellers.html', {'books': books})
    
    except requests.exceptions.RequestException as e:
        # Xử lý lỗi khi gửi yêu cầu API
        return render(request, 'books/error.html', {'error': str(e)})
