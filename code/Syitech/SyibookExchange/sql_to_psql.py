from django.contrib.contenttypes.models import ContentType

def run():
    ContentType.objects.all().delete()