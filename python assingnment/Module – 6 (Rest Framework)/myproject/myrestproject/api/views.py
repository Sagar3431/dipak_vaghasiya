from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import BokkSerializers

# Create your views here.
@api_view(["Post"])
def bookadd(request):
    if isinstance(request.data, list):
        Serializers = BokkSerializers(data=request.data,many=True)
    else:
        Serializers = BokkSerializers(data=request.data)
    if Serializers.is_valid():
        Serializers.save()
        return Response(Serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(Serializers.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def BookList(request):
    if request.method=="GET":
        students=Book.objects.all()
        Serializer=BokkSerializers(students,many=True)
        return Response(Serializer.data)
    
@api_view(["GET"])
def bookSpecific(request,pk):
    if request.method=="GET":
        book=Book.objects.get(id=pk)
        Serializer=BokkSerializers(book)
        return Response(Serializer.data)
    
@api_view(["DELETE"])
def bookDelete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def deleteAllBook(request):
    book = Book.objects.all()
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    book=Book.objects.all()
    context={
        "book":book
    }
    return render(request,"api/home.html",context)

def delete(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return redirect("home")

def addbook(request):
    if request.method=="POST":
        Title=request.POST["Title"]
        Author=request.POST["Author"]
        Isbn=request.POST["Isbn"]
        Publisher=request.POST["Publisher"]
        if Title and Author and Isbn and Publisher:
            Book.objects.create(Title=Title, Author=Author, Isbn=Isbn, Publisher=Publisher)
    return render(request,"api/addbook.html")

def edite(request,pk):
    book=Book.objects.get(id=pk)
    if request.method == "POST":
        # Safely access POST data using .get(), which avoids MultiValueDictKeyError
        book.Title = request.POST.get("Title", book.Title)
        book.Author = request.POST.get("Author", book.Author)
        book.Isbn = request.POST.get("Isbn", book.Isbn)
        book.Publisher = request.POST.get("Publisher", book.Publisher)
        book.save()
        
    contex={
            "book":book
         }
    return render(request,"api/edite.html",contex)


def view(request,pk):
    book=Book.objects.get(id=pk)
    contex={
        "book":book
    }
    return render(request,"api/view.html",contex)