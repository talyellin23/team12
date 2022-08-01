from flask import session

from utilities.db.db_manager import dbManager


class User:
    def __init__(self, name, email, phone='-1', birthday='-1', password='-1', age='-1',
                 weight='-1', height='-1', gender='-1', smoker='-1', bmi='-1', bmr='-1', area='-1'):
        super().__init__()
        self.FullName = name
        self.Email = email
        self.PhoneNumber = phone
        self.DateOfBirth = birthday
        self.Password = password
        self.Age = int(age)
        self.Weight = int(weight)
        self.Height = int(height)
        self.Gender = gender
        self.Smoker = smoker
        self.BMI = float(bmi)
        self.BMR = float(bmr)
        self.Area = area

    def getEmail(self):
        return self.Email

    def getName(self, Email):
        query = "SELECT * FROM memberstable WHERE Email='%s';" % self.Email
        result = dbManager.fetch(query)
        for user in result:
            if user.Email == Email:
                return user.FullName

    def getUser(self):
        query = "SELECT * FROM memberstable WHERE Email='%s';" % self.Email
        return dbManager.fetch(query)

    def addUser(self):
        query = f"INSERT INTO memberstable(FullName, Email, PhoneNumber, DateOfBirth, Password) VALUES ('%s','%s','%s','%s','%s')" % (
            self.FullName, self.Email, self.PhoneNumber, self.DateOfBirth, self.Password)
        result = dbManager.commit(query)
        print(result)

    def updateUser(self):
        query = f"UPDATE memberstable SET Password='%s', FullName='%s', PhoneNumber='%s'  WHERE Email='%s'" % (
            self.Password, self.FullName, self.PhoneNumber, self.Email)
        dbManager.commit(query)

    def updateBMI(self):
        query = f"UPDATE memberstable SET Age='%s', Weight='%s', Height='%s', Gender='%s', Smoker='%s', BMI='%f', BMR='%f', Area='%s' WHERE Email='%s'" % \
                (
                    self.Age, self.Weight, self.Height, self.Gender, self.Smoker, self.BMI, self.BMR, self.Area,
                    self.Email)
        dbManager.commit(query)

    def searchUser(self):
        query = 'SELECT * FROM memberstable'
        result = dbManager.fetch(query)
        for member in result:
            if member.Email == self.Email:
                return 'This user already exist!'
            else:
                return ''
        return ''

    def deleteUser(self):
        query = "DELETE FROM memberstable WHERE Email='%s';" % self.Email
        dbManager.commit(query)

    def login(self):
        query = 'SELECT * FROM memberstable'
        users1 = dbManager.fetch(query)
        for user in users1:
            if user.Email == self.Email:
                if user.Password == self.Password:
                    return 'Login Successfully'
                else:
                    return 'Please make sure your password is correct'
        return 'Email does not exist in the system'

    def getExperts(self):
        if session['BMI'] < 18.4:
            query = "SELECT * FROM experttable WHERE (experttable.Reign='%s' OR 'Israel'='%s') and" \
                    " (experttable.Speciality='Nutritionist' OR experttable.Speciality='Family Doctor' OR" \
                    " (experttable.Speciality='Rehab Institute' and 'yes' = '%s')) " \
                    "order by  Speciality" % (
                        session['Area'], session['Area'], session['Smoker'])
        elif 18.4 <= session['BMI'] < 24.9:
            query = "SELECT * FROM experttable WHERE (experttable.Reign='%s' OR 'Israel'='%s') and" \
                    " (experttable.Speciality='Personal Trainer' OR" \
                    " (experttable.Speciality='Rehab Institute' and 'yes' = '%s')) " \
                    "order by  Speciality" % (
                        session['Area'], session['Area'],  session['Smoker'])
        elif 24.9 <= session['BMI'] < 29.9:
            query = "SELECT * FROM experttable WHERE (experttable.Reign='%s' OR 'Israel'='%s') and" \
                    " (experttable.Speciality='Nutritionist' OR experttable.Speciality='Personal Trainer' OR" \
                    " (experttable.Speciality='Rehab Institute' and 'yes' = '%s')) " \
                    "order by  Speciality" % (
                        session['Area'], session['Area'], session['Smoker'])
        else:
            query = "SELECT * FROM experttable WHERE (experttable.Reign='%s' OR 'Israel'='%s') and" \
                    " (experttable.Speciality='Family Doctor' OR" \
                    " (experttable.Speciality='Rehab Institute' and 'yes' = '%s')) " \
                    "order by  Speciality" % (
                        session['Area'], session['Area'], session['Smoker'])

        return dbManager.fetch(query)
