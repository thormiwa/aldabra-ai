import asyncio

from asgiref.sync import sync_to_async

from django.utils import timezone
from django.conf import settings
from django.utils.timezone import timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.triggers.cron import CronTrigger

# COMMON
from django.shortcuts import (
    redirect, 
    get_object_or_404,
)

from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.http.response import Http404

# Model
from .models import Appointment

## default Mail list
Mail_List = {
    'sender': 'amidbidee@gmail.com',
}

def sendEmailNotification(subject, email_address, sender, html_con, text_con=None):
    html_content = html_con
    text_content = text_con
    msg = EmailMultiAlternatives(subject, html_content, sender, [email_address])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

## Send Email Notification To Doctor on Appointment Request
def notifyDoctor(*args, **kwargs):
    ## get appointment and doctors email, well you should know that
    appointment = get_object_or_404(Appointment, appointment_id=kwargs['appointment_id'])
    email_address = appointment.get_doctor_email

    ## appointment detail url
    appointment_url = appointment.get_absolute_url()

    ## THIS IS FOR DEVELOPMENT PURPOSE USING DJANGO SMTP MAIL TOOL
    Mail_List = {
        'subject': 'Appointment Request',
        'email_address': email_address,

        'text': "Someone Requested an Appointment with you, please review it here",
        'html': f"<p>Someone Requested an Appointment with you, please review it <a href='https://127.0.0.1:3000/{appointment_url}'>here</a></p>",
        'sender': 'amidbidee@gmail.com'
    }

    sendEmailNotification(
        Mail_List['subject'], 
        Mail_List['email_address'], 
        Mail_List['sender'], 
        Mail_List['html'])
    
    ## redirect to homepage(for now)
    return redirect('home')


def acceptSetTimer(request, appointment_id):
    ## get appointment
    appointment = get_object_or_404(Appointment, appointment_id=appointment_id)

    if appointment:
       try:
           if appointment.appointment_state == 'AC':
               pass
           else:
               appointment.setState('AC') ## set appointment state AC:Accepted
               appointment.booked = True
               appointment.save()

           dt = appointment.appointment_dt

           ## THIS IS FOR DEVELOPMENT PURPOSE USING DJANGO SMTP MAIL TOOL
           Mail_List = {
               'doctor_email': appointment.get_doctor_email,
               'patient_email': appointment.get_patient_email,

               'subject1': "Appointment has  been set to",
               'subject2': "Appointment Booked and Accepted",

               'text1': f"""
                                 An Appointment as been set for 
                                 date:'{dt}'
                        """,
               'html1': f"""
                                 <p>
                                 An Appointment as been set for;
                                 date:'{dt}'
                                 </p>
                        """,

               'text2': f"""
                                 Your Appointment has been accepted and successfully booked.
                                 Appointment as been set for;
                                 date:'{dt}', 
                        """,
               'html2': f"""
                                 <p>
                                 Your Appointment has been accepted and successfully booked.
                                 Appointment as been set for;
                                 date:'{dt}'
                                 </p>
                        """,
           }

           sendEmailNotification(
               Mail_List['subject1'], 
               Mail_List['doctor_email'], 
               Mail_List['sender'], 
               Mail_List['html1'])
           sendEmailNotification(
               Mail_List['subject2'], 
               Mail_List['patient_email'], 
               Mail_List['sender'], 
               Mail_List['html2'])
           
       except appointment.DoesNotExist:
           return Http404

    return redirect('appointment:dashboard')


def declineDelete(request, appointment_id):
    appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
    
    if appointment:
        try:
            if appointment.appointment_state == 'DE':
                pass
            else: 
                appointment.setState('DE') ## DE:Decline
                appointment.booked = False
                appointment.save()

            ## THIS IS FOR DEVELOPMENT PURPOSE USING DJANGO SMTP MAIL TOOL
            Mail_List = {
                'patient_email': appointment.get_patient_email,
                'subject': 'Appointment Declined',

                'text': f"""
                             Your Requested Appointment was declined,
                             the following reasons were provided; {appointment.doctor_dec_reason}
                        """,
                        
                'html': f"""
                            <p>
                             Your Requested Appointment was declined,
                             the following reasons were provided; {appointment.doctor_dec_reason}
                            </p>
                        """
        }

        except appointment.DoesNotExist:
            return Http404

    return redirect('home')


def get_appointment(request, appointment_id):
    appointment = Appointment.objects.get(appointment_id=appointment_id)
    return appointment

def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

def start_appointment_thread(*args, **kwargs):
    s = BlockingScheduler(timezone=settings.TIME_ZONE)
    s.add_jobstore(DjangoJobStore(), 'default')
    appointment = get_object_or_404(Appointment, appointment_id=kwargs['appointment_id'])

    if appointment.appointment_dt < timezone.now():
        s.add_job(notifyDoctor, 
        trigger=CronTrigger(start_date=appointment.appointment_dt, timezone=settings.TIME_ZONE), 
        id='new_appointment',
        max_instances=1,
        replace_existing=True,
        kwargs={'appointment_id': kwargs['appointment_id']}
        )
        s.start()