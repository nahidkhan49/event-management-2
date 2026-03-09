from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from event.models import Event


@receiver(m2m_changed, sender=Event.participant.through)
def send_rsvp_email(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            user = instance.participant.get(id=user_id)

            send_mail(
                subject="RSVP Confirmation",
                message=f"You have successfully RSVP'd for {instance.title}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
