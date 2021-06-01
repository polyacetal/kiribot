# coding: UTF-8

import discord
import sys
import random
import time
import datetime
import kiribot_fn

date = datetime.datetime.now()
client = discord.Client()
vcc = discord.VoiceChannel
vc = discord.VoiceClient
setup = False

@client.event
async def on_ready():
	print("setup successfully")
	print("Wellcome!")
	print("きりたん対話システム")

@client.event
async def on_message(message):
	global setup
	global vc
	global vcc
	prefix = "'"

	if message.author.bot:
		return

	if message.content == prefix+"sh":
		if str(message.author.id) == "567276649339682819":
			await message.channel.send("対戦ありがとうございました")
			await client.change_presence(status = discord.Status.offline)
			print("shutdown successfully")
			await client.logout()
		return

	if message.content.startswith(prefix+"st"):
		if setup == False:
			setup = True
			await message.channel.send("Welcome!\n起動しました")
			print ("steup完了")
		return

	if setup == False:
		return

	if message.content.startswith(prefix+"sk") or message.content.startswith(prefix+"sp"):
		if message.author.voice is not None :
			if vc == discord.VoiceClient or vc.is_connected() == False:
				await message.channel.send('今から接続しますね')
				vcc = message.author.voice.channel
				vc = await vcc.connect()
				await message.channel.send('VC接続しました')
			else:
				await message.channel.send('接続済みです。Over！')
		else :
			await message.channel.send('VCに接続してます？')
		return

	if message.content == (prefix+"tk"):
		if vc.is_connected() == True:
			await message.channel.send('切断作業中....。')
			if vc.is_playing() == True :
				vc.stop()
			await vc.disconnect()
			await message.channel.send('切断しました。\n対戦ありがとうございました')
		else :
			await message.channel.send('VCに接続してませんよ？')
		return

	if message.content == (prefix+"fz"):
		print("1")
		msg = "おしゃべりを中断します\nスリープモードに入ります"
		await message.channel.send(msg)
		setup = False
		print("msg & stop success")
		return

	if message.content.startswith("ありがとう"):
		msg = kiribot_fn.thx()
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("こんにちは"):
		msg , source = kiribot_fn.hello()
		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("こんにちわ"):
		msg , source = kiribot_fn.hello()
		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("hello"):
		msg , source = kiribot_fn.hello()
		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("こんばんは") or message.content.startswith("こんばんわ"):
		if vc != discord.VoiceClient and vc.is_connected() == True:
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\hello2.wav" , options='-application audio')
			vc.play(source)
		await message.channel.send("こんばんは")
		print("msg ans success")
		return

	if message.content.startswith("今何時？"):
		word = "今は{}時{}"
		hour = date.hour
		minute = date.minute
		if minute >= 0 and minute <= 24:
			reply = "くらいですね。"
		elif minute >= 25 and minute <= 34:
			reply = "半くらいですね。"
		elif minute >= 35 and minute <= 49:
			reply = "半過ぎですね。"
		elif minute >= 50 and minute <= 59:
			speech = "くらいですね。\nそろそろ{}時になります。"
			nexthour = hour + 1
			reply = speech.format(nexthour)

		msg = word.format(hour,reply)
		await message.channel.send(msg)
		print("time ans success")
		return

	if message.content.startswith("疲れた"):
		reply = ["そんなときはずんだを食べましょう","お疲れ様です"]
		msg = random.choice(reply)
		if msg == "そんなときはずんだを食べましょう":
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\eatzunda.wav" , options='-application audio')
		elif msg == "お疲れ様です":
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\goodwork.wav" , options='-application audio')

		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("ｷﾘﾀﾝｶﾜｲｲﾔｯﾀｰ"):
		reply = ["……ありがとうございます","なにいってんだこいつ。","ヘンタイさんですね……。","わたし、小学五年生なんですけど……"]
		msg = random.choice(reply)
		if msg == "……ありがとうございます":
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\thx.wav" , options='-application audio')
		elif msg == "なにいってんだこいつ。":
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\what.wav" , options='-application audio')
		elif msg == "ヘンタイさんですね……。":
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\hentai.wav" , options='-application audio')
		elif msg == "わたし、小学五年生なんですけど……":
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\syou5.wav" , options='-application audio')

		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("おはよう"):
		reply = "おはようございます{}"
		hour = date.hour
		source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\hello3.wav" , options='-application audio')
		if  hour <= 3:
			word = "\nってか寝ました？"
			source2 = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\sleep.wav" , options='-application audio')

		elif hour >= 4 and hour <= 5:
			word = "\n早いですね"
			source2 = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\early.wav" , options='-application audio')

		elif hour >= 6 and hour <= 8:
			word = "\n健康的ですね"
			source2 = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\healthy.wav" , options='-application audio')

		elif hour >= 9 and hour <= 11:
			word = "\nって遅くないですか？私も大概ですが..."
			source2 = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\late.wav" , options='-application audio')

		elif hour >= 12:
			word = "\n昼夜逆転ですね..."
			source2 = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\reversal.wav" , options='-application audio')
		msg = reply.format(word)

		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
			vc.play(source2)
		await message.channel.send(msg)
		print("msg ans success")
		return

	if message.content.startswith("ｵﾊﾖ"):
		source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\hello4.wav" , options='-application audio')
		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send("ｵﾊﾖ")
		print("msg ans success")
		return

	if message.content.startswith("草"):
		source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\lol.wav" , options='-application audio')
		if vc != discord.VoiceClient and vc.is_connected() == True:
			vc.play(source)
		await message.channel.send("草生えますね")
		print("msg ans success")
		return

	if vc != discord.VoiceClient and vc.is_connected() == True:
		if message.content.startswith("カウント"):
			source = discord.FFmpegPCMAudio("D:\\Pybot\\kiribot\\voice\\count.wav" , options='-application audio')
			vc.play(source)
			await message.channel.send("すりー……、つー……、わーん……、ぜろー。")
			print("msg voice success")
			return

	msg = kiribot_fn.test(message.content)
	if msg :
		await message.channel.send(msg)
		print("msg ans success")
		return

client.run("")
