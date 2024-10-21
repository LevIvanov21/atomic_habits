from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_habits_created_at_habits_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habits",
            name="prize",
            field=models.CharField(
                default=None, max_length=100, verbose_name="Вознаграждение"
            ),
        ),
    ]
