from django.db import models
from common.models import CommonModel

# Create your models here.
class ChattingRoom(CommonModel) :
    # chat-room
    users = models.ManyToManyField("users.User",)
    
    def __str__(self) -> str :
        return "Chatting Room"

class Message(CommonModel) :
    
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="directMessages",
    )
    
    room = models.ForeignKey(
        "direct_messages.ChattingRoom", 
        on_delete=models.CASCADE,
        related_name="directMessages",
    )
    
    def __str__(self) -> str :
        return f"{self.user} : {self.text}"