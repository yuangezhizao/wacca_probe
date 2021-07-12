#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/12 23:33
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
from wacca_probe.plugins.extensions import db


class Record(db.Model):
    __bind_key__ = 'wacca'
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)

    scoreId = db.Column(db.Integer)
    modeName = db.Column(db.VARCHAR(50))
    comboCount = db.Column(db.Integer)
    # productId = db.Column(db.Integer)
    musicRate = db.Column(db.VARCHAR(50))
    gameDate = db.Column(db.DateTime, nullable=False)
    storeId = db.Column(db.Integer)
    greatCount = db.Column(db.Integer)
    # productName = db.Column(db.VARCHAR(50))
    # machineName = db.Column(db.VARCHAR(50))
    musicName = db.Column(db.VARCHAR(50))
    score = db.Column(db.Integer)
    marvelousCount = db.Column(db.Integer)
    machineId = db.Column(db.Integer)
    musicId = db.Column(db.Integer)
    goodCount = db.Column(db.Integer)
    musicGradeName = db.Column(db.VARCHAR(50))
    storeName = db.Column(db.VARCHAR(50))
    artistName = db.Column(db.VARCHAR(50))
    musicGrade = db.Column(db.Integer)
    musicImage = db.Column(db.VARCHAR(255))
    missCount = db.Column(db.Integer)

    cache_dt = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, level_img_s, scoreId, modeName, comboCount, musicRate, gameDate, storeId, greatCount,
                 musicName, score, marvelousCount, machineId, musicId, goodCount, musicGradeName, storeName, artistName,
                 musicGrade, musicImage, missCount, cache_dt):
        self.id = id
        self.level_img_s = level_img_s
        self.scoreId = scoreId
        self.modeName = modeName
        self.comboCount = comboCount
        self.musicRate = musicRate
        self.gameDate = gameDate
        self.storeId = storeId
        self.greatCount = greatCount
        self.musicName = musicName
        self.score = score
        self.marvelousCount = marvelousCount
        self.machineId = machineId
        self.musicId = musicId
        self.goodCount = goodCount
        self.musicGradeName = musicGradeName
        self.storeName = storeName
        self.artistName = artistName
        self.musicGrade = musicGrade
        self.musicImage = musicImage
        self.missCount = missCount
        self.cache_dt = cache_dt

    def __repr__(self):
        return '<Record (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.level_img_s, self.scoreId, self.modeName, self.comboCount, self.musicRate, self.gameDate,
            self.storeId, self.greatCount, self.musicName, self.score, self.marvelousCount, self.machineId,
            self.musicId, self.goodCount, self.musicGradeName, self.storeName, self.artistName, self.musicGrade,
            self.musicImage, self.missCount, self.cache_dt)

    def to_json(self):
        record = {
            'id': self.id,
            'level_img_s': self.level_img_s,
            'scoreId': self.scoreId,
            'modeName': self.modeName,
            'comboCount': self.comboCount,
            'musicRate': self.musicRate,
            'gameDate': self.gameDate,
            'storeId': self.storeId,
            'greatCount': self.greatCount,
            'musicName': self.musicName,
            'score': self.score,
            'marvelousCount': self.marvelousCount,
            'machineId': self.machineId,
            'musicId': self.musicId,
            'goodCount': self.goodCount,
            'musicGradeName': self.musicGradeName,
            'storeName': self.storeName,
            'artistName': self.artistName,
            'musicGrade': self.musicGrade,
            'musicImage': self.musicImage,
            'missCount': self.missCount,
            'cache_dt': self.cache_dt
        }
        return record

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
