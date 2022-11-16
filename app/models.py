from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# QUESTIONS = [
#     {
#         'id': question_id,
#         'title': f'Question #{question_id}',
#         'text': f'Text of question #{question_id}',
#         'answers_number': question_id * question_id,
#         'tags': ['tag' for i in range(4)],
#     } for question_id in range(100)
# ]
#
# HOT_QUESTIONS = [
#     {
#         'id': question_id,
#         'title': f'Hot Question #{question_id}',
#         'text': f'Hot Text of question #{question_id}',
#         'answers_number': question_id * question_id,
#         'tags': ['Hot tag' for i in range(5)],
#     } for question_id in range(100)
# ]


class TagManager(models.Manager):
    def popular(self):
        return self.order_by('-usage_num')[:10]


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=False)
    usage_num = models.PositiveIntegerField(default=0)

    objects = TagManager()

    def __str__(self):
        return f'{self.name}'


class ProfileManager(models.Manager):
    def best(self):
        return self.order_by('-rating')[:5]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    objects = ProfileManager()

    def __str__(self):
        return f'Имя: {self.user.username}'


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by("-createdAt")

    def hot(self):
        return self.order_by("-rating")

    def get_by_tag(self, tag_name):
        return self.filter(tags__name=tag_name)


class Question(models.Model):
    title = models.CharField(max_length=100, unique=False)
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.IntegerField(default=0)
    answers_number = models.IntegerField(default=0)
    createdAt = models.DateField(auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return f'Вопрос: {self.title} | Ответов: {self.rating}'


class AnswerManager(models.Manager):
    def new(self, id):
        q = Question.objects.get(pk=id)
        return self.filter(question=q).order_by("-createdAt")

    def hot(self, id):
        q = Question.objects.get(pk=id)
        return self.filter(question=q).order_by("-rating")


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null=True)
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    question = models.ForeignKey(Question, models.CASCADE)
    createdAt = models.DateField(auto_now_add=True)

    objects = AnswerManager()

    def __str__(self):
        return f'Вопрос: {self.question.title} | Ответ: {self.text} | Рейтинг: {self.rating}'


