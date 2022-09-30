import discord
from discord.ext import commands
import os
import time
import datetime
import asyncio

availableMember = []
bot = commands.Bot(command_prefix='$')

srcPath = (__file__)
srcPath = srcPath.replace("\\", "/")
srcPath = srcPath.replace("HuTaoBot_Initial.py", "")

token = ''

# ====================================================================================================
@bot.event
async def on_ready():
    print("HuTaoBot - Login\n=====================")
    print("Src Path : "+ srcPath)
    print("Current Time : "+ str(datetime.datetime.now().time()) + " / Server Time : KST. - 9 Hours")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("$캐릭터 / $성유물 / $무기 / $파밍"))

# ====================================================================================================

@bot.command()
async def 바람행자(ctx):
    lumineImage = discord.File(str(srcPath)+"src/character/lumine.jpg", filename="lumine.jpg")
    lumineSetEmbed = discord.Embed(title="여행자 · 루미네", color=0xF7F4E3)
    lumineSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 매의 검 / 천공의 검 / 반암결록 / 부식의 검 / 칠흑검", inline=False)
    lumineSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 2세트 + 검투사 2세트 / 청록 4세트", inline=False)
    lumineSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    lumineSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    lumineSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %\n- 바람 원소 피해 %", inline=True)
    lumineSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %\n", inline=True)
    #lumineSetEmbed.set_footer(text="fdsffsdfsdfsdfd")
    lumineSetEmbed.set_thumbnail(url="attachment://lumine.jpg")
    await ctx.message.delete()
    await ctx.send(file=lumineImage, embed=lumineSetEmbed, delete_after=300.0)

@bot.command()
async def 설탕(ctx):
    sucroseImage = discord.File(str(srcPath)+"src/character/sucrose.png", filename="sucrose.png")
    sucroseSetEmbed = discord.Embed(title="무해한 달콤함 · 설탕", color=0xCEE7CA)
    sucroseSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 만국 항해용해도 / 페보니우스 비전 / 드래곤 슬래이어 영웅담", inline=False)
    #sucroseSetEmbed.add_field(name="추천 특성 순서", value="원소 폭발 Q - 원소 스킬 E - 일반 공격", inline=False)
    sucroseSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 4세트 / 유배자 4세트", inline=False)
    sucroseSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 원소 마스터리 / 원소 충전 효율 %", inline=False)
    sucroseSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 마스터리\n- 원소 충전 효율 %", inline=True)
    sucroseSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 원소 마스터리", inline=True)
    sucroseSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 원소 마스터리", inline=True)
    sucroseSetEmbed.set_thumbnail(url="attachment://sucrose.png")
    await ctx.message.delete()
    await ctx.send(file=sucroseImage, embed=sucroseSetEmbed, delete_after=300.0)

@bot.command()
async def 진(ctx):
    jeanImage = discord.File(str(srcPath)+"src/character/jean.jpg", filename="jean.jpg")
    jeanSetEmbed = discord.Embed(title="민들레 기사 · 진", color=0xFFDCA3)
    jeanSetEmbed.add_field(name="🗡️ │ 🗡️ │ 추천 무기", value="- 천공의 검 / 매의 검 / 참봉의 칼날 / 페보니우스 검 / 부식의 검", inline=False)
    # jeanSetEmbed.add_field(name="추천 특성 순서", value="- 원소 폭발 Q - 원소 스킬 E - 일반 공격", inline=False)
    jeanSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 2세트 + 검투사 2세트 / 청록 4세트", inline=False)
    jeanSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    jeanSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    jeanSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 바람 원소 피해 %", inline=True)
    jeanSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 원소 마스터리", inline=True)
    jeanSetEmbed.set_thumbnail(url="attachment://jean.jpg")
    await ctx.message.delete()
    await ctx.send(file=jeanImage, embed=jeanSetEmbed, delete_after=300.0)

@bot.command()
async def 소(ctx):
    xiaoImage = discord.File(str(srcPath)+"src/character/xiao.jpg", filename="xiao.jpg")
    xiaoSetEmbed = discord.Embed(title="호법야차 · 소", color=0x60BFAA)
    xiaoSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 화박연 / 관홍의 창 / 호마의 지팡이 / 결투의 창 / 흑암창", inline=False)
    # xiaoSetEmbed.add_field(name="추천 특성 순서", value="일반 공격 - 원소 폭발 Q - 원소 스킬 E", inline=False)
    xiaoSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 2세트 + 검투사 2세트", inline=False)
    xiaoSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    xiaoSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    xiaoSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 바람 원소 피해 %", inline=True)
    xiaoSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    xiaoSetEmbed.set_thumbnail(url="attachment://xiao.jpg")
    await ctx.message.delete()
    await ctx.send(file=xiaoImage, embed=xiaoSetEmbed, delete_after=300.0)

@bot.command()
async def 벤티(ctx):
    ventiImage = discord.File(str(srcPath)+"src/character/venti.jpg", filename="venti.jpg")
    ventiSetEmbed = discord.Embed(title="바람의 시인 · 벤티", color=0x9BC5A1)
    ventiSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 종말 탄식의 노래 / 천공의 날개 / 절현 / 페보니우스 활", inline=False)
    #ventiSetEmbed.add_field(name="추천 특성 순서", value="- 원소 폭발 Q - 원소 스킬 E - 일반 공격", inline=False)
    ventiSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 4세트", inline=False)
    ventiSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    ventiSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 충전 효율 %", inline=True)
    ventiSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 바람 원소 피해 %", inline=True)
    ventiSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    ventiSetEmbed.set_thumbnail(url="attachment://venti.jpg")
    await ctx.message.delete()
    await ctx.send(file=ventiImage, embed=ventiSetEmbed, delete_after=300.0)

# ====================================================================================================

@bot.command()
async def 타르탈리아(ctx):
    tartagliaImage = discord.File(str(srcPath)+"src/character/tartaglia.png", filename="tartaglia.png")
    tartagliaSetEmbed = discord.Embed(title="귀공자 · 타르탈리아", color=0xC98443)
    tartagliaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 날개 / 청록의 사냥활", inline=False)
    tartagliaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 몰락 2세트 + 왕실 2세트 / 몰락 4세트", inline=False)
    tartagliaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    tartagliaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    tartagliaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물 원소 피해 %", inline=True)
    tartagliaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    tartagliaSetEmbed.set_thumbnail(url="attachment://tartaglia.png")
    await ctx.message.delete()
    await ctx.send(file=tartagliaImage, embed=tartagliaSetEmbed, delete_after=300.0)

@bot.command()
async def 모나(ctx):
    monaImage = discord.File(str(srcPath)+"src/character/mona.jpg", filename="mona.jpg")
    monaSetEmbed = discord.Embed(title="별하늘의 물거울 · 모나", color=0x6670B8)
    monaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 음유시인의 악장", inline=False)
    monaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 4세트", inline=False)
    monaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    monaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    monaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물 원소 피해 %", inline=True)
    monaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    monaSetEmbed.set_thumbnail(url="attachment://mona.jpg")
    await ctx.message.delete()
    await ctx.send(file=monaImage, embed=monaSetEmbed, delete_after=300.0)

@bot.command()
async def 바바라(ctx):
    barbaraImage = discord.File(str(srcPath)+"src/character/barbara.jpg", filename="barbara.jpg")
    barbaraSetEmbed = discord.Embed(title="빛나는 아이돌 · 바바라", color=0xD7CDB6)
    barbaraSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 드래곤 슬레이어 영웅담", inline=False)
    barbaraSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 소녀 4세트 / 유배자 4세트", inline=False)
    barbaraSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 원소 충전 효율 %", inline=False)
    barbaraSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 충전 효율 %", inline=True)
    barbaraSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %", inline=True)
    barbaraSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- HP %\n- 치유 보너스 %", inline=True)
    barbaraSetEmbed.set_thumbnail(url="attachment://barbara.jpg")
    await ctx.message.delete()
    await ctx.send(file=barbaraImage, embed=barbaraSetEmbed, delete_after=300.0)

@bot.command()
async def 행추(ctx):
    xingqiuImage = discord.File(str(srcPath)+"src/character/xingqiu.png", filename="xingqiu.png")
    xingqiuSetEmbed = discord.Embed(title="의기충천 · 행추", color=0x3F6F8A)
    xingqiuSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 검 / 제례검", inline=False)
    xingqiuSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 2세트 + 몰락 2세트 / 왕실 4세트", inline=False)
    xingqiuSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    xingqiuSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    xingqiuSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물 원소 피해 %", inline=True)
    xingqiuSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    xingqiuSetEmbed.set_thumbnail(url="attachment://xingqiu.png")
    await ctx.message.delete()
    await ctx.send(file=xingqiuImage, embed=xingqiuSetEmbed, delete_after=300.0)

# ====================================================================================================

@bot.command()
async def 치치(ctx):
    qiqiImage = discord.File(str(srcPath)+"src/character/qiqi.jpg", filename="qiqi.jpg")
    qiqiSetEmbed = discord.Embed(title="차가운 환혼의 밤 · 치치", color=0x99B5EE)
    qiqiSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 제례검", inline=False)
    qiqiSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 소녀 4세트", inline=False)
    qiqiSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 원소 충전 효율 %", inline=False)
    qiqiSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    qiqiSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    qiqiSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치유 보너스 %", inline=True)
    qiqiSetEmbed.set_thumbnail(url="attachment://qiqi.jpg")
    await ctx.message.delete()
    await ctx.send(file=qiqiImage, embed=qiqiSetEmbed, delete_after=300.0)

