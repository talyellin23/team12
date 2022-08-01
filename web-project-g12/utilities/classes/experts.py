from utilities.db.db_manager import dbManager


class Expert:
    def _init_(self, firstname='-1', familyname='-1', speciality='-1', reign='-1', address='-1'):
        self.FirstName = firstname
        self.FamilyName = familyname
        self.Speciality = speciality
        self.Reign = reign
        self.Address = address

    def get_specialty(self):
        return self.Speciality

    def get_expert(self):
        query = "SELECT * FROM experttable WHERE name='%s';" % self.idE
        return dbManager.fetch(query)

    def add_expert(self):
        query = f"INSERT INTO experttable(FirstName, FamilyName, Speciality, Reign, Address) VALUES ('%s','%s','%s','%s','%s')" % (
            self.FirstName, self.FamilyName, self.Speciality, self.Reign, self.Address)
        dbManager.commit(query)
