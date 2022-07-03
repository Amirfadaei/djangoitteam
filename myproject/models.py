import uuid

from django.db import models

class Projects(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=50, null=True, blank=True)
    source_link = models.CharField(max_length=50, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4(), unique=True,primary_key=True, editable=False)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)



    def __str__(self):
        return self.title