@bot.command()
async def 케이아(ctx):
    kaeyaImage = discord.File(str(srcPath)+"src/character/kaeya.png", filename="kaeya.png")
    kaeyaSetEmbed = discord.Embed(title="한풍의 검사 · 케이아", color=0x5782A8)
    kaeyaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 매의 검 / 천공의 검 / 페보니우스 검 / 부식의 검", inline=False)
    kaeyaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 얼음 2세트 + 왕실 2세트", inline=False)
    kaeyaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    kaeyaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    kaeyaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 얼음 원소 피해 %", inline=True)
    kaeyaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %", inline=True)
    kaeyaSetEmbed.set_thumbnail(url="attachment://kaeya.png")
    await ctx.message.delete()
    await ctx.send(file=kaeyaImage, embed=kaeyaSetEmbed, delete_after=300.0)

@bot.command()
async def 감우(ctx):
    ganyuImage = discord.File(str(srcPath)+"src/character/ganyu.jpg", filename="ganyu.jpg")
    ganyuSetEmbed = discord.Embed(title="리월의 수호자 · 감우", color=0x77BCFF)
    ganyuSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 아모스의 활 / 천공의 날개 / 청록의 사냥활", inline=False)
    ganyuSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 얼음 4세트 / 얼음 2세트 + 검투사 2세트 / 악단 4세트", inline=False)
    ganyuSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 공격력 % / 원소 충전 효율 %", inline=False)
    ganyuSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    ganyuSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 얼음 원소 피해 %", inline=True)
    ganyuSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %\n(악단세트 적용)", inline=True)
    ganyuSetEmbed.set_thumbnail(url="attachment://ganyu.jpg")
    await ctx.message.delete()
    await ctx.send(file=ganyuImage, embed=ganyuSetEmbed, delete_after=300.0)

@bot.command()
async def 디오나(ctx):
    dionaImage = discord.File(str(srcPath)+"src/character/diona.png", filename="diona.png")
    dionaSetEmbed = discord.Embed(title="캐츠라인 칵테일 · 디오나", color=0xFEAB9D)
    dionaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 제례활", inline=False)
    dionaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 4세트 / 소녀 4세트", inline=False)
    dionaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 원소 충전 효율 %", inline=False)
    dionaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 충전 효율 %", inline=True)
    dionaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n- 원소 충전 효율 %", inline=True)
    dionaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- HP %", inline=True)
    dionaSetEmbed.set_thumbnail(url="attachment://diona.png")
    await ctx.message.delete()
    await ctx.send(file=dionaImage, embed=dionaSetEmbed, delete_after=300.0)

@bot.command()
async def 중운(ctx):
    chongyunImage = discord.File(str(srcPath)+"src/character/chongyun.png", filename="chongyun.png")
    chongyunSetEmbed = discord.Embed(title="얼어붙은 정열 · 중운", color=0x99B5EE)
    chongyunSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 늑대의 말로 / 천공의 긍지 / 제례 대검 / 설장의 성은", inline=False)
    chongyunSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 얼음 2세트 + 왕실 2세트 / 얼음 4세트", inline=False)
    chongyunSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    chongyunSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    chongyunSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 얼음 원소 피해 %", inline=True)
    chongyunSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    chongyunSetEmbed.set_thumbnail(url="attachment://chongyun.png")
    await ctx.message.delete()
    await ctx.send(file=chongyunImage, embed=chongyunSetEmbed, delete_after=300.0)

@bot.command()
async def 로자리아(ctx):
    rosariaImage = discord.File(str(srcPath)+"src/system/unknown.jpg", filename="unknown.jpg")
    rosariaSetEmbed = discord.Embed(title="가시관의 은혜 · 로자리아", color=0x93050C)
    rosariaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 화박연 / 호마의 지팡이 / 천공의 마루 / 관홍의 창 / 유월창", inline=False)
    rosariaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 검투사 4세트 / 얼음 4세트 / 왕실 4세트", inline=False)
    rosariaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 / 공격력 % / 치명타 확률 % / 치명타 피해 %\n- 원소 충전 효율 % (왕실 세트 적용)", inline=False)
    rosariaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력%\n- 원소 충전 효율 %\n(왕실 세트 적용)", inline=True)
    rosariaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %\n- 얼음 원소 피해 %\n(얼음 / 왕실 적용)", inline=True)
    rosariaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    rosariaSetEmbed.set_thumbnail(url="attachment://unknown.jpg")
    await ctx.message.delete()
    await ctx.send(file=rosariaImage, embed=rosariaSetEmbed, delete_after=300.0)

@bot.command()
async def 유라(ctx):
    eulaImage = discord.File(str(srcPath)+"src/system/unknown.jpg", filename="unknown.jpg")
    eulaSetEmbed = discord.Embed(title="물보라의 선무 · 유라", color=0x8ECED4)
    eulaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 자료 없음", inline=False)
    eulaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 자료 없음", inline=False)
    eulaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 자료 없음", inline=False)
    eulaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 자료 없음", inline=True)
    eulaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 자료 없음", inline=True)
    eulaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 자료 없음", inline=True)
    eulaSetEmbed.set_thumbnail(url="attachment://unknown.jpg")
    await ctx.message.delete()
    await ctx.send(file=eulaImage, embed=eulaSetEmbed, delete_after=300.0)

@bot.command()
async def 아야카(ctx):
    ayakaImage = discord.File(str(srcPath)+"src/character/ayaka.png", filename="ayaka.png")
    ayakaSetEmbed = discord.Embed(title="이명 · 카미사토 아야카", color=0x99B5EE)
    ayakaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 자료 없음", inline=False)
    ayakaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 자료 없음", inline=False)
    ayakaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 자료 없음", inline=False)
    ayakaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 자료 없음", inline=True)
    ayakaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 자료 없음", inline=True)
    ayakaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 자료 없음", inline=True)
    ayakaSetEmbed.set_thumbnail(url="attachment://ayaka.png")
    await ctx.message.delete()
    await ctx.send(file=ayakaImage, embed=ayakaSetEmbed, delete_after=300.0)

# ====================================================================================================

@bot.command()
async def 각청(ctx):
    keqingImage = discord.File(str(srcPath)+"src/character/keqing.jpg", filename="keqing.jpg")
    keqingSetEmbed = discord.Embed(title="질뢰쾌우 · 각청", color=0xB488CB)
    keqingSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 매의 검 / 반암결록 / 칠흑검 / 용의 포효", inline=False)
    keqingSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 뇌명 4세트 / 번분 2세트 + 검투사 2세트\n- 기사 2세트 + 검투사 2세트", inline=False)
    keqingSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    keqingSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    keqingSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 번개 원소 피해 %\n- 물리 피해 보너스 %\n(기 + 검 세트 적용)", inline=True)
    keqingSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    keqingSetEmbed.set_thumbnail(url="attachment://keqing.jpg")
    await ctx.message.delete()
    await ctx.send(file=keqingImage, embed=keqingSetEmbed, delete_after=300.0)

@bot.command()
async def 피슬(ctx):
    fischlImage = discord.File(str(srcPath)+"src/character/fischl.jpg", filename="fischl.jpg")
    fischlSetEmbed = discord.Embed(title="단죄의 황녀 · 피슬", color=0xFAE8B6)
    fischlSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 날개 / 아모스의 활", inline=False)
    fischlSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 번분 4세트 / 기사도 2세트 + 검투사 2세트 (아모스의 활)", inline=False)
    fischlSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    fischlSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    fischlSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 물리 피해 보너스 %\n- 번개 원소 피해 %\n(번분 세트 적용)", inline=True)
    fischlSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    fischlSetEmbed.set_thumbnail(url="attachment://fischl.jpg")
    await ctx.message.delete()
    await ctx.send(file=fischlImage, embed=fischlSetEmbed, delete_after=300.0)

@bot.command()
async def 북두(ctx):
    beidouImage = discord.File(str(srcPath)+"src/system/unknown.jpg", filename="unknown.jpg")
    beidouSetEmbed = discord.Embed(title="무관의 용왕 · 북두", color=0xFAE8B6)
    beidouSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로 / 제례대검", inline=False)
    beidouSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 번분 2세트 + 검투사 2세트", inline=False)
    beidouSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    beidouSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    beidouSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 번개 원소 피해 %", inline=True)
    beidouSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    beidouSetEmbed.set_thumbnail(url="attachment://unknown.jpg")
    await ctx.message.delete()
    await ctx.send(file=beidouImage, embed=beidouSetEmbed, delete_after=300.0)

@bot.command()
async def 레이저(ctx):
    razorImage = discord.File(str(srcPath)+"src/system/unknown.jpg", filename="unknown.jpg")
    razorSetEmbed = discord.Embed(title="늑대소년 · 레이저", color=0xA68FCD)
    razorSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 늑대의 말로 / 천공의 긍지", inline=False)
    razorSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 검투사 4세트", inline=False)
    razorSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    razorSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    razorSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %", inline=True)
    razorSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    razorSetEmbed.set_thumbnail(url="attachment://unknown.jpg")
    await ctx.message.delete()
    await ctx.send(file=razorImage, embed=razorSetEmbed, delete_after=300.0)

