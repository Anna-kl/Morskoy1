from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key=True)
     chat_id=Column(Integer, unique=True)
     nickname = Column(String)
     dttm=Column(DateTime)

class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    user1 = Column(Integer, ForeignKey("users.id"))
    user2 = Column(Integer, ForeignKey("users.id"))
    dttm=Column(DateTime)
    state = Column(String)
    current=Column(String)

class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("room.id"))
    win=Column(Integer, ForeignKey("users.id"))
    dttm_finish=Column(DateTime)


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    room_id=Column(Integer, ForeignKey("room.id"))
    user_id=Column(Integer, ForeignKey("users.id"))
    name=Column(String)


meta = MetaData()




class DB():
    session=None

    db_string = "postgresql+psycopg2://postgres:2537300@localhost/postgres"
    def __init__(self):
        engine = create_engine(self.db_string, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()

    def get_datawait(self):
        data=self.session.query(User).filter(Room.state=='wait').first()
        return data
    def Add_user(self, message):

        s = User(chat_id=message.chat.id, nickname=message.chat.first_name, dttm=datetime.datetime.now())
        try:
            self.session.add(s)
            self.session.commit()
        except:
            self.__init__()
        return  self.session.query(User).filter(User.chat_id==message.chat.id).first()
    def Greate_room(self, state, data):
        s1=Room(state=state, user1=data.id, dttm=datetime.datetime.now())
        self.session.add(s1)
        self.session.commit()
    def add_user_in_room(self,  message):
        s=self.session.query(Room).filter(Room.state=='wait').first()
        user=self.session.query(User).filter(User.chat_id==message.chat.id).first()
        s.user2=user.id
        s.state='active'
        s.dttm=datetime.datetime.now()
        self.session.commit()
        return s
    def save_file(self, name_file, user,room):
        a=File(user_id=user, room_id=room, name=name_file)
        self.session.add(a)
        self.session.commit()

    def file_room(self, message, number):

        if number=='1':
            user=self.session.query(User).filter(User.chat_id==message.chat.id).first()
            room=self.session.query(Room).filter(Room.user1==user.id).first()
            if room.current == 'user' + number:
                return -1
            elif room.current is None:
                room.current='2'

            file = self.session.query(File).filter(File.id==1).first()
        else:
            user = self.session.query(User).filter(User.chat_id == message.chat.id).first()
            room = self.session.query(Room).filter((Room.user2 == user.id)
                                                   and (Room.state=='active')).first()
            if room.current == 'user' + number:
                return -1
            elif room.current is None:
                room.current = '2'
            file=self.session.query(File).filter(File.id==2).first()
        return file
    def change_flag(self, number, id):
        room = self.session.query(Room).filter(Room.id == id).first()
        room.current='user'+number
        self.session.commit()

