from django.core.management.base import BaseCommand
from django.core.management import call_command
from blogging.models import Article

class Command(BaseCommand):
    help = "Очищение данных из таблиц баз данных и загрузка тестовых данных из фикстур."

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Successfully deleted data from database"))
        call_command("loaddata", "article_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