@bot.command()
async def 리사(ctx):
    lisaImage = discord.File(str(srcPath)+"src/character/lisa.png", filename="lisa.png")
    lisaSetEmbed = discord.Embed(title="장미 마녀 · 리사", color=0x5339A6)
    lisaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 두루마리 / 사풍원서", inline=False)
    lisaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 번분 4세트", inline=False)
    lisaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    lisaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    lisaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 번개 원소 피해 %", inline=True)
    lisaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    lisaSetEmbed.set_thumbnail(url="attachment://lisa.png")
    await ctx.message.delete()
    await ctx.send(file=lisaImage, embed=lisaSetEmbed, delete_after=300.0)

# ====================================================================================================

@bot.command()
async def 바위행자(ctx):
    aetherImage = discord.File(str(srcPath)+"src/character/aether.jpg", filename="aether.jpg")
    aetherSetEmbed = discord.Embed(title="여행자 · 아이테르", color=0xF7F4E3)
    aetherSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 참봉의 칼날", inline=False)
    aetherSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 반암 2세트 + 검투사 2세트 / 반암 2세트 + 왕실 2세트", inline=False)
    aetherSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 / 치명타 피해", inline=False)
    aetherSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    aetherSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %\n- 바위 원소 피해 %", inline=True)
    aetherSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률\n- 치명타 피해", inline=True)
    aetherSetEmbed.set_thumbnail(url="attachment://aether.jpg")
    await ctx.message.delete()
    await ctx.send(file=aetherImage, embed=aetherSetEmbed, delete_after=300.0)

@bot.command()
async def 노엘(ctx):
    noelleImage = discord.File(str(srcPath)+"src/character/noelle.jpg", filename="noelle.jpg")
    noelleSetEmbed = discord.Embed(title="수여받지 못한 꽃 · 노엘", color=0xBFBFC0)
    noelleSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로 / 백영검 / 이무기 검", inline=False)
    noelleSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 유성 4세트", inline=False)
    noelleSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 방어력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    noelleSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 방어력 %", inline=True)
    noelleSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 방어력 %\n- 바위 원소 피해 %", inline=True)
    noelleSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    noelleSetEmbed.set_thumbnail(url="attachment://noelle.jpg")
    await ctx.message.delete()
    await ctx.send(file=noelleImage, embed=noelleSetEmbed, delete_after=300.0)

@bot.command()
async def 응광(ctx):
    ningguangImage = discord.File(str(srcPath)+"src/character/ningguang.png", filename="ningguang.png")
    ningguangSetEmbed = discord.Embed(title="엄월천권 · 응광", color=0xBFBFC0)
    ningguangSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 속세의 자물쇠 / 천공의 두루마리 / 일월의 정수 / 소심", inline=False)
    ningguangSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 반암 2세트 + 검투사 2세트", inline=False)
    ningguangSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 원소 충전 효율 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    ningguangSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    ningguangSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 바위 원소 피해 %", inline=True)
    ningguangSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    ningguangSetEmbed.set_thumbnail(url="attachment://ningguang.png")
    await ctx.message.delete()
    await ctx.send(file=ningguangImage, embed=ningguangSetEmbed, delete_after=300.0)

@bot.command()
async def 알베도(ctx):
    albedoImage = discord.File(str(srcPath)+"src/character/albedo.jpg", filename="albedo.jpg")
    albedoSetEmbed = discord.Embed(title="알베도 무기 & 성유물 세팅", color=0xE3D8BF)
    albedoSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 여명신검", inline=False)
    albedoSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 수호자 2세트 + 반암 2세트 / 반암 4세트 / 반암 2세트 + 왕실 2세트", inline=False)
    albedoSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 방어력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    albedoSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 방어력 %", inline=True)
    albedoSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 방어력 %\n- 바위 원소 피해 %", inline=True)
    albedoSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 방어력 %\n- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    albedoSetEmbed.set_thumbnail(url="attachment://albedo.jpg")
    await ctx.message.delete()
    await ctx.send(file=albedoImage, embed=albedoSetEmbed, delete_after=300.0)

@bot.command()
async def 종려(ctx):
    zhongliImage = discord.File(str(srcPath)+"src/character/zhongli.png", filename="zhongli.png")
    zhongliSetEmbed = discord.Embed(title="종려 무기 & 성유물 세팅", color=0xE3964C)
    zhongliSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 관흥의 창 / 천공의 마루 / 화박연", inline=False)
    zhongliSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 반암 2세트 + 왕실 2세트 / 반암 2세트 + 검투사 2세트", inline=False)
    zhongliSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    zhongliSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- HP %\n- 공격력 %", inline=True)
    zhongliSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n- 바위 원소 피해 %", inline=True)
    zhongliSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    zhongliSetEmbed.set_thumbnail(url="attachment://zhongli.png")
    await ctx.message.delete()
    await ctx.send(file=zhongliImage, embed=zhongliSetEmbed, delete_after=300.0)

# ====================================================================================================

@bot.command()
async def 향릉(ctx):
    xianglingImage = discord.File(str(srcPath)+"src/character/xiangling.png", filename="xiangling.png")
    xianglingSetEmbed = discord.Embed(title="만민백미 · 향릉", color=0xBF4F2D)
    xianglingSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 화박연 / 천공의 마루 / 페보니우스 장창 / 유월창", inline=False)
    xianglingSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 2세트 + 왕실 2세트 & 검투사 2세트 / 마녀 4세트", inline=False)
    xianglingSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    xianglingSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    xianglingSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 불 원소 피해 %", inline=True)
    xianglingSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    xianglingSetEmbed.set_thumbnail(url="attachment://xiangling.png")
    await ctx.message.delete()
    await ctx.send(file=xianglingImage, embed=xianglingSetEmbed, delete_after=300.0)

@bot.command()
async def 클레(ctx):
    kleeImage = discord.File(str(srcPath)+"src/character/klee.jpg", filename="klee.jpg")
    kleeSetEmbed = discord.Embed(title="도망치는 태양 · 클레", color=0xB84E44)
    kleeSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 사풍원서", inline=False)
    kleeSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트", inline=False)
    kleeSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    kleeSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    kleeSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
    kleeSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    kleeSetEmbed.set_thumbnail(url="attachment://klee.jpg")
    await ctx.message.delete()
    await ctx.send(file=kleeImage, embed=kleeSetEmbed, delete_after=300.0)

@bot.command()
async def 다이루크(ctx):
    dilucImage = discord.File(str(srcPath)+"src/character/diluc.png", filename="diluc.png")
    dilucSetEmbed = discord.Embed(title="새벽의 어둠 · 다이루크", color=0xDC545C)
    dilucSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로", inline=False)
    dilucSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트", inline=False)
    dilucSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
    dilucSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    dilucSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
    dilucSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    dilucSetEmbed.set_thumbnail(url="attachment://diluc.png")
    await ctx.message.delete()
    await ctx.send(file=dilucImage, embed=dilucSetEmbed, delete_after=300.0)

@bot.command()
async def 베넷(ctx):
    bennettImage = discord.File(str(srcPath)+"src/character/bennett.png", filename="bennett.png")
    bennettSetEmbed = discord.Embed(title="운명의 시금석 · 베넷", color=0xF1E8D4)
    bennettSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 검 / 제례검", inline=False)
    bennettSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 4세트", inline=False)
    bennettSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 % (①)", inline=False)
    bennettSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 % (①)\n- 원소 충전 효율 %", inline=True)
    bennettSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n불 원소 피해 %", inline=True)
    bennettSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치유 보너스 %\n- 치명타 확률 % (①)", inline=True)
    bennettSetEmbed.set_thumbnail(url="attachment://bennett.png")
    await ctx.message.delete()
    await ctx.send(file=bennettImage, embed=bennettSetEmbed, delete_after=300.0)

@bot.command()
async def 엠버(ctx):
    amberImage = discord.File(str(srcPath)+"src/character/amber.png", filename="amber.png")
    amberSetEmbed = discord.Embed(title="비행 챔피언 · 엠버", color=0xA21730)
    amberSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 페보니우스 활", inline=False)
    amberSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 악단 4세트", inline=False)
    amberSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
    amberSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
    amberSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
    amberSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    amberSetEmbed.set_thumbnail(url="attachment://amber.png")
    await ctx.message.delete()
    await ctx.send(file=amberImage, embed=amberSetEmbed, delete_after=300.0)

@bot.command()
async def 신염(ctx):
    xinyanImage = discord.File(str(srcPath)+"src/character/xinyan.png", filename="xinyan.png")
    xinyanSetEmbed = discord.Embed(title="폭열 멜로디 · 신염", color=0x68544A)
    xinyanSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로", inline=False)
    xinyanSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 기사도 4세트 / 기사도 2세트 + 왕실 2세트", inline=False)
    xinyanSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해", inline=False)
    xinyanSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    xinyanSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %", inline=True)
    xinyanSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    xinyanSetEmbed.set_thumbnail(url="attachment://xinyan.png")
    await ctx.message.delete()
    await ctx.send(file=xinyanImage, embed=xinyanSetEmbed, delete_after=300.0)

