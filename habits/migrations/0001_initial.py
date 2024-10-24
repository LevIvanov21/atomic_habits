from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=140, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время, когда надо выполнить привычку')),
                ('action', models.CharField(max_length=140, verbose_name='Действие, которое надо сделать')),
                ('is_good', models.BooleanField(choices=[(True, 'Приятная'), (False, 'Нет')], default=True, verbose_name='Приятная')),
                ('periodicity', models.SmallIntegerField(default=1, verbose_name='Периодичность (в днях) - от 1 до 7')),
                ('prize', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('duration', models.SmallIntegerField(verbose_name='Время на выполнение (в минутах)')),
                ('is_public', models.BooleanField(choices=[(True, 'Публичная'), (False, 'Нет')], default=True, verbose_name='Публичная')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ['-id'],
            },
        ),
    ]
