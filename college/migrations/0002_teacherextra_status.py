

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherextra',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]