@bot.command()
async def 호두(ctx):
    hutaoImage = discord.File(str(srcPath)+"src/character/hutao.jpg", filename="hutao.jpg")
    hutaoSetEmbed = discord.Embed(title="눈 그친 뒤의 매화향 · 호두", color=0xECAAA7)
    hutaoSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 호마의 지팡이 / 화박연 / 흑술창", inline=False)
    hutaoSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트", inline=False)
    hutaoSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 치명타 확률 % / 치명타 피해", inline=False)
    hutaoSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- HP %", inline=True)
    hutaoSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n- 불 원소 피해 %", inline=True)
    hutaoSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    hutaoSetEmbed.set_thumbnail(url="attachment://hutao.jpg")
    await ctx.message.delete()
    await ctx.send(file=hutaoImage, embed=hutaoSetEmbed, delete_after=300.0)

@bot.command()
async def 연비(ctx):
    yanfeiImage = discord.File(str(srcPath)+"src/system/unknown.jpg", filename="unknown.jpg")
    yanfeiSetEmbed = discord.Embed(title="지명무사 · 연비", color=0xFADDD3) 
    yanfeiSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 사풍 원서 / 속세의 자물쇠 / 일월의 정수 / 인동의 열매", inline=False)
    yanfeiSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트 / 악단 4세트", inline=False)
    yanfeiSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 / 원소 마스터 / 치명타 확률 % / 치명타 피해 %", inline=False)
    yanfeiSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
    yanfeiSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
    yanfeiSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
    yanfeiSetEmbed.set_thumbnail(url="attachment://unknown.jpg")
    await ctx.message.delete()
    await ctx.send(file=yanfeiImage, embed=yanfeiSetEmbed, delete_after=300.0)



# ==========================================================================




@bot.command()
async def 검투사(ctx):
    finaleImage = discord.File(str(srcPath)+"src/artifacts/finale.png", filename="finale.png")
    finaleSetEmbed = discord.Embed(title="검투사의 피날레", color=0xFFE482)
    finaleSetEmbed.add_field(name="2세트 효과", value="공격력 +18%", inline=False)
    finaleSetEmbed.add_field(name="4세트 효과", value="해당 성유물 세트를 장착한 캐릭터가 한손검, 양손검, 장병기를 사용 시 캐릭터의 일반 공격으로 가하는 피해가 35% 증가한다.", inline=False)
    finaleSetEmbed.add_field(name="획득처", value="영역 토벌 - 바람 드래곤의 폐허로\n토벌 - 북풍의 왕랑, 울프의 영주 외 레진을 소모하는 모든 토벌", inline=False)
    finaleSetEmbed.set_thumbnail(url="attachment://finale.png")
    await ctx.message.delete()
    await ctx.send(file=finaleImage, embed=finaleSetEmbed, delete_after=300.0)

@bot.command()
async def 악단(ctx):
    troupeImage = discord.File(str(srcPath)+"src/artifacts/troupe.png", filename="troupe.png")
    troupeSetEmbed = discord.Embed(title="대지를 유랑하는 악단", color=0xFFE482)
    troupeSetEmbed.add_field(name="2세트 효과", value="원소 마스터리 +80pt", inline=False)
    troupeSetEmbed.add_field(name="4세트 효과", value="해당 성유물 세트를 장착한 캐릭터가 법구 또는 활을 사용시\n캐릭터의 강공격으로 가하는 피해가 35% 증가한다.", inline=False)
    troupeSetEmbed.add_field(name="획득처", value="영역 토벌 - 바람 드래곤의 폐허로\n토벌 - 북풍의 왕랑, 울프의 영주 외 레진을 소모하는 모든 토벌", inline=False)
    troupeSetEmbed.set_thumbnail(url="attachment://troupe.png")
    await ctx.message.delete()
    await ctx.send(file=troupeImage, embed=troupeSetEmbed, delete_after=300.0)

@bot.command()
async def 번분(ctx):
    furyImage = discord.File(str(srcPath)+"src/artifacts/fury.png", filename="fury.png")
    furySetEmbed = discord.Embed(title="번개 같은 분노", color=0xFFE482)
    furySetEmbed.add_field(name="2세트 효과", value="번개 원소 피해 +15%", inline=False)
    furySetEmbed.add_field(name="4세트 효과", value="과부하, 감전, 초전도 반응이 주는 피해가 40% 증가한다.\n원소 반응 발동 시 원소 스킬의 재사용 대기시간이 1초 줄어든다.\n해당 효과는 0.8초마다 1번 발동한다.", inline=False)
    furySetEmbed.add_field(name="획득처", value="비경 - 한 여름의 정원", inline=False)
    furySetEmbed.set_thumbnail(url="attachment://fury.png")
    await ctx.message.delete()
    await ctx.send(file=furyImage, embed=furySetEmbed, delete_after=300.0)

@bot.command()
async def 뇌명(ctx):
    thunderImage = discord.File(str(srcPath)+"src/artifacts/thunder.png", filename="thunder.png")
    thunderSetEmbed = discord.Embed(title="뇌명을 평정한 존자", color=0xFFE482)
    thunderSetEmbed.add_field(name="2세트 효과", value="번개 원소 내성 +40%", inline=False)
    thunderSetEmbed.add_field(name="4세트 효과", value="번개 원소의 영향을 받은 적에게 가하는 피해가 35% 증가한다.", inline=False)
    thunderSetEmbed.add_field(name="획득처", value="비경 - 한 여름의 정원", inline=False)
    thunderSetEmbed.set_thumbnail(url="attachment://thunder.png")
    await ctx.message.delete()
    await ctx.send(file=thunderImage, embed=thunderSetEmbed, delete_after=300.0)

@bot.command()
async def 청록(ctx):
    viridescentImage = discord.File(str(srcPath)+"src/artifacts/viridescent.png", filename="viridescent.png")
    viridescentSetEmbed = discord.Embed(title="청록색 그림자", color=0xFFE482)
    viridescentSetEmbed.add_field(name="2세트 효과", value="바람 원소 피해 +15%", inline=False)
    viridescentSetEmbed.add_field(name="4세트 효과", value="확산 반응이 가하는 피해가 60% 증가한다. 확산되는\n원소 타입에 따라 피해 범위 내 적의 해당 원소의 내성이 40% 감소한다.\n지속 시간 - 10초.", inline=False)
    viridescentSetEmbed.add_field(name="획득처", value="비경 - 각인의 골짜기", inline=False)
    viridescentSetEmbed.set_thumbnail(url="attachment://viridescent.png")
    await ctx.message.delete()
    await ctx.send(file=viridescentImage, embed=viridescentSetEmbed, delete_after=300.0)

@bot.command()
async def 소녀(ctx):
    belovedImage = discord.File(str(srcPath)+"src/artifacts/beloved.png", filename="beloved.png")
    belovedSetEmbed = discord.Embed(title="사랑받는 소녀", color=0xFFE482)
    belovedSetEmbed.add_field(name="2세트 효과", value="캐릭터가 주는 치유 효과 +15%", inline=False)
    belovedSetEmbed.add_field(name="4세트 효과", value="원소 전투 스킬 또는 원소폭발 발동 후 10초 동안\n파티 내 모든 캐릭터가 받는 치유 효과가 20% 증가한다.", inline=False)
    belovedSetEmbed.add_field(name="획득처", value="비경 - 각인의 골짜기", inline=False)
    belovedSetEmbed.set_thumbnail(url="attachment://beloved.png")
    await ctx.message.delete()
    await ctx.send(file=belovedImage, embed=belovedSetEmbed, delete_after=300.0)

@bot.command()
async def 반암(ctx):
    petraImage = discord.File(str(srcPath)+"src/artifacts/petra.png", filename="petra.png")
    petraSetEmbed = discord.Embed(title="유구한 반암", color=0xFFE482)
    petraSetEmbed.add_field(name="2세트 효과", value="바위 원소 피해 보너스를 15% 획득한다.", inline=False)
    petraSetEmbed.add_field(name="4세트 효과", value="바위 원소 반응으로 만들어진 결정을 획득 시 파티 내\n모든 캐릭터는 해당 원소 피해 보너스를 35% 획득한다. 지속 시간: 10초.\n이러한 효과로 1가지의 원소 피해 보너스만 획득할 수 있다.", inline=False)
    petraSetEmbed.add_field(name="획득처", value="비경 - 하늘을 찌르는 땅", inline=False)
    petraSetEmbed.set_thumbnail(url="attachment://petra.png")
    await ctx.message.delete()
    await ctx.send(file=petraImage, embed=petraSetEmbed, delete_after=300.0)

@bot.command()
async def 유성(ctx):
    bolideImage = discord.File(str(srcPath)+"src/artifacts/bolide.png", filename="bolide.png")
    bolideSetEmbed = discord.Embed(title="날아오르는 유성", color=0xFFE482)
    bolideSetEmbed.add_field(name="2세트 효과", value="보호막 강화 효과가 35% 상승한다.", inline=False)
    bolideSetEmbed.add_field(name="4세트 효과", value="보호막이 존재 시 추가로\n일반 공격과 강공격 보너스를 40% 획득한다.", inline=False)
    bolideSetEmbed.add_field(name="획득처", value="비경 - 하늘을 찌르는 땅", inline=False)
    bolideSetEmbed.set_thumbnail(url="attachment://bolide.png")
    await ctx.message.delete()
    await ctx.send(file=bolideImage, embed=bolideSetEmbed, delete_after=300.0)

