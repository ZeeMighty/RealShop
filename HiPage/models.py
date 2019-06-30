from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Good(models.Model):
    Name = models.CharField(max_length = 150)
    Type = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)
    Available = models.CharField(max_length = 50)
    Photo = models.ImageField(upload_to = 'clothes_photos')
    Price = models.IntegerField(default = '0')
    Discount = models.IntegerField(default = '0')
    Size = models.ManyToManyField('Size')
    URL = models.CharField(max_length = 50, default = " ")


    def __str__(self):
        return self.Name

class Type(models.Model):
    type = models.CharField(max_length = 50, default = " ")

    def __str__(self):
        return self.type

class Size(models.Model):
    size = models.CharField(max_length = 150)

    def __str__(self):
        return self.size


class Good_Get(models.Model):
    Size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length = 150, default = " ")
#    Available = models.CharField(max_length = 50, default = " ")
    Photo = models.ImageField(default = " ")
    Price = models.CharField(max_length = 10, default = '0')

    def __str__(self):
        return str(self.Size)

class UserGood(Good_Get):
    class Meta:
        ordering = ('Size', 'Name', 'Photo', 'Price')
        proxy = True

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email = email,
            username = username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length = 20, default = "")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
