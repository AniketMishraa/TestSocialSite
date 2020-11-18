from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField(max_length = 20)
	profile_pic = models.ImageField(upload_to='profile_pic')
	

	def __str__(self):
		return self.user.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)







