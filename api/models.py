from .CompanyManager import CompanyManager


class Company:
    objects = CompanyManager()

    def __init__(self):
        # the private key
        self.id = None

        # title or name (for displaying purposes)
        # of this company (required)
        self.name = None

        # email where all emails generated to this company
        # will be redirected (required)
        self.email = None

        # email of the contact person, in case is different
        # from leads_email (optional)
        # self.contact_email = None

        # phone of the contact person where calls to this company
        # should be directed (optional)
        # self.contact_phone = None

        # contact person first name (optional)
        # self.contact_first_name = None

        # contact person last name (optional)
        # self.contact_last_name = None

        # ... and many more fields ...
    def save(self):
        if self.id is not None:
            self.objects.update(self)
        else:
            self.objects.insert(self)

    def delete(self):
        self.objects.delete(self)
