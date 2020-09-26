# To Do list project - stage 2/4
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sys import exit

Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date)

    def __repr__(self):
        """
                it will look like this format
                id. task
                id. task
                id. task
                """
        return f"{self.id}. {self.task}"

class ToDoList:

    def __init__(self, db_name):
        # table and database initializing
        self.engine = create_engine(f'sqlite:///{db_name}.db?check_same_thread=False')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        # session initializing
        self.session = Session()

    def menu(self):
        print("\n1) Today's tasks\n2) Add task\n0) Exit")
        action = int(input())
        if action == 1:
            self.today_task()
        elif action == 2:
            self.add_task(input("\nEnter Task\n>"))
        elif action == 0:
            # It exits the session with a system exit. No need to terminate with flags.
            print("\nBye!")
            exit(1)

    def today_task(self):
        rows = self.session.query(Table).all()
        if len(rows) == 0:
            print("\nToday:\nNothing to do!")
        else:
            for row in rows:
                print(f"{row.id}. {row.task}")

    def add_task(self, task_name):
        new_row = Table(task=task_name)
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!")

my_list = ToDoList("todo")
while True:
    my_list.menu()