from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,
            from_email='ya.kaban-kru4e-vseh@yandex.ru',
            to=['kaban-kru4e-vseh@mail.ru', ],
        )
        msg.attach_alternative(html_content, "text/html")

        msg.send()

        return redirect('appointments:make_appointment')


