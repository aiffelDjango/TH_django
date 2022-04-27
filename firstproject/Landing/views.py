from django.shortcuts import render
from django.core.files.storage import default_storage
# httpResponse를 위해 임포트
from django.http import HttpResponse
# 인공지능을 관리하는 코드 임포트
from stickerUtils.sticker import stickerGen


# Create your views here.
#views.py
def index(req):
    return render(req,'Landing/index.html')

def study(req):
    return render(req,'Landing/study.html')


def sticker(req):
    return render(req,'Landing/sticker.html')

def stickerResult(request):
    if request.method == 'POST': # 통신이 post일때
        try:
            imgMemory= request.FILES["image"] # 통신에서 iamge를 inmemory에 저장되어 있는 값으로 읽어 드리도록 한다.
            imgByte = imgMemory.read() # 통신에서 iamge를 Byte로 읽어 드리도록 한다.
            convertImg = "data:image/jpg;base64, "+str(stickerGen(imgByte)) # Html img 태그에서 출력할수 있도록 base64 타입으로 변환
            return render(request, 'Landing/stickerResult.html', {'image':convertImg}) # stickerResult.html을 보여줄때 가공한 image파일도 같이 넘긴다
        except:
            return   HttpResponse("보여줄 이미지가 없습니다!") # image 파일이 없으면 처리
    else:
        return   HttpResponse("보여줄 이미지가 없습니다!") # post 통신이 아니면 자료를 보낼수 없어서 예외 처리