@bot.command()
async def 마녀(ctx):
    witchImage = discord.File(str(srcPath)+"src/artifacts/witch.png", filename="witch.png")
    witchSetEmbed = discord.Embed(title="불타오르는 화염의 마녀", color=0xFFE482)
    witchSetEmbed.add_field(name="2세트 효과", value="불 원소 피해 +15%", inline=False)
    witchSetEmbed.add_field(name="4세트 효과", value="과부하, 연소 반응이 적에게 주는 피해가 40% 증가하고\n증발, 융해 반응의 보너스 계수가 15% 증가한다.\n원소 전투 스킬 발동 후 10초 동안\n2세트의 효과가 50% 증가한다. 최대 중첩수 - 3회", inline=False)
    witchSetEmbed.add_field(name="획득처", value="비경 - 무망 인구 밀궁", inline=False)
    witchSetEmbed.set_thumbnail(url="attachment://witch.png")
    await ctx.message.delete()
    await ctx.send(file=witchImage, embed=witchSetEmbed, delete_after=300.0)

@bot.command()
async def 현인(ctx):
    walkerImage = discord.File(str(srcPath)+"src/artifacts/walker.png", filename="walker.png")
    walkerSetEmbed = discord.Embed(title="불 위를 걷는 현인", color=0xFFE482)
    walkerSetEmbed.add_field(name="2세트 효과", value="불 원소 내성 +40%", inline=False)
    walkerSetEmbed.add_field(name="4세트 효과", value="불 원소의 영향을 받은 적에게 가하는 피해가 35% 증가한다.", inline=False)
    walkerSetEmbed.add_field(name="획득처", value="비경 - 무망 인구 밀궁", inline=False)
    walkerSetEmbed.set_thumbnail(url="attachment://walker.png")
    await ctx.message.delete()
    await ctx.send(file=walkerImage, embed=walkerSetEmbed, delete_after=300.0)

@bot.command()
async def 기사도(ctx):
    chivalryImage = discord.File(str(srcPath)+"src/artifacts/chivalry.png", filename="chivalry.png")
    chivalrySetEmbed = discord.Embed(title="피에 물든 기사도", color=0xFFE482)
    chivalrySetEmbed.add_field(name="2세트 효과", value="가하는 물리 피해가 25% 증가한다.", inline=False)
    chivalrySetEmbed.add_field(name="4세트 효과", value="적을 처치한 후 10초 동안 강공격 사용 시\n스태미나를 소모하지 않고 강공격으로 가하는 피해가 50% 증가한다.", inline=False)
    chivalrySetEmbed.add_field(name="획득처", value="비경 - 화지 산굴", inline=False)
    chivalrySetEmbed.set_thumbnail(url="attachment://chivalry.png")
    await ctx.message.delete()
    await ctx.send(file=chivalryImage, embed=chivalrySetEmbed, delete_after=300.0)

@bot.command()
async def 왕실(ctx):
    noblesseImage = discord.File(str(srcPath)+"src/artifacts/noblesse.png", filename="noblesse.png")
    noblesseSetEmbed = discord.Embed(title="옛 왕실의 의식", color=0xFFE482)
    noblesseSetEmbed.add_field(name="2세트 효과", value="원소폭발로 가하는 피해가 20% 증가한다.", inline=False)
    noblesseSetEmbed.add_field(name="4세트 효과", value="원소폭발 후 파티 내 모든 캐릭터의 공격력이 20% 증가한다.\n지속 시간 - 12초. 해당 효과는 중첩되지 않는다.", inline=False)
    noblesseSetEmbed.add_field(name="획득처", value="비경 - 화지 산굴", inline=False)
    noblesseSetEmbed.set_thumbnail(url="attachment://noblesse.png")
    await ctx.message.delete()
    await ctx.send(file=noblesseImage, embed=noblesseSetEmbed, delete_after=300.0)

@bot.command()
async def 얼음(ctx):
    blizzardImage = discord.File(str(srcPath)+"src/artifacts/blizzard.png", filename="blizzard.png")
    blizzardSetEmbed = discord.Embed(title="얼음바람 속에서 길잃은 용사", color=0xFFE482)
    blizzardSetEmbed.add_field(name="2세트 효과", value="얼음 원소 피해 보너스 +15%", inline=False)
    blizzardSetEmbed.add_field(name="4세트 효과", value="얼음 원소의 영향을 받은 적을 공격 시\n치명타 확률이 20% 증가한다.\n만약 적이 빙결 상태라면 치명타 확률이 추가로 20% 증가한다.", inline=False)
    blizzardSetEmbed.add_field(name="획득처", value="비경 - 빈다그니르의 정상", inline=False)
    blizzardSetEmbed.set_thumbnail(url="attachment://blizzard.png")
    await ctx.message.delete()
    await ctx.send(file=blizzardImage, embed=blizzardSetEmbed, delete_after=300.0)

@bot.command()
async def 몰락(ctx):
    depthImage = discord.File(str(srcPath)+"src/artifacts/depth.png", filename="depth.png")
    depthSetEmbed = discord.Embed(title="몰락한 마음", color=0xFFE482)
    depthSetEmbed.add_field(name="2세트 효과", value="물 원소 피해 +15%", inline=False)
    depthSetEmbed.add_field(name="4세트 효과", value="원소전투 스킬 발동 후 15초 동안\n일반 공격과 강공격으로 가하는 피해가 30% 증가한다.", inline=False)
    depthSetEmbed.add_field(name="획득처", value="비경 - 빈다그니르의 정상", inline=False)
    depthSetEmbed.set_thumbnail(url="attachment://depth.png")
    await ctx.message.delete()
    await ctx.send(file=depthImage, embed=depthSetEmbed, delete_after=300.0)





# ==========================================================================





@bot.command()
async def 매의검(ctx):
    hawkImage = discord.File(str(srcPath)+"src/weapon_sword/hawk.png", filename="hawk.png")
    hawkSetEmbed = discord.Embed(title="매의 검", color=0xFFE482)
    hawkSetEmbed.add_field(name="초기 공격력", value="48", inline=True)
    hawkSetEmbed.add_field(name="추가 능력치", value="물리 피해 보너스", inline=True)
    hawkSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    hawkSetEmbed.add_field(name="무기 스킬", value="공격력이 20/40% 증가한다.", inline=False)
    hawkSetEmbed.add_field(name="피해를 입으면 발동", value="공격력 100/160%만큼의 HP를 회복하고\n주변의 적에게 공격력 200/320%의 피해를 준다.\n해당 효과는 15초마다 1번 발동한다.", inline=False)
    hawkSetEmbed.set_thumbnail(url="attachment://hawk.png")
    await ctx.message.delete()
    await ctx.send(file=hawkImage, embed=hawkSetEmbed, delete_after=300.0)

@bot.command()
async def 천공의검(ctx):
    skywardImage = discord.File(str(srcPath)+"src/weapon_sword/skyward.png", filename="skyward.png")
    skywardSetEmbed = discord.Embed(title="천공의 검", color=0xFFE482)
    skywardSetEmbed.add_field(name="초기 공격력", value="46", inline=True)
    skywardSetEmbed.add_field(name="추가 능력치", value="원소 충전 효율", inline=True)
    skywardSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    skywardSetEmbed.add_field(name="무기 스킬", value="치명타 확률이 4/8% 증가한다.", inline=False)
    skywardSetEmbed.add_field(name="원소폭발 시 발동", value="이동속도+10%, 공격속도+10%\n일반공격과 강공격이 명중 시\n추가로 공격력 20/40%의 피해를 준다. 지속 시간 : 12초", inline=False)
    skywardSetEmbed.set_thumbnail(url="attachment://skyward.png")
    await ctx.message.delete()
    await ctx.send(file=skywardImage, embed=skywardSetEmbed, delete_after=300.0)

@bot.command()
async def 참봉의칼날(ctx):
    summitImage = discord.File(str(srcPath)+"src/weapon_sword/summit.png", filename="summit.png")
    summitSetEmbed = discord.Embed(title="참봉의 칼날", color=0xFFE482)
    summitSetEmbed.add_field(name="초기 공격력", value="46", inline=True)
    summitSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    summitSetEmbed.add_field(name="획득 경로", value="기원(기간 한정)", inline=True)
    summitSetEmbed.add_field(name="무기 스킬", value="보호막 강화 효과가 20/40% 증가한다.\n공격 명중 후 공격력이 4/8% 증가한다.\n지속 시간: 8초. 최대 중첩수: 5회. 0.3초마다 1번 발동한다.", inline=False)
    summitSetEmbed.add_field(name="보호막 존재 시 발동", value="해당 효과의 공격력 증가 효과가 100% 증가한다.", inline=False)
    summitSetEmbed.set_thumbnail(url="attachment://summit.png")
    await ctx.message.delete()
    await ctx.send(file=summitImage, embed=summitSetEmbed, delete_after=300.0)

@bot.command()
async def 피리검(ctx):
    fluteImage = discord.File(str(srcPath)+"src/weapon_sword/flute.png", filename="flute.png")
    fluteSetEmbed = discord.Embed(title="피리검", color=0xAA7DFF)
    fluteSetEmbed.add_field(name="초기 공격력", value="42", inline=True)
    fluteSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    fluteSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    fluteSetEmbed.add_field(name="무기 스킬", value="일반공격과 강공격이 명중 시 하모니를 부여한다.\n5 하모니를 얻으면 음악의 힘이 발동하고\n주변 적에게 100/200%의 피해를 준다.\n하모니는 최대 30초 동안 지속, 0.5초마다 1개를 얻을 수 있다.", inline=False)
    fluteSetEmbed.set_thumbnail(url="attachment://flute.png")
    await ctx.message.delete()
    await ctx.send(file=fluteImage, embed=fluteSetEmbed, delete_after=300.0)

