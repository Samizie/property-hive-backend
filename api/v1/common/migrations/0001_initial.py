# Generated by Django 5.1.1 on 2024-10-01 20:06

import api.v1.common.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "email",
                    models.EmailField(
                        blank=True, default="", max_length=254, unique=True
                    ),
                ),
                ("fname", models.CharField(blank=True, max_length=255)),
                ("lname", models.CharField(blank=True, max_length=255)),
                (
                    "business_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="user_avatars/"),
                ),
                ("custom_url", models.URLField(blank=True, max_length=500, null=True)),
                ("is_company", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
            managers=[
                ("objects", api.v1.common.models.CustomUserManagement()),
            ],
        ),
        migrations.CreateModel(
            name="KycDocuments",
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
                    "document_type",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
                (
                    "document_file",
                    models.FileField(
                        blank=True, null=True, upload_to="media/kyc_documents/"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kyc_documents",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "company_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_profiles/"
                    ),
                ),
                (
                    "company_banner",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_profiles/"
                    ),
                ),
                (
                    "company_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.TextField(max_length=500)),
                ("instagram", models.CharField(blank=True, max_length=225, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=225, null=True)),
                ("facebook", models.CharField(blank=True, max_length=225, null=True)),
                ("twitter", models.CharField(blank=True, max_length=225, null=True)),
                (
                    "userid",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
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
                ("name", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("squaremeters", models.CharField(max_length=255)),
                ("property_type", models.CharField(max_length=255)),
                ("number_of_bathrooms", models.IntegerField(blank=True, null=True)),
                ("number_of_bedrooms", models.IntegerField(blank=True, null=True)),
                ("installment_duration", models.CharField(max_length=255)),
                ("payment_frequency", models.CharField(max_length=255)),
                ("down_payment", models.TextField()),
                ("installment_payment_price", models.IntegerField()),
                ("duration", models.TextField()),
                ("price", models.IntegerField(blank=True)),
                ("is_sold", models.BooleanField(default=False)),
                ("date_sold", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("keywords", models.TextField(blank=True, null=True)),
                (
                    "sellerid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="properties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyDocuments",
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
                    "document_type",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
                (
                    "img",
                    models.ImageField(blank=True, null=True, upload_to="propery_img/"),
                ),
                (
                    "file_path",
                    models.FileField(
                        blank=True, null=True, upload_to="media/kyc_documents/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "propertyid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_documents",
                        to="common.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyImages",
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
                    "img",
                    models.ImageField(blank=True, null=True, upload_to="propery_img/"),
                ),
                (
                    "propertyid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_images",
                        to="common.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ratings",
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
                ("comment", models.TextField(null=True)),
                (
                    "rate",
                    models.IntegerField(
                        choices=[
                            (1, "1 Star"),
                            (2, "2 Stars"),
                            (3, "3 Stars"),
                            (4, "4 Stars"),
                            (5, "5 Stars"),
                        ],
                        default=1,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "propertyid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="propertyid_rating",
                        to="common.property",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Soldproperties",
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
                ("date_sold", models.DateTimeField(auto_now_add=True)),
                (
                    "buyerid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_soldproperties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "propertyid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_soldproperties",
                        to="common.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transactions",
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
                    "status",
                    models.CharField(
                        choices=[("P", "Pending"), ("A", "Success"), ("F", "Failed")],
                        default="P",
                        max_length=1,
                    ),
                ),
                ("payment_method", models.CharField(max_length=255)),
                ("total_amount", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "propertyid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_transactions",
                        to="common.property",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
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
                ("payment_status", models.CharField(max_length=225)),
                ("payment_method", models.CharField(max_length=225)),
                ("note", models.TextField(blank=True, null=True)),
                ("issue_date", models.DateTimeField(auto_now_add=True)),
                (
                    "transactionid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="common.transactions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Userproperties",
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
                ("date_purchased", models.DateTimeField(auto_now_add=True)),
                (
                    "propertyid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_properties",
                        to="common.property",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_properties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
