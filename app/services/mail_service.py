from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import config

# Create mail connection configuration
mail_conf = ConnectionConfig(
    MAIL_USERNAME=config.mail_username,
    MAIL_PASSWORD=config.mail_password,
    MAIL_FROM=config.mail_from,
    MAIL_PORT=config.mail_port,
    MAIL_SERVER=config.mail_server,
    MAIL_FROM_NAME=config.mail_from_name,
    MAIL_STARTTLS=config.mail_starttls,
    MAIL_SSL_TLS=config.mail_ssl_tls,
    USE_CREDENTIALS=config.use_credentials,
    VALIDATE_CERTS=config.validate_certs,
)

# Initialize FastMail instance
fastmail = FastMail(mail_conf)

class MailService:
    @staticmethod
    async def send_email(
        subject: str,
        recipients: list[str],
        body: str,
        subtype: str = "html"
    ):
        """
        Send an email using fastapi-mail
        
        Args:
            subject: Email subject
            recipients: List of recipient email addresses
            body: Email body content
            subtype: Email body type ('html' or 'plain')
        """
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype=MessageType.html if subtype == "html" else MessageType.plain,
        )
        
        await fastmail.send_message(message)
    
    @staticmethod
    async def send_todo_notification(
        recipient: str,
        todo_title: str,
        action: str = "created"
    ):
        """
        Send a todo notification email
        
        Args:
            recipient: Recipient email address
            todo_title: Title of the todo item
            action: Action performed (created, updated, deleted, etc.)
        """
        subject = f"Todo {action.capitalize()}: {todo_title}"
        body = f"""
        <html>
            <body>
                <h2>Todo {action.capitalize()}</h2>
                <p>Your todo item "<strong>{todo_title}</strong>" has been {action}.</p>
                <p>Thank you for using Todo FastAPI!</p>
            </body>
        </html>
        """
        
        await MailService.send_email(
            subject=subject,
            recipients=[recipient],
            body=body,
            subtype="html"
        )

