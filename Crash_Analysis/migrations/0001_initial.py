from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        CreateExtension("postgis"),
        # Add other operations if needed
    ]
