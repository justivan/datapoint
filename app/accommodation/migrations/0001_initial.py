# Generated by Django 4.2.7 on 2024-03-12 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("definitions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContractManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "accommodation_contract_manager",
                "ordering": ("user__name",),
            },
        ),
        migrations.CreateModel(
            name="HotelCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
            ],
            options={
                "verbose_name_plural": "hotel categories",
                "db_table": "accommodation_hotel_category",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="HotelChain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
            ],
            options={
                "db_table": "accommodation_hotel_chain",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="HotelStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
            ],
            options={
                "verbose_name_plural": "hotel status",
                "db_table": "accommodation_hotel_status",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="HotelTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("slug", models.SlugField(editable=False, max_length=120)),
            ],
            options={
                "db_table": "accommodation_tag",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="SalesContact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Name of contact",
                    ),
                ),
                (
                    "designation",
                    models.CharField(blank=True, max_length=120, null=True),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "mobile",
                    phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
                ),
            ],
            options={
                "db_table": "accommodation_sales_contact",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=120, unique=True, verbose_name="Hotel Name"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accommodation.hotelcategory",
                    ),
                ),
                (
                    "chain",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accommodation.hotelchain",
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="definitions.area",
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
                ),
                (
                    "longitude",
                    models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
                ),
                ("giata", models.IntegerField(blank=True, default=0)),
                (
                    "contract_manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accommodation.contractmanager",
                    ),
                ),
                (
                    "sales_contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accommodation.salescontact",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accommodation.hotelstatus",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        db_column="updated_by",
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        db_table="accommodation_hotel_tag",
                        to="accommodation.hoteltag",
                    ),
                ),
            ],
            options={
                "ordering": (django.db.models.functions.text.Lower("name"),),
            },
        ),
        migrations.CreateModel(
            name="HotelRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=120, verbose_name="Hotel Room Name"),
                ),
                ("ordinal", models.PositiveIntegerField(default=1)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accommodation.hotel",
                    ),
                ),
            ],
            options={
                "db_table": "accommodation_hotel_room",
                "ordering": ("hotel", "ordinal"),
                "unique_together": {("hotel", "name")},
            },
        ),
        migrations.RunSQL(
            "ALTER SEQUENCE accommodation_hotel_id_seq RESTART WITH 10000001;",
        ),
    ]