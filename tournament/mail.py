from django.core import mail
from django.template import Context
from django.template.loader import render_to_string

connection = mail.get_connection()


def send_confirmation_email(user_dict, path_to_body):
    """Send a generic message."""
    cont = Context(user_dict)  # Allows for passing of content to HTML template
    html_content = render_to_string(path_to_body + ".html", cont)  # Both are needed due to the way Django handles
    txt_content = render_to_string(path_to_body + ".txt", cont)    # html form rendering

    email = mail.EmailMultiAlternatives("Registration confirmation", txt_content)
    email.attach_alternative(html_content, 'text/html')  # TODO Figure out why this is needed
    email.to = [user_dict['email']]
    email.send()


