import builtins
import sqlalchemy

from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker

from pokedb.classes import Base,Account,Prefix,Observation,Name,Score,Season,Word

engine = create_engine('sqlite:///%s' % 'pokedb.db')

def connectdb():
    DBSession = sessionmaker(bind=engine)
    session=DBSession()
    return(session)

def createdb():
    Base.metadata.create_all(engine)

def insert_account(session,nickname,auth_token,date_now,country_code):
    new_account = Account(nickname=nickname, auth_token=auth_token,
                          date_joined=date_now, date_last_seen=date_now,
                          country_code=country_code,active=True)
    session.add(new_account)
    session.commit()
    return(new_account)


def find_account(session,nickname):
    account_q=session.query(Account).filter(Account.nickname==nickname)
    if account_q.count() > 0:
        return(account_q.first())
    else:
        return None

def insert_prefix(session,inet6num,name_id,date_now,season_id):
    new_prefix = Prefix(inet6num=inet6num,name_id=name_id,
                        date_seen_first=date_now, date_seen_last=date_now,
                        season_first_seen_id=season_id)
    session.add(new_prefix)
    session.commit()
    return(new_prefix)
    
    return()

def find_prefix(session,inet6num):
    prefix_q = session.query(Prefix).filter(prefix==inet6num)
    if prefix_q.count() > 0:
        return(prefix_q.first())
    else
        return None

def insert_season(session,name,date_start,date_end):
    new_season = Season(name=name,date_start=date_start,date_end=date_end)
    session.add(new_season)
    session.commit()
    return(new_season)

def insert_name(session,word_1_id,word_2_id,word_3_id,prefix_id):
    new_name = Name(word_1_id=word_1_id, word_2_id=word_2_id,
                    word_3_id=word_3_id, prefix_id=prefix_id)
    session.add(new_name)
    session.commit()
    return(new_name)

def find_name(word_1_id,word_2_id,word_3_id):
    name_q=session.query(Name).filter(Name.word_1_id==word_1_id).filter(Name.word_2_id==word_2_id).filter(Name.word_3_id==word_3_id)
    if name_q.count() > 0:
        return(name_q.first())
    else
        return None

def insert_word(name):
    new_word = Word(name=name)
    session.add(new_word)
    session.commit()
    return(new_word)

def insert_observation(prefix_id,season_id,account_id,location,points,points_reason):
    new_observation = Observation(prefix_id=prefix_id, season_id=season_id,
                                  account_id=account_id, location=location,
                                  points=points,points_reason=points_reason)
    session.add(new_observation)
    session.commit()
    return(new_observation)

def report_season_score(session,season_id,account_id):
    season_score_q=session.query(Score).filter(Score.account_id==account_id).filter(Score.season_id==season_id)
    if season_score_q.count() > 0:
        return(season_score.first().value)
    else
        return(0)

def report_global_score(session,account_id):
    global_score=0
    global_score_q=session.query(Score).filter(Score.account_id==account_id)
    for row in global_score_q.all():
        global_score=global_score+row.value()
    return(global_score)

        

def add_score(session,account_id,season_id):
    new_score = Score(account_id=account_id,season_id=season_id,value=value)
    session.add(new_score)
    session.commit()
    return(new_score)