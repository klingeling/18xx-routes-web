import os

#Global
SECRET_KEY = os.environ.get("SECRET_KEY", "d055d10f-0770-437d-8f5f-96d345146841")
TEMPLATES_AUTO_RELOAD = True
EXPLAIN_TEMPLATE_LOADING = False

# WTForms
WTF_CSRF_ENABLED = True
WTF_CSRF_TIME_LIMIT = None

# SendGrid
# MAIL_USERNAME = os.environ['EMAIL_USER']
MAIL_USERNAME = '915157650@qq.com'
