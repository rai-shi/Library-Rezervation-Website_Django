# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Kutuphane(models.Model):
    konumid = models.AutoField(db_column='konumID', primary_key=True)  # Field name made lowercase.
    odano = models.IntegerField(db_column='odaNo')  # Field name made lowercase.
    masano = models.CharField(db_column='MasaNo', max_length=1)  # Field name made lowercase.
    sandalyeno = models.CharField(db_column='sandalyeNo', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kutuphane'


class Misafiruye(models.Model):
    uyeid = models.AutoField(db_column='UyeID', primary_key=True)  # Field name made lowercase.
    ad = models.CharField(db_column='Ad', max_length=45)  # Field name made lowercase.
    soyad = models.CharField(db_column='Soyad', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=45)  # Field name made lowercase.
    sifre = models.CharField(db_column='Sifre', max_length=8)  # Field name made lowercase.
    meslek = models.CharField(db_column='Meslek', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telno = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'misafiruye'


class Ogrenciuye(models.Model):
    uyeid = models.AutoField(db_column='uyeID', primary_key=True)  # Field name made lowercase.
    ad = models.CharField(db_column='Ad', max_length=40)  # Field name made lowercase.
    soyad = models.CharField(db_column='Soyad', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=45)  # Field name made lowercase.
    sifre = models.CharField(db_column='Sifre', max_length=8)  # Field name made lowercase.
    telno = models.CharField(db_column='Telno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    puan = models.IntegerField(db_column='Puan', blank=True, null=True)  # Field name made lowercase.
    ogrno = models.IntegerField(db_column='OgrNo', unique=True)  # Field name made lowercase.
    fakulte = models.CharField(db_column='Fakulte', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bolum = models.CharField(db_column='Bolum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mezuntarihi = models.DateField(db_column='MezunTarihi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ogrenciuye'


class Oneri(models.Model):
    oneriid = models.AutoField(db_column='oneriID', primary_key=True)  # Field name made lowercase.
    oneri = models.TextField(blank=True, null=True)
    uyeid = models.ForeignKey(Ogrenciuye, models.DO_NOTHING, db_column='UyeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oneri'


class Rezervasyon(models.Model):
    rezervasyonid = models.AutoField(db_column='rezervasyonID', primary_key=True)  # Field name made lowercase.
    uyeid = models.ForeignKey(Ogrenciuye, models.DO_NOTHING, db_column='uyeID')  # Field name made lowercase.
    tarih = models.DateField()
    saatbaslangic = models.TimeField(db_column='saatBaslangic')  # Field name made lowercase.
    saatbitis = models.TimeField(db_column='saatBitis')  # Field name made lowercase.
    molahakki = models.TimeField(blank=True, null=True)
    konumid = models.ForeignKey(Kutuphane, models.DO_NOTHING, db_column='konumID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rezervasyon'


class Siparis(models.Model):
    siparisid = models.AutoField(db_column='siparisID', primary_key=True)  # Field name made lowercase.
    uyeid = models.ForeignKey(Ogrenciuye, models.DO_NOTHING, db_column='uyeID')  # Field name made lowercase.
    siparistarih = models.DateTimeField(db_column='siparisTarih')  # Field name made lowercase.
    teslimtarih = models.DateTimeField(db_column='teslimTarih')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siparis'


class Siparisurun(models.Model):
    siparisid = models.IntegerField(db_column='siparisID', primary_key=True)  # Field name made lowercase.
    urunid = models.IntegerField(db_column='urunID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siparisurun'
        unique_together = (('siparisid', 'urunid'),)


class Urun(models.Model):
    urunid = models.AutoField(db_column='urunID', primary_key=True)  # Field name made lowercase.
    urunismi = models.CharField(db_column='urunIsmi', max_length=45)  # Field name made lowercase.
    urunpuan = models.IntegerField(db_column='urunPuan', blank=True, null=True)  # Field name made lowercase.
    stok = models.IntegerField(blank=True, null=True)
    urunfotograf = models.TextField(db_column='urunFotograf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'urun'
