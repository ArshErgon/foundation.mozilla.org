# Generated by Kevin on 2022-06-17 09:55

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models
from networkapi.wagtailpages.models import Profile


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0029_adds_slug_field'),
    ]

    def populate_profile_slugs(apps, schema_editor):
        """Call save on the Profile snippets to populate
        slug values"""
        for profile in Profile.objects.all():
            profile.save()

    operations = [
        migrations.RunPython(populate_profile_slugs),
    ]