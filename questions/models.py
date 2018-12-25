from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum

# Напоминалка: ForeignKey в связи один ко многим указываем на связь "один"

class ModelManagerQuestion(models.Manager):
    def top(self):
        return self.annotate(answer_count=Count('answers')).order_by('-answer_count')
    
    def get_tag(self, tag_name):
        tags = get_object_or_404(Tag, name=tag_name)
        return self.annotate(answer_count=Count('answers')).order_by().filter(tags__id = tags.id)[::-1]

    def get_list(self):
        return self.annotate(answer_count=Count('answers')).order_by()[::-1]

    def get_question(self, question_id):
        return self.annotate(answer_count=Count('answers')).get(id=question_id)


class ModelManagerAnswer(models.Manager):
    def answer(self, question_id):
        question = get_object_or_404(Question, pk=int(question_id))
        return self.filter(question__id = question.id)



class LikeDislikeManager(models.Manager):
    use_for_related_fields = True
 
    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


class Profile(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    avatar_path = models.FileField(upload_to="uploads/%Y/%m/%d/")


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
 
    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )
 
    vote = models.SmallIntegerField(verbose_name=u"Vote", choices=VOTES)
    user = models.ForeignKey(to="Profile", verbose_name=u"Profile", on_delete=models.SET_NULL, null=True)
 
    content_type = models.ForeignKey(to="contenttypes.ContentType", on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 
    objects = LikeDislikeManager()


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Question(models.Model):

    objects = ModelManagerQuestion()
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=600)
    author = models.ForeignKey(to="Profile", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    votes = GenericRelation(to="LikeDislike", related_query_name='questions')


class Answer(models.Model):

    objects = ModelManagerAnswer()
    description = models.TextField(max_length=200)
    question = models.ForeignKey(to="Question", on_delete=models.SET_NULL, null=True, related_name='answers')
    author = models.ForeignKey(to="Profile", on_delete=models.SET_NULL, null=True, related_name='answers')
    votes = GenericRelation(to="LikeDislike", related_query_name='answers')


