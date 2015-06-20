class Registration:
    def __init__(self, repository):
        self.repository = repository

    def registerUser(self, user):
        if( len(self.repository.findUsers()) == 0):
            user.setAdmin()
        self.repository.registerUser(user)



class Repository:

    #records = [{"name":"user1"}, {"name":"user2"}, {"name":"user3"}]
    records = []

    def findUsers2(self):
        users = []
        for record in Repository.records:
            users.append( User(record["name"]) )
        return users

    def findUsers(self):
        users = None
        if( len(Repository.records)>0 ):
            users = []
            for record in Repository.records:
                users.append( User(record["name"]) )
        return users

    def registerUser(self, newUser):
        pass

class User:
    def __init__(self, username):
        self.username = username
        self.admin = False

    def setAdmin(self):
        self.admin = True

r = Registration( Repository() )
r.registerUser( User("john") )
