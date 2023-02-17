class Contact_list:
    
    def __init__(self, name, list_of_ppl):
        self.name = name
        self.list_of_ppl = sorted(list_of_ppl, key=lambda user: user['name'])
        self.duplicate = []

    def add_contact(self, contact):
        self.list_of_ppl.append(contact)
        self.list_of_ppl = sorted(self.list_of_ppl, key=lambda user: user['name'])

    def remove_contact(self, name):
        for c in self.list_of_ppl:
            if c['name'] == name:
                self.list_of_ppl.remove(c)

    def same_contact(self, other_list):
        share = []
        for i in self.list_of_ppl:
            if i in other_list.list_of_ppl:
                share.append(i)
        return Contact_list(f"{self.name} - {other_list}", share)

            
friends = [{'name':'Bob', 'number':'555-5555'}, {'name':'Alice','number':'867-5309'}]   
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Emm', 'number':'555-5555'},{'name':'Bob', 'number':'555-5555'}]

my_work_buddies = Contact_list('Work Buddies', work_buddies)
my_friends_list = Contact_list('My Friends', friends)

friends_i_work_with = my_friends_list.same_contact(my_work_buddies)
print(friends_i_work_with.list_of_ppl)

print(my_work_buddies.add_contact)


print(my_work_buddies.name)
print(my_work_buddies.list_of_ppl)