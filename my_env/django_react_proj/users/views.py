from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, Events
from .serializers import *
import mysql.connector as sql

# database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "event_database",
}


# login api
@api_view(["POST"])
def login(request):
    if request.method == "POST":
        m = sql.connect(
            host="localhost", user="root", password="1234", database="event_database"
        )
        cursor = m.cursor()
        email = request.POST.get("email", "")
        pwd = request.POST.get("password", "")
        query = "select * from users_user where email='{}' and password='{}'".format(
            email, pwd
        )
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            user_data = {
                "id": user[0],
                "name": user[1],
                "email": user[2],
            }
            return Response(user_data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data="User doesn't exist")


# register api
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET api for fetching all the events
@api_view(["GET"])
def getEvents(request):
    if request.method == "GET":
        data = Events.objects.all()

        serializer = EventsSerializer(data, context={"request": request}, many=True)

        return Response(serializer.data)


# POST api for adding an event
@api_view(["POST"])
def addEvent(request):
    if request.method == "POST":
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# put api to update is_liked state of an event
@api_view(["PUT"])
def updateEvent(request, pk):
    try:
        event = Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = EventsSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
