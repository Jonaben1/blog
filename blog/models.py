from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from gtts import gTTS
import tempfile


# Create your models here.


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    author = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    title = models.CharField(
        max_length=255,
        unique=True
    )
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    body = RichTextUploadingField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
    categories = models.ManyToManyField(
        'Category', related_name='post'
    )
    status = models.IntegerField(
        choices=STATUS, default=0
    )

    audio = models.FileField(upload_to='audio/', blank=True)

    class Meta:
        ordering = ['-created_on']

    def read_time(self):
        return round(len(self.body.split(' ')) / 200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail.html', kwargs=({'slug': self.slug}))

    def save(self, *args, **kwargs):
        # generate and cache the audio content using gTTS
        audio = gTTS(text=self.body, lang='en', slow=False)
        with tempfile.TemporaryFile(mode='w') as f:
            audio.write_to_fp(f)
            self.audio.save(f'{self.title}.mp3', f)
        super().save(*args, **kwargs)



class Comment(models.Model):
    name = models.CharField(max_length=80)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body  = models.TextField()
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.content} by {self.name}'




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
