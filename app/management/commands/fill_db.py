from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Tag, Question, Answer
from random import choice, sample
from faker import Faker

fake = Faker()


def fill_tags(count):
    for i in range(count):
        Tag.objects.create(
            name=f'{fake.word()}',
            usage_num=fake.random_int(min=0, max=1000)
        )


def fill_profiles(count):
    for i in range(count):
        user = User.objects.create_user(f'{fake.name()}{fake.random_int(min=0, max=10)}', fake.email(), fake.password())
        user.save()

        Profile.objects.create(
            rating=fake.random_int(min=0, max=100),
            user=user
        )


def fill_questions(count):
    profiles_id = list(Profile.objects.values_list('id', flat=True))
    tags_id = list(Tag.objects.values_list('id', flat=True))

    for i in range(count):
        q = Question.objects.create(
            title=' '.join(fake.sentences(fake.random_int(min=3, max=4))),
            text=' '.join(fake.sentences(fake.random_int(min=20, max=25))),
            author=Profile.objects.get(pk=choice(profiles_id)),
            rating=fake.random_int(min=-100, max=100),
            answers_number=0,
        )
        q.save()

        cur_tags_id = sample(tags_id, fake.random_int(min=1, max=4))
        for tag_id in cur_tags_id:
            q.tags.add(Tag.objects.get(pk=tag_id))


def fill_answers(count):
    profiles_id = list(Profile.objects.values_list('id', flat=True))
    questions_id = list(Question.objects.values_list('id', flat=True))

    for i in range(count):
        q = Question.objects.get(pk=choice(questions_id))
        q.answers_number += 1
        q.save()

        a = Answer.objects.create(
            text=' '.join(fake.sentences(fake.random_int(min=30, max=40))),
            author=Profile.objects.get(pk=choice(profiles_id)),
            correct=choice([True, False]),
            rating=fake.random_int(min=0, max=len(profiles_id) - 1),
            question=q,
        )
        a.save()


class Command(BaseCommand):

    help = 'Fill db with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--profile', '-p', type=int)
        parser.add_argument('--tag', '-t', type=int)
        parser.add_argument('--question', '-q', type=int)
        parser.add_argument('--answer', '-a', type=int)
        parser.add_argument('--ratio', '-r', type=int)

    def handle(self, *args, **options):
        if options['profile']:
            fill_profiles(options.get('profile', 0))
        if options['tag']:
            fill_tags(options.get('tag', 0))
        if options['question']:
            fill_questions(options.get('question', 0))
        if options['answer']:
            fill_answers(options.get('answer', 0))
        if options['ratio']:
            ratio = options.get('ratio', 0)
            fill_profiles(ratio)
            fill_tags(ratio)
            fill_questions(ratio * 10)
            fill_answers(ratio * 100)
