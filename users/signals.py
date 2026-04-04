from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from urllib.parse import quote


from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        token = default_token_generator.make_token(instance)

        activation_link = f"https://event-management-2-3zlo.onrender.com/users/activate/{uid}/{token}/"

        email = EmailMultiAlternatives(
            subject="Activate Your Account",
            body=f"Hello {instance.username},\n\nClick this link:\n{activation_link}",
            from_email=settings.EMAIL_HOST_USER,
            to=[instance.email]
        )

        email.content_subtype = "plain"
        email.send()
        
        
@receiver(post_save,sender=User)
def assign_default_role(sender,instance,created,**kwergs):
    if created:
        group,_=Group.objects.get_or_create(name='Participant')
        instance.groups.add(group)