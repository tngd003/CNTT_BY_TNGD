from django.db import models
from django.contrib.auth.forms import User
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
#
class TheLoai(models.Model):
    danhmuc_con = models.ForeignKey('self', on_delete=models.CASCADE, related_name='danhmuc_conn', null=True, blank=True)  
    is_sub = models.BooleanField(default=False)
    ten_the_loai = models.CharField(max_length=200, null=True)
  

    def __str__(self):
        return self.ten_the_loai

class Sach(models.Model):
    tensach = models.CharField(max_length=200, null=True)
    danhmuc = models.ManyToManyField(TheLoai, related_name='danhmucs')
    sochuong = models.FloatField()
    ngaythem = models.DateTimeField(auto_now_add=True)
    tacgia = models.CharField(max_length=200, null=True)
    gioithieu = models.CharField(max_length=200, null=True)
    trangthai = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.tensach

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ThichSach(models.Model):
    sach = models.ForeignKey(Sach, on_delete=models.SET_NULL, blank=True, null=True)
    ngay = models.DateTimeField(auto_now_add=True)
    sachdathich = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.sachdathich

class ItemSach(models.Model):
    spsach = models.ForeignKey(Sach, on_delete=models.SET_NULL, blank=True, null=True)
    thich = models.ForeignKey(ThichSach, on_delete=models.SET_NULL, blank=True, null=True)
    ngaythich = models.DateTimeField(auto_now_add=True)

class ThongTin(models.Model):
    sach = models.ForeignKey(Sach, on_delete=models.SET_NULL, blank=True, null=True)
    thich = models.ForeignKey(ThichSach, on_delete=models.SET_NULL, blank=True, null=True)
    ten = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.ten
    
class ChapBook(models.Model):
    tensach = models.ForeignKey(Sach,on_delete=models.SET_NULL,blank=True,null=True)
    idchuong = models.FloatField()
    ngaythem = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return f"{self.tensach} - {self.idchuong}"
    @property
    def IMAGEURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url    
    

#doiformdangky
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']