from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True) #unique=重複禁止
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):

    ROOM_TYPES = [
       #(databaseに保存される値, 管理画面に表示される値)
        ("standard", "Standard"),
        ("double", "Double"),
        ("deluxe", "Deluxe"),
        
    ]

    hotel = models.ForeignKey(
        #どのホテルの部屋か
        Hotel,
        on_delete=models.CASCADE #親が消えたら消す
    )

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES
    )

    def __str__(self):
        return f"{self.hotel.name} - {self.room_type}"


class Reservation(models.Model):

    user = models.ForeignKey(
        #誰が予約したか
        User,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        #どの部屋を予約したか
        Room,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"