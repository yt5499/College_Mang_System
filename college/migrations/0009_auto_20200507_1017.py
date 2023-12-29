

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_studentextra_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='teacherextra',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]
