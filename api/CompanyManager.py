from django.db import connection


class CompanyManager():
    def __init__(self):
        pass

    @staticmethod
    def format_boolean(value):
        return 'TRUE' if value else 'FALSE'

    @staticmethod
    def format_date(value):
        return value.isoformat()

    @staticmethod
    def format_datetime(value):
        return value.isoformat()

    @staticmethod
    def delete(c):
        pass

    @staticmethod
    def update(c):
        cursor = connection.cursor()
        query = """UPDATE ayudacontador_company
                   SET name='{0}',
                       email='{1}',
                       contact_email='{2}',
                       contact_phone='{3}',
                       contact_first_name='{4}',
                       contact_last_name='{5}',
                       web='{6}',
                       description='{7}',
                       logo='{8}',
                       invoicing_data='{9}',
                       lead_quota='{10}',
                       notes='{11}',
                       subscription_active='{12}',
                       lead_active='{13}',
                       last_notification_date='{14}',
                       received_leads_count={15},
                       trial_start_date='{16}',
                       remove_from_guide='{17}',
                       mailing_active='{18}',
                       created='{19}'
                   WHERE id={20};""".format(
            c.name,
            c.email,
            c.contact_email,
            c.contact_phone,
            c.contact_first_name,
            c.contact_last_name,
            c.web,
            c.description,
            c.logo,
            c.invoicing_data,
            c.lead_quota,
            c.notes,
            CompanyManager.format_boolean(c.subscription_active),
            CompanyManager.format_boolean(c.lead_active),
            CompanyManager.format_datetime(
                c.last_notification_date),
            c.received_leads_count,
            CompanyManager.format_date(c.trial_start_date),
            CompanyManager.format_boolean(c.remove_from_guide),
            CompanyManager.format_boolean(c.mailing_active),
            CompanyManager.format_datetime(c.created),
            c.id)

        cursor.execute(query)

    @staticmethod
    def insert(c):
        cursor = connection.cursor()
        query = """INSERT INTO res_partner
                   (name,email,display_name,company_id,active,customer,supplier,phone,street)
                   VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}');""".format(
            c.name,
            c.email,
            c.name,
            '1',
            'True',
            'True',
            'False',
            c.phone,
            c.street)

        cursor.execute(query)

    @staticmethod
    def all():
        cursor = connection.cursor()
        query = """SELECT name,email,id
                  FROM res_partner;"""

        cursor.execute(query)
        objects = []

        from .models import Company

        for row in cursor.fetchall():
            c = Company()
            c.name = row[0]
            c.email = row[1]
            c.id = row[2]
            objects.append(c)

        return objects

    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = """SELECT name,email,id
                   FROM res_partner
                   WHERE id={0};""".format(id)

        cursor.execute(query)
        objects = []

        from .models import Company

        for row in cursor.fetchall():
            c = Company()
            c.name = row[0]
            c.email = row[1]
            c.id = row[2]
            objects.append(c)

        return None if len(objects) == 0 else objects[0]
