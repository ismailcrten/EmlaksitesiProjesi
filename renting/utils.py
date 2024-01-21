from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings


class MailHandler:
    # send email to superadmin user
    @staticmethod
    def contact_send_mail(_name, _email, _phone, _subject, _message):
        with get_connection(  
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = _subject
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = ['help.rentapart@gmail.com', ]  
           message = _message
           html_content = f"""
                    <div style='font-family:monospace'>
                        <div style='display:flex;justify-content:center'>
                            <h2>GOLDEN RENT İLETİŞİM MESAJI</h2>
                        </div>
                        <div>
                            <h3>Kullanıcı İletişim Bilgileri</h3>
                            <div style='border: 1px solid #0000002e; border-radius:3px; padding:10px; width: 75%'>
                                <p style='margin: 0px;'>İsim : <b>{_name}</b></p>
                                <p style='margin: 5px 0px;'>Kullanıcı mail : <b>{_email}</b></p>
                                <p style='margin: 5px 0px;'>Kullanıcı telefon numarası : <b>{_phone}</b></p>
                            </div>
                            <br>
                            <h3>Kullanıcı Mesajı</h3>
                            <p style='margin: 0px;'>{_message}</p>
                            <br>
                        
                        </div>
                    </div>
                        """
           msg = EmailMultiAlternatives(subject, message, email_from, recipient_list, connection=connection)
           msg.attach_alternative(html_content, "text/html")
           msg.send()