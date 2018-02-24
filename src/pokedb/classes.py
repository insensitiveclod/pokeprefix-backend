#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(20), nullable=False)
    auth_token = Column(String(255), nullable=False)
    date_joined = Column(DateTime, nullable=False)
    date_last_submission = Column(DateTime)
    date_last_seen = Column(DateTime)
    country_code = Column(String(2))
    active = Column(Boolean)

class Word(Base):
    __tablename__ = 'word'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class Season(Base):
    __tablename__ = 'season'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    period_start = Column(DateTime, nullable=False)
    period_duration = Column(DateTime, nullable=False)

class Prefix(Base):
    __tablename__ = 'prefix'
    id = Column(Integer, primary_key=True)
    prefix = Column(Integer)
    date_seen_first = Column(DateTime, nullable=False)
    date_seen_last = Column(DateTime, nullable=False)
    season_first_seen_id = Column(Integer, ForeignKey('season.id'))
    season_first_seen = relationship(Season)

class Name(Base):
    __tablename__ = 'name'
    id = Column(Integer, primary_key=True)
    name_1_id = Column(Integer)
    name_2_id = Column(Integer)
    name_3_id = Column(Integer)
    prefix_id = Column(Integer, ForeignKey('prefix.id'))
    prefix = relationship(Prefix)

class Observation(Base):
    __tablename__ = 'observation'
    id = Column(Integer, primary_key =True)
    prefix_id = Column(Integer, ForeignKey('prefix.id'))
    prefix = relationship(Prefix)
    season_id = Column(Integer, ForeignKey('season.id'))
    season = relationship(Season)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    location = Column(String(255),nullable=False)
    points = int
    points_reason = Column(String(255))

class Score(Base):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    season_id = Column(Integer, ForeignKey('season.id'))
    season = relationship(Season)
    value = Column(Integer)