@bot.command()
async def 제례검(ctx):
    sacrificialImage = discord.File(str(srcPath)+"src/weapon_sword/sacrificial.png", filename="sacrificial.png")
    sacrificialISetEmbed = discord.Embed(title="제례검", color=0xAA7DFF)
    sacrificialISetEmbed.add_field(name="초기 공격력", value="41", inline=True)
    sacrificialISetEmbed.add_field(name="추가 능력치", value="원소 충전 효율", inline=True)
    sacrificialISetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    sacrificialISetEmbed.add_field(name="무기 스킬", value="원소 전투 스킬로 피해를 줄 때 40/80%의 확률로\n해당 스킬의 재발동 대기시간이 초기화된다.\n해당 효과는 30/16초마다 1번 발동한다", inline=False)
    sacrificialISetEmbed.set_thumbnail(url="attachment://sacrificial.png")
    await ctx.message.delete()
    await ctx.send(file=sacrificialImage, embed=sacrificialISetEmbed, delete_after=300.0)

@bot.command()
async def 왕실의장검(ctx):
    royalImage = discord.File(str(srcPath)+"src/weapon_sword/royal.png", filename="royal.png")
    royalSetEmbed = discord.Embed(title="왕실의 장검", color=0xAA7DFF)
    royalSetEmbed.add_field(name="초기 공격력", value="42", inline=True)
    royalSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    royalSetEmbed.add_field(name="획득 경로", value="20년 10월\n스타라이트 교환", inline=True)
    royalSetEmbed.add_field(name="무기 스킬", value="공격으로 피해를 줄 때마다 치명타 확률이 8/16% 증가한다.\n최대 중첩수: 5회.\n공격 시 치명타가 발생하면 모든 집중 효과가 사라진다.", inline=False)
    royalSetEmbed.set_thumbnail(url="attachment://royal.png")
    await ctx.message.delete()
    await ctx.send(file=royalImage, embed=royalSetEmbed, delete_after=300.0)

@bot.command()
async def 용의포효(ctx):
    lionImage = discord.File(str(srcPath)+"src/weapon_sword/lion.png", filename="lion.png")
    lionSetEmbed = discord.Embed(title="용의 포효", color=0xAA7DFF)
    lionSetEmbed.add_field(name="초기 공격력", value="42", inline=True)
    lionSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    lionSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    lionSetEmbed.add_field(name="무기 스킬", value="불 원소 또는 번개 원소의 영향을 받은\n적에게 가하는 피해가 20/36% 증가한다.", inline=False)
    lionSetEmbed.set_thumbnail(url="attachment://lion.png")
    await ctx.message.delete()
    await ctx.send(file=lionImage, embed=lionSetEmbed, delete_after=300.0)

@bot.command()
async def 참암프로토타입(ctx):
    rancourImage = discord.File(str(srcPath)+"src/weapon_sword/rancour.png", filename="rancour.png")
    rancourSetEmbed = discord.Embed(title="참암 프로토타입", color=0xAA7DFF)
    rancourSetEmbed.add_field(name="초기 공격력", value="44", inline=True)
    rancourSetEmbed.add_field(name="추가 능력치", value="물리 피해 보너스", inline=True)
    rancourSetEmbed.add_field(name="획득 경로", value="단조", inline=True)
    rancourSetEmbed.add_field(name="무기 스킬", value="공격력과 방어력이 4/8% 증가한다.\n지속 시간: 6초. 최대 중첩수: 4회.\n해당 효과는 0.3초마다 1번 발동한다.", inline=False)
    rancourSetEmbed.set_thumbnail(url="attachment://rancour.png")
    await ctx.message.delete()
    await ctx.send(file=rancourImage, embed=rancourSetEmbed, delete_after=300.0)

@bot.command()
async def 강철벌침(ctx):
    stingImage = discord.File(str(srcPath)+"src/weapon_sword/sting.png", filename="sting.png")
    stingSetEmbed = discord.Embed(title="강철 벌침", color=0xAA7DFF)
    stingSetEmbed.add_field(name="초기 공격력", value="42", inline=True)
    stingSetEmbed.add_field(name="추가 능력치", value="원소 마스터리", inline=True)
    stingSetEmbed.add_field(name="획득 경로", value="단조", inline=True)
    stingSetEmbed.add_field(name="무기 스킬", value="원소 피해를 가한 후 6초 동안\n캐릭터가 가하는 피해가 6/12% 증가한다.\n최대 중첩수: 2회. 해당 효과는 1초마다 1번 발동한다.", inline=False)
    stingSetEmbed.set_thumbnail(url="attachment://sting.png")
    await ctx.message.delete()
    await ctx.send(file=stingImage, embed=stingSetEmbed, delete_after=300.0)

@bot.command()
async def 흑암장검(ctx):
    blackcliffImage = discord.File(str(srcPath)+"src/weapon_sword/blackcliff.png", filename="blackcliff.png")
    blackcliffSetEmbed = discord.Embed(title="흑암 장검", color=0xAA7DFF)
    blackcliffSetEmbed.add_field(name="초기 공격력", value="44", inline=True)
    blackcliffSetEmbed.add_field(name="추가 능력치", value="치명타 피해", inline=True)
    blackcliffSetEmbed.add_field(name="획득 경로", value="20년 11월\n스타라이트 교환", inline=True)
    blackcliffSetEmbed.add_field(name="무기 스킬", value="적을 처치한 후 공격력이 12/24% 증가한다.\n지속 시간: 30초. 최대 중첩수: 3회.\n중첩 1회당 지속 시간은 독립 계산한다.", inline=False)
    blackcliffSetEmbed.set_thumbnail(url="attachment://blackcliff.png")
    await ctx.message.delete()
    await ctx.send(file=blackcliffImage, embed=blackcliffSetEmbed, delete_after=300.0)

@bot.command()
async def 칠흑검(ctx):
    blackswordImage = discord.File(str(srcPath)+"src/weapon_sword/blacksword.png", filename="blacksword.png")
    blackswordSetEmbed = discord.Embed(title="칠흑검", color=0xAA7DFF)
    blackswordSetEmbed.add_field(name="초기 공격력", value="42", inline=True)
    blackswordSetEmbed.add_field(name="추가 능력치", value="치명타 확률", inline=True)
    blackswordSetEmbed.add_field(name="획득 경로", value="진주 기행", inline=True)
    blackswordSetEmbed.add_field(name="무기 스킬", value="일반 공격과 강공격으로 가하는 피해가 20/40% 증가한다.\n또한 일반 공격과 강공격이 치명타 시\n공격력의 60/100%에 해당하는 HP를 회복한다.\n해당 효과는 5초마다 1번 발동한다.", inline=False)
    blackswordSetEmbed.set_thumbnail(url="attachment://blacksword.png")
    await ctx.message.delete()
    await ctx.send(file=blackswordImage, embed=blackswordSetEmbed, delete_after=300.0)

@bot.command()
async def 강림의검(ctx):
    descensionImage = discord.File(str(srcPath)+"src/weapon_sword/decension.png", filename="decension.png")
    descensionSetEmbed = discord.Embed(title="강림의 검", color=0xAA7DFF)
    descensionSetEmbed.add_field(name="초기 공격력", value="39", inline=True)
    descensionSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    descensionSetEmbed.add_field(name="획득 경로", value="PS4\n기본 지급", inline=True)
    descensionSetEmbed.add_field(name="무기 스킬", value="일반 공격과 강공격 명중 후\n50%의 확률로 작은 범위에 공격력 200%의 피해를 준다.\n해당 효과는 10초마다 1회 발동한다.\n또한 여행자가 강림의 검을 장비시 공격력이 66pt 증가한다", inline=False)
    descensionSetEmbed.set_thumbnail(url="attachment://decension.png")
    await ctx.message.delete()
    await ctx.send(file=descensionImage, embed=descensionSetEmbed, delete_after=300.0)

@bot.command()
async def 부식의검(ctx):
    desireImage = discord.File(str(srcPath)+"src/weapon_sword/desire.png", filename="desire.png")
    desireSetEmbed = discord.Embed(title="부식의 검", color=0xAA7DFF)
    desireSetEmbed.add_field(name="초기 공격력", value="42", inline=True)
    desireSetEmbed.add_field(name="추가 능력치", value="원소 충전 효율", inline=True)
    desireSetEmbed.add_field(name="획득 경로", value="백악과 흑룡\n이벤트 참여", inline=True)
    desireSetEmbed.add_field(name="무기 스킬", value="원소전투 스킬로 가하는 피해가 16/32% 증가하고\n원소전투 스킬의 치명타 확률이 6/12% 증가한다", inline=False)
    desireSetEmbed.set_thumbnail(url="attachment://desire.png")
    await ctx.message.delete()
    await ctx.send(file=desireImage, embed=desireSetEmbed, delete_after=300.0)

