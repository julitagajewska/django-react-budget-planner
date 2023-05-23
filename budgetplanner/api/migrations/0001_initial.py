# Generated by Django 4.1.5 on 2023-05-22 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('incoming', 'Incoming'), ('outgoing', 'Outgoing'), ('Wallet', 'Wallet')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('incoming', 'Incoming'), ('outgoing', 'Outgoing')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('categories', models.ManyToManyField(blank=True, to='api.category')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.CharField(max_length=250)),
                ('recipient', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.transactiontype')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallets', models.ManyToManyField(to='api.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorytype'),
        ),
        migrations.AddField(
            model_name='category',
            name='wallets',
            field=models.ManyToManyField(blank=True, to='api.wallet'),
        ),
    ]
