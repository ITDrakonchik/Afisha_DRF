from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def filter_reviews(self):
        return self.reviews.filter(stars__in=[4, 5])

    @property
    def rating(self):
        reviews = self.filter_reviews
        count = reviews.count()
        sum_ = 0
        for item in reviews:
            sum_ += item.stars
        try:
            return sum_ / count
        except ZeroDivisionError:
            return 0


STARS = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)


class Review(models.Model):
    text = models.CharField(max_length=100)
    stars = models.IntegerField(default=5, choices=STARS)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,  related_name='reviews')

    def __str__(self):
        return self.text

    def stars_str(self):
        return self.stars * '* '
