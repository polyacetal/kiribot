# coding: UTF-8

import discord
import sys
import random
import time
import datetime

date = datetime.datetime.now()
client = discord.Client()
vcc = discord.VoiceChannel
vc = discord.VoiceClient

voice = "D:\\Pybot\\kiribot\\voice\\"
musices = "D:\\Pybot\\kiribot\\musices"

def thx():
    reply = ["そのように言ってもらえて何よりです","また何かあれば言ってください","どういたしまして"]
    msg = random.choice(reply)
    return msg

def hello():
    msg = "こんにちは"
    source = discord.FFmpegPCMAudio(voice + "hello.wav" , options='-application audio')
    return msg , source

def music():
    pass

def test(mes):
    #if mes == "test":
    msg = "その言葉はまだ知りません"
    return msg
