from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_tg_chat_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                help_text="Укажите телеграм chat-id",
                max_length=50,
                verbose_name="Телеграм chat-id",
            ),
        ),
    ]
