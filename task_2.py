class Tester:

    def __init__(self, name):
        self.tester_name = name

    def work_hard(self, deadline=True):
        if deadline:
            print(self.tester_name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.tester_name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)