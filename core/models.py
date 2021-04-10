from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from rest_framework import routers, serializers, viewsets
from twilio.rest import Client
# Create your models here.
account_sid = 'AC5c02098e2b8867fc74d77cceaecd55af'
auth_token = 'ba78dd79b097140995725d3844a31de5'

class API(models.Model):
    name = models.CharField(max_length=10)
    phone = models.IntegerField()
    location = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    sid = models.CharField(max_length=500,null=True)

    class Meta:
        verbose_name = 'API'
        verbose_name_plural = 'APIs'

    def __str__(self):
        return '{0} {1}'.format(self.name,self.location)

class APISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = API
        fields = ['url', 'name', 'email', 'phone','location']

class APIViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = APISerializer


@receiver(post_save, sender=API)
def sendreport(sender, instance, **kwargs):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body='I need Help!!! I am {0} I am rightnow at {1} My phone number is {2}'.format(instance.name,instance.location,instance.phone),from_='+15085254297',to='+917999776136')
    # send_mail(
    #     'Emergency',
    #     'I need Help!!! I am {0} I am rightnow at {1} My phone number is {2}'.format(instance.name,instance.location,instance.phone),
    #     'starjayp02@gmail.com',
    #     ['{0}'.format(instance.email)],
    #     fail_silently=False,
    # )
    instance.sid = str(message.sid)
    instance.save()