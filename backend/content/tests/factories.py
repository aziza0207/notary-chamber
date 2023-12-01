import factory

from ..models import News


class NewsFactory(factory.django.DjangoModelFactory):
    main_image = factory.Faker('image_url')
    title = factory.Faker('catch_phrase')
    slug = factory.Faker('slug')
    description = factory.Faker('text')
    video = factory.Faker('image_url')
    date = factory.Faker('date_this_year')
    is_pinned = factory.Faker('boolean')

    class Meta:
        model = News
