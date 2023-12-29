

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_notice_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='by',
            field=models.CharField(default='college', max_length=20, null=True),
        ),
    ]
