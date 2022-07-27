# Generated by Django 4.0.2 on 2022-07-15 23:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import miq.core.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('store', '0004_product_is_oos'),
        ('core', '0003_sitesetting_whatsapp_number'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update date and time')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2, message='Enter your first name.')], verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2, message='Enter your last name.')], verbose_name='Last name')),
                ('phone', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(4, message='Veuillez entrer votre numéro de téléphone.')], verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_customers', to='staff.user')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update date and time')),
                ('notes', models.TextField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('dt_delivery', models.DateTimeField(blank=True, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('dt_delivered', models.DateTimeField(blank=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_orders', to='staff.user')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='sales.customer')),
            ],
            options={
                'verbose_name': 'Orders settings',
                'verbose_name_plural': 'Orders settings',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.user',),
            managers=[
                ('objects', miq.core.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='OrdersSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update date and time')),
                ('checkout_method', models.CharField(choices=[('PAY', 'Use payment platforms'), ('MSG', 'Use messaging platforms')], default='MSG', max_length=50, verbose_name='Checkout method')),
                ('site', models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='sites.site', verbose_name='Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update date and time')),
                ('name', models.CharField(max_length=99, verbose_name='Name')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Current price')),
                ('was_sale', models.BooleanField(default=False, verbose_name='Is on sale')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('img', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.productimage', verbose_name='Image')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='sales.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='store.product', verbose_name='Product')),
                ('size', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='store.productsize', verbose_name='Size')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, through='sales.OrderItem', to='store.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer', to='sales.customeruser'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sales.order',),
        ),
    ]