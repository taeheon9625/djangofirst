from rest_framework.response import Response
from rest_framework.decorators import api_view

#python에서 @으로 시작하는 단어는 decorator라고 하는데 실제 함수를 호출하면
#특정 내용을 삽입해서 함수를 실행합니다.
#반복적으로 사용하는 내용이나 직접 작성하기 번거로운 내용을 decorator로 만듭니다.
#GET 요청이 오면 함수를 호출
@api_view(['GET'])
def hello(request):
    return Response("Hello REST API")


from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializer

#get과 post모두 처리
@api_view(['GET', 'POST'])
def booksAPI(request):
    #get방식의 처리 - 조회를 요청하는 경우
    if request.method == 'GET':
        books = Book.objects.all()
        #테이블 데이터 전부 가져오기
        serializer = BookSerializer(books, many = True)
        #출력하기 위해서 브라우저의 형식으로 데이터 변환
        return Response(serializer.data)
        #출력
   
    #post방식의 처리 - 삽입하는 경우
    elif request.method == 'POST':
        #클라이언트에서 전송된데이터를 가지고 Model1 인스턴스 생성
        serializer = BookSerializer( data = request.data)
        #유효성 검사를 수행해서 통과하면 삽입하고 실패하면 이유 출력
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET'])
def oneBookAPI(request, bid):
    #Book 테이블에서 bid 컬럼의 값이 bid인 값을 찾아옵니다.
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data)