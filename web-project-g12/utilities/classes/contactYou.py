from utilities.db.db_manager import dbManager


class Contact:
    def __init__(self, name='-1', email='-1', phone='-1', time='-1', reason='-1', create='-1'):
        self.FullName = name
        self.Email = email
        self.PhoneNumber = phone
        self.TimeOfContact = time
        self.Reason = reason
        self.CreateDate = create

    def addContact(self):
        query = f"INSERT INTO contacttable(FullName, Email, PhoneNumber, TimeOfContact, Reason, CreateDate) VALUES ('%s','%s','%s','%s','%s','%s')" % (
            self.FullName, self.Email, self.PhoneNumber, self.TimeOfContact, self.Reason, self.CreateDate)
        result = dbManager.commit(query)
        print(result)
