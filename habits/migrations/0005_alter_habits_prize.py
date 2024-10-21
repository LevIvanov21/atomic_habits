from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_alter_habits_prize"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habits",
            name="prize",
            field=models.CharField(max_length=100, verbose_name="Вознаграждение"),
        ),
    ]