@bot.command()
async def 뒷골목의섬광(ctx):
    alleyImage = discord.File(str(srcPath)+"src/weapon_sword/alley.png", filename="alley.png")
    alleySetEmbed = discord.Embed(title="뒷골목의 섬광", color=0xAA7DFF)
    alleySetEmbed.add_field(name="초기 공격력", value="45", inline=True)
    alleySetEmbed.add_field(name="추가 능력치", value="원소 마스터리", inline=True)
    alleySetEmbed.add_field(name="획득 경로", value="기원\n(기간 한정)", inline=True)
    alleySetEmbed.add_field(name="무기 스킬", value="캐릭터가 가하는 피해가 12/24% 증가한다.\n피해를 받은 후, 피해 증가 효과는 5초 뒤 사라진다.", inline=False)
    alleySetEmbed.set_thumbnail(url="attachment://alley.png")
    await ctx.message.delete()
    await ctx.send(file=alleyImage, embed=alleySetEmbed, delete_after=300.0)

@bot.command()
async def 차가운칼날(ctx):
    coolsteelImage = discord.File(str(srcPath)+"src/weapon_sword/coolsteel.png", filename="coolsteel.png")
    coolsteelSetEmbed = discord.Embed(title="차가운 칼날", color=0x7DBAFF)
    coolsteelSetEmbed.add_field(name="초기 공격력", value="39", inline=True)
    coolsteelSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    coolsteelSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    coolsteelSetEmbed.add_field(name="무기 스킬", value="물 원소 또는 얼음 원소의 영향을 받은\n적에게 가하는 피해가 12/24% 증가한다.", inline=False)
    coolsteelSetEmbed.set_thumbnail(url="attachment://coolsteel.png")
    await ctx.message.delete()
    await ctx.send(file=coolsteelImage, embed=coolsteelSetEmbed, delete_after=300.0)

@bot.command()
async def 여명신검(ctx):
    harbingerImage = discord.File(str(srcPath)+"src/weapon_sword/harbinger.png", filename="harbinger.png")
    harbingerSetEmbed = discord.Embed(title="여명신검", color=0x7DBAFF)
    harbingerSetEmbed.add_field(name="초기 공격력", value="39", inline=True)
    harbingerSetEmbed.add_field(name="추가 능력치", value="치명타 피해", inline=True)
    harbingerSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    harbingerSetEmbed.add_field(name="무기 스킬", value="HP가 90% 초과 시 치명타 확률이 14/28%증가한다.", inline=False)
    harbingerSetEmbed.set_thumbnail(url="attachment://harbinger.png")
    await ctx.message.delete()
    await ctx.send(file=harbingerImage, embed=harbingerSetEmbed, delete_after=300.0)

@bot.command()
async def 여행자의검(ctx):
    travelerswordImage = discord.File(str(srcPath)+"src/weapon_sword/travelersword.png", filename="travelersword.png")
    travelerswordSetEmbed = discord.Embed(title="여행자의 검", color=0x7DBAFF)
    travelerswordSetEmbed.add_field(name="초기 공격력", value="40", inline=True)
    travelerswordSetEmbed.add_field(name="추가 능력치", value="방어력", inline=True)
    travelerswordSetEmbed.add_field(name="획득 경로", value="상자", inline=True)
    travelerswordSetEmbed.add_field(name="무기 스킬", value="원소 구슬 또는 원소 입자를 획득 시 HP를 1/2% 회복한다.", inline=False)
    travelerswordSetEmbed.set_thumbnail(url="attachment://travelersword.png")
    await ctx.message.delete()
    await ctx.send(file=travelerswordImage, embed=travelerswordSetEmbed, delete_after=300.0)

@bot.command()
async def 홀호생선회칼(ctx):
    filletImage = discord.File(str(srcPath)+"src/weapon_sword/fillet.png", filename="fillet.png")
    filletSetEmbed = discord.Embed(title="홀호 생선회칼", color=0x7DBAFF)
    filletSetEmbed.add_field(name="초기 공격력", value="39", inline=True)
    filletSetEmbed.add_field(name="추가 능력치", value="공격력", inline=True)
    filletSetEmbed.add_field(name="획득 경로", value="리월 상자", inline=True)
    filletSetEmbed.add_field(name="무기 스킬", value="공격 명중 시 50%의 확률로\n단일 타킷에게 공격력 240/400%의 피해를 준다.\n해당 효과는 15/11초마다 1번 발동한다.", inline=False)
    filletSetEmbed.set_thumbnail(url="attachment://fillet.png")
    await ctx.message.delete()
    await ctx.send(file=filletImage, embed=filletSetEmbed, delete_after=300.0)

@bot.command()
async def 비천어검(ctx):
    skyriderImage = discord.File(str(srcPath)+"src/weapon_sword/skyrider.png", filename="skyrider.png")
    skyriderSetEmbed = discord.Embed(title="비천어검", color=0x7DBAFF)
    skyriderSetEmbed.add_field(name="초기 공격력", value="38", inline=True)
    skyriderSetEmbed.add_field(name="추가 능력치", value="원소 충전 효율", inline=True)
    skyriderSetEmbed.add_field(name="획득 경로", value="기원", inline=True)
    skyriderSetEmbed.add_field(name="무기 스킬", value="원소폭발 발동 후 공격력과 이동속도가 12/24% 증가한다.", inline=False)
    skyriderSetEmbed.set_thumbnail(url="attachment://skyrider.png")
    await ctx.message.delete()
    await ctx.send(file=skyriderImage, embed=skyriderSetEmbed, delete_after=300.0)

@bot.command()
async def 암철검(ctx):
    ironswordImage = discord.File(str(srcPath)+"src/weapon_sword/ironsword.png", filename="ironsword.png")
    ironswordSetEmbed = discord.Embed(title="암철검", color=0x7DBAFF)
    ironswordSetEmbed.add_field(name="초기 공격력", value="39", inline=True)
    ironswordSetEmbed.add_field(name="추가 능력치", value="원소 마스터리", inline=True)
    ironswordSetEmbed.add_field(name="획득 경로", value="쾌도진", inline=True)
    ironswordSetEmbed.add_field(name="무기 스킬", value="과부하, 초전도, 감전, 번개 원소 확산 반응 후\n12초동안 공격력이 20/40%증가한다.", inline=False)
    ironswordSetEmbed.set_thumbnail(url="attachment://ironsword.png")
    await ctx.message.delete()
    await ctx.send(file=ironswordImage, embed=ironswordSetEmbed, delete_after=300.0)

@bot.command()
async def 실버소드(ctx):
    silverswordImage = discord.File(str(srcPath)+"src/weapon_sword/silversword.png", filename="silversword.png")
    silverswordSetEmbed = discord.Embed(title="실버 소드", color=0xA0FF7D)
    silverswordSetEmbed.add_field(name="초기 공격력", value="33", inline=True)
    silverswordSetEmbed.add_field(name="획득 경로", value="상자", inline=True)
    silverswordSetEmbed.set_thumbnail(url="attachment://silversword.png")
    await ctx.message.delete()
    await ctx.send(file=silverswordImage, embed=silverswordSetEmbed, delete_after=300.0)

@bot.command()
async def 무인검(ctx):
    dullbladeImage = discord.File(str(srcPath)+"src/weapon_sword/dullblade.png", filename="dullblade.png")
    dullbladeSetEmbed = discord.Embed(title="무인검", color=0xC2C2C2)
    dullbladeSetEmbed.add_field(name="초기 공격력", value="23", inline=True)
    dullbladeSetEmbed.add_field(name="획득 경로", value="상자", inline=True)
    dullbladeSetEmbed.set_thumbnail(url="attachment://dullblade.png")
    await ctx.message.delete()
    await ctx.send(file=dullbladeImage, embed=dullbladeSetEmbed, delete_after=300.0)


# ==========================================================================


@bot.command()
async def 통통연꽃(ctx):
    if ctx.author.id in availableMember :
        tongtongImage = discord.File(str(srcPath)+"src/map/tongtong.png", filename="tongtong.png")
        tongtongSetEmbed = discord.Embed(title="몬드 지역 특산물 · 통통 연꽃", color=0xC2C2C2)
        tongtongSetEmbed.set_author(name="▷ 성유물 위치 보러가기", url="https://genshin-impact-map.appsample.com/#/")
        tongtongSetEmbed.add_field(name="🎑 │ 획득 경로", value="- 호수 물가 채집", inline=True)
        tongtongSetEmbed.add_field(name="👤 │ 사용 캐릭터", value="- 케이아 / 디오나", inline=True)
        tongtongSetEmbed.add_field(name="🍱 │ 사용 레시피", value="- 통통 연꽃 해산물 수프", inline=True)
        tongtongSetEmbed.set_thumbnail(url="attachment://tongtong.png")
        await ctx.message.delete()
        await ctx.send(file=tongtongImage, embed=tongtongSetEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)

@bot.command()
async def 고리고리(ctx):
    if ctx.author.id in availableMember :
        gorigoriImage = discord.File(str(srcPath)+"src/map/gorigori.png", filename="gorigori.png")
        gorigoriSetEmbed = discord.Embed(title="몬드 지역 특산물 · 고리고리 열매", color=0xC2C2C2)
        gorigoriSetEmbed.set_author(name="▷ 성유물 위치 보러가기", url="https://genshin-impact-map.appsample.com/#/")
        gorigoriSetEmbed.add_field(name="🎑 │ 획득 경로", value="- 야외 채집", inline=True)
        gorigoriSetEmbed.add_field(name="👤 │ 사용 캐릭터", value="- 레이저", inline=True)
        gorigoriSetEmbed.set_thumbnail(url="attachment://gorigori.png")
        await ctx.message.delete()
        await ctx.send(file=gorigoriImage, embed=gorigoriSetEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)

@bot.command()
async def 낙락베리(ctx):
    if ctx.author.id in availableMember :
        nakrakImage = discord.File(str(srcPath)+"src/map/nakrak.png", filename="nakrak.png")
        nakrakSetEmbed = discord.Embed(title="몬드 지역 특산물 · 낙락베리", color=0xC2C2C2)
        nakrakSetEmbed.set_author(name="▷ 성유물 위치 보러가기", url="https://genshin-impact-map.appsample.com/#/")
        nakrakSetEmbed.add_field(name="🎑 │ 획득 경로", value="- 야외 채집", inline=True)
        nakrakSetEmbed.add_field(name="👤 │ 사용 캐릭터", value="- 리사 / 노엘", inline=True)
        nakrakSetEmbed.set_thumbnail(url="attachment://nakrak.png")
        await ctx.message.delete()
        await ctx.send(file=nakrakImage, embed=nakrakSetEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)

@bot.command()
async def 세실리아(ctx):
    if ctx.author.id in availableMember :
        sesilliaImage = discord.File(str(srcPath)+"src/map/sesillia.png", filename="sesillia.png")
        sesilliaSetEmbed = discord.Embed(title="몬드 지역 특산물 · 세실리아꽃", color=0xC2C2C2)
        sesilliaSetEmbed.set_author(name="▷ 성유물 위치 보러가기", url="https://genshin-impact-map.appsample.com/#/")
        sesilliaSetEmbed.add_field(name="🎑 │ 획득 경로", value="- 야외 채집", inline=True)
        sesilliaSetEmbed.add_field(name="👤 │ 사용 캐릭터", value="- 벤티 / 알베도", inline=True)
        sesilliaSetEmbed.set_thumbnail(url="attachment://sesillia.png")
        await ctx.message.delete()
        await ctx.send(file=sesilliaImage, embed=sesilliaSetEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)

@bot.command()
async def 풍차국화(ctx):
    if ctx.author.id in availableMember :
        pungchaImage = discord.File(str(srcPath)+"src/map/pungcha.png", filename="pungcha.png")
        pungchaSetEmbed = discord.Embed(title="몬드 지역 특산물 · 풍차 국화", color=0xC2C2C2)
        pungchaSetEmbed.set_author(name="▷ 성유물 위치 보러가기", url="https://genshin-impact-map.appsample.com/#/")
        pungchaSetEmbed.add_field(name="🎑 │ 획득 경로", value="- 바람이 시작하는 곳\n- 야외 나무 및 채집", inline=True)
        pungchaSetEmbed.add_field(name="👤 │ 사용 캐릭터", value="- 여행자 / 베넷\n- 설탕", inline=True)
        pungchaSetEmbed.add_field(name="🍱 │ 사용 레시피", value="- 바람 잡는 병", inline=True)
        pungchaSetEmbed.set_thumbnail(url="attachment://pungcha.png")
        await ctx.message.delete()
        await ctx.send(file=pungchaImage, embed=pungchaSetEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)

@bot.command()
async def 바람버섯(ctx):
    if ctx.author.id in availableMember :
        windmushroomImage = discord.File(str(srcPath)+"src/map/windmushroom.png", filename="windmushroom.png")
        windmushroomSetEmbed = discord.Embed(title="몬드 지역 특산물 · 바람버섯", color=0xC2C2C2)
        windmushroomSetEmbed.set_author(name="▷ 성유물 위치 보러가기", url="https://genshin-impact-map.appsample.com/#/")
        windmushroomSetEmbed.add_field(name="🎑 │ 획득 경로", value="- 지붕 및 채집", inline=True)
        windmushroomSetEmbed.add_field(name="👤 │ 사용 캐릭터", value="- 클레 / 바바라\n- 모나", inline=True)
        windmushroomSetEmbed.add_field(name="🍱 │ 사용 레시피", value="- 바람의 보물찾기 나침반", inline=True)
        windmushroomSetEmbed.set_thumbnail(url="attachment://windmushroom.png")
        await ctx.message.delete()
        await ctx.send(file=windmushroomImage, embed=windmushroomSetEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)


@bot.command()
async def 파밍(ctx):
    if ctx.author.id in availableMember :
        todayWeek = datetime.datetime.today().weekday()
        if todayWeek == 0 : # 월요일
            todayWeekEmbed = discord.Embed(title="오늘은 월요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n고탑 왕 시리즈 / 고운한림 시리즈 / 자유 시리즈 / 번영 시리즈\n\n**- 육성 가능 캐릭터**\n바바라 / 디오나 / 엠버 / 타르탈리아 / 클레 / 설탕 / 응광 / 소 / 각청 / 치치")

        elif todayWeek == 1 : # 화요일
            todayWeekEmbed = discord.Embed(title="오늘은 화요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n칼바람 울프 시리즈 / 안개구름 속 시리즈 / 투쟁 시리즈 / 근면 시리즈\n\n**- 육성 가능 캐릭터**\n노엘 / 베넷 / 레이저 / 모나 / 다이루크 / 진 / 향릉 / 증운 / 감우 / 호두")

        elif todayWeek == 2 :  # 수요일
            todayWeekEmbed = discord.Embed(title="오늘은 수요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n라이언 투사 시리즈 / 흑운철 시리즈 / 시문 시리즈 / 황금 시리즈\n\n**- 육성 가능 캐릭터**\n벤티 / 알베도 / 케이아 / 리사 / 피슬 / 북두 / 행추 / 신염 / 종려")

        elif todayWeek == 3 : # 목요일
            todayWeekEmbed = discord.Embed(title="오늘은 목요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n고탑 왕 시리즈 / 고운한림 시리즈 / 자유 시리즈 / 번영 시리즈\n\n**- 육성 가능 캐릭터**\n바바라 / 디오나 / 엠버 / 타르탈리아 / 클레 / 설탕 / 응광 / 소 / 각청 / 치치")

        elif todayWeek == 4 : # 금요일
            todayWeekEmbed = discord.Embed(title="오늘은 금요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n칼바람 울프 시리즈 / 안개구름 속 시리즈 / 투쟁 시리즈 / 근면 시리즈\n\n**- 육성 가능 캐릭터**\n노엘 / 베넷 / 레이저 / 모나 / 다이루크 / 진 / 향릉 / 증운 / 감우 / 호두")
            
        elif todayWeek == 5 :  # 토요일
            todayWeekEmbed = discord.Embed(title="오늘은 토요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n라이언 투사 시리즈 / 흑운철 시리즈 / 시문 시리즈 / 황금 시리즈\n\n**- 육성 가능 캐릭터**\n벤티 / 알베도 / 케이아 / 리사 / 피슬 / 북두 / 행추 / 신염 / 종려")

        elif todayWeek == 6 :  # 일요일
            todayWeekEmbed = discord.Embed(title="오늘은 일요일 !", color=0xFFB3C2, description="**- 드롭 가능 아이템**\n제한 없음 !\n\n**- 육성 가능 캐릭터**\n제한 없음 !")
        
        await ctx.message.delete()
        await ctx.send(embed=todayWeekEmbed, delete_after=300.0)

    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)



# ==========================================================================

@bot.command()
async def 리딤(ctx):
    if ctx.author.id in availableMember :
        redeemImage = discord.File(str(srcPath)+"src/system/event3.jpg", filename="event3.jpg")
        redeemSetEmbed = discord.Embed(title="사용 가능한 리딤코드 (21년 3월 28일 기준)", color=0xFFB3C2)
        redeemSetEmbed.add_field(name="원석 50개", value="genshingift", inline=True)
        redeemSetEmbed.add_field(name="원석 30개", value="SBNBUK67M37Z", inline=True)
        redeemSetEmbed.add_field(name="원석 60개", value="GS6ACJ775KNV", inline=True)
        redeemSetEmbed.add_field(name="원석 60개", value="TT7BVJNPL249", inline=True)
        redeemSetEmbed.set_thumbnail(url="attachment://event3.jpg")
        await ctx.message.delete()
        await ctx.send(file=redeemImage, embed=redeemSetEmbed, delete_after=300.0)
    else :
        NotAvailableSetEmbed = discord.Embed(title="이용 불가", color=0xC2C2C2, description="서버 부스터 / 후원 사용자가 아니라서 이용 할 수 없어요.")
        await ctx.message.delete()
        await ctx.send(embed=NotAvailableSetEmbed, delete_after=10.0)

@bot.command()
async def dailyCheckAlarm():
    await bot.wait_until_ready()
    channel = bot.get_channel(821045712069722142)
    while not bot.is_closed():
        currentHour = int(datetime.datetime.now().time().strftime("%H"))
        if currentHour == 16 :
            eventImage = discord.File(str(srcPath)+"src/system/event.jpg", filename="event.jpg")
            dailyCheckAlarmEmbed1 = discord.Embed(title="일일 출석체크 알림", color=0xFFB3C2, description="벌써 다음날이 되었어요! 잊지 말고 꼭 출석해 주세요!\n\n[출석하러 가기](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ko-kr)")
            dailyCheckAlarmEmbed1.set_thumbnail(url="attachment://event.jpg")
            await channel.send(file=eventImage, embed=dailyCheckAlarmEmbed1, delete_after=86400.0)
            await asyncio.sleep(86400)

        await asyncio.sleep(600)

bot.loop.create_task(dailyCheckAlarm())


# ==========================================================================


bot.run(token)
