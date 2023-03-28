from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
# def student_api(request):
#     return Response({"msg":"hello student"})

@api_view(['GET','POST'])
def student_api(request):
    if request.method == "GET":
        return Response({"msg":"this is get requests"})
    if request.method == "POST":
        print(request.data)
        return Response({"msg":"this is post request"})


