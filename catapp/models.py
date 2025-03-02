from django.db import models


class PredictionTag(models.TextChoices):
    PHILOSOPHICAL = "philosophical", "Философское"
    FUNNY = "funny", "Смешное"
    INSPIRATIONAL = "inspirational", "Жизнеутверждающее"


class Prediction(models.Model):
    text = models.TextField(null=True, blank=True, max_length=500)
    image = models.ImageField(upload_to="predictions/", null=True, blank=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(
        max_length=20,
        choices=PredictionTag.choices,
        default=PredictionTag.PHILOSOPHICAL,
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return self.text[:50] if self.text else f"Image Prediction {self.id}"


class Comment(models.Model):
    prediction = models.ForeignKey(
        Prediction, related_name="comments", on_delete=models.CASCADE
    )
    username = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.username}"


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"
