import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import datetime
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

srcPath = (__file__)
srcPath = srcPath.replace("\\", "/")
srcPath = srcPath.replace("HuTaoBot_Current.py", "")

token = ''

# ====================================================================================================

@bot.event
async def on_ready():
    print("HuTaoBot - Login\n=====================")
    print("Src Path : "+ srcPath)
    print("Current Time : "+ str(datetime.datetime.now().time()) + " / Server Time : KST. - 9 Hours")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("모든 명령어는 슬래시로 이전 !"))

# ====================================================================================================

@slash.slash(name="캐릭터",
             description="해당 캐릭터의 추천 세팅을 보여줍니다.",
             options=[create_option(name="이름", description="해당하는 캐릭터의 추천 세팅을 보여줍니다.", option_type=3, required=True)])

async def 이름(ctx, 이름: str) :
    if 이름 == "루미네" :
        lumineImage = discord.File(str(srcPath)+"src/character/lumine.jpg", filename="lumine.jpg")
        lumineSetEmbed = discord.Embed(title="여행자 · 루미네", color=0xF7F4E3)
        lumineSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 매의 검 / 천공의 검 / 반암결록 / 부식의 검 / 칠흑검", inline=False)
        lumineSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 2세트 + 검투사 2세트 / 청록 4세트", inline=False)
        lumineSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        lumineSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        lumineSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %\n- 바람 원소 피해 %", inline=True)
        lumineSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %\n", inline=True)
        lumineSetEmbed.set_thumbnail(url="attachment://lumine.jpg")
        await ctx.send(file=lumineImage, embed=lumineSetEmbed, delete_after=300.0)

    elif 이름 == "설탕" :
        sucroseImage = discord.File(str(srcPath)+"src/character/sucrose.png", filename="sucrose.png")
        sucroseSetEmbed = discord.Embed(title="무해한 달콤함 · 설탕", color=0xCEE7CA)
        sucroseSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 만국 항해용해도 / 페보니우스 비전 / 드래곤 슬래이어 영웅담", inline=False)
        sucroseSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 4세트 / 유배자 4세트", inline=False)
        sucroseSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 원소 마스터리 / 원소 충전 효율 %", inline=False)
        sucroseSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 마스터리\n- 원소 충전 효율 %", inline=True)
        sucroseSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 원소 마스터리", inline=True)
        sucroseSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 원소 마스터리", inline=True)
        sucroseSetEmbed.set_thumbnail(url="attachment://sucrose.png")
        await ctx.send(file=sucroseImage, embed=sucroseSetEmbed, delete_after=300.0)

    elif 이름 == "진" :
        jeanImage = discord.File(str(srcPath)+"src/character/jean.jpg", filename="jean.jpg")
        jeanSetEmbed = discord.Embed(title="민들레 기사 · 진", color=0xFFDCA3)
        jeanSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 검 / 매의 검 / 참봉의 칼날 / 페보니우스 검 / 부식의 검", inline=False)
        jeanSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 2세트 + 검투사 2세트 / 청록 4세트", inline=False)
        jeanSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        jeanSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        jeanSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 바람 원소 피해 %", inline=True)
        jeanSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 원소 마스터리", inline=True)
        jeanSetEmbed.set_thumbnail(url="attachment://jean.jpg")
        await ctx.send(file=jeanImage, embed=jeanSetEmbed, delete_after=300.0)

    elif 이름 == "소" :
        xiaoImage = discord.File(str(srcPath)+"src/character/xiao.jpg", filename="xiao.jpg")
        xiaoSetEmbed = discord.Embed(title="호법야차 · 소", color=0x60BFAA)
        xiaoSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 화박연 / 관홍의 창 / 호마의 지팡이 / 결투의 창 / 흑암창", inline=False)
        xiaoSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 2세트 + 검투사 2세트", inline=False)
        xiaoSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        xiaoSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        xiaoSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 바람 원소 피해 %", inline=True)
        xiaoSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        xiaoSetEmbed.set_thumbnail(url="attachment://xiao.jpg")
        await ctx.send(file=xiaoImage, embed=xiaoSetEmbed, delete_after=300.0)

    elif 이름 == "벤티" :
        ventiImage = discord.File(str(srcPath)+"src/character/venti.jpg", filename="venti.jpg")
        ventiSetEmbed = discord.Embed(title="바람의 시인 · 벤티", color=0x9BC5A1)
        ventiSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 종말 탄식의 노래 / 천공의 날개 / 절현 / 페보니우스 활", inline=False)
        ventiSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 청록 4세트", inline=False)
        ventiSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        ventiSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 충전 효율 %", inline=True)
        ventiSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 바람 원소 피해 %", inline=True)
        ventiSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        ventiSetEmbed.set_thumbnail(url="attachment://venti.jpg")
        await ctx.send(file=ventiImage, embed=ventiSetEmbed, delete_after=300.0)

    elif 이름 == "타르탈리아" :
        tartagliaImage = discord.File(str(srcPath)+"src/character/tartaglia.png", filename="tartaglia.png")
        tartagliaSetEmbed = discord.Embed(title="귀공자 · 타르탈리아", color=0xC98443)
        tartagliaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 날개 / 청록의 사냥활", inline=False)
        tartagliaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 몰락 2세트 + 왕실 2세트 / 몰락 4세트", inline=False)
        tartagliaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        tartagliaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        tartagliaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물 원소 피해 %", inline=True)
        tartagliaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        tartagliaSetEmbed.set_thumbnail(url="attachment://tartaglia.png")
        await ctx.send(file=tartagliaImage, embed=tartagliaSetEmbed, delete_after=300.0)

    elif 이름 == "모나" :
        monaImage = discord.File(str(srcPath)+"src/character/mona.jpg", filename="mona.jpg")
        monaSetEmbed = discord.Embed(title="별하늘의 물거울 · 모나", color=0x6670B8)
        monaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 음유시인의 악장", inline=False)
        monaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 4세트", inline=False)
        monaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        monaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        monaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물 원소 피해 %", inline=True)
        monaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        monaSetEmbed.set_thumbnail(url="attachment://mona.jpg")
        await ctx.send(file=monaImage, embed=monaSetEmbed, delete_after=300.0)

    elif 이름 == "바바라" :
        barbaraImage = discord.File(str(srcPath)+"src/character/barbara.jpg", filename="barbara.jpg")
        barbaraSetEmbed = discord.Embed(title="빛나는 아이돌 · 바바라", color=0xD7CDB6)
        barbaraSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 드래곤 슬레이어 영웅담", inline=False)
        barbaraSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 소녀 4세트 / 유배자 4세트", inline=False)
        barbaraSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 원소 충전 효율 %", inline=False)
        barbaraSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 충전 효율 %", inline=True)
        barbaraSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %", inline=True)
        barbaraSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- HP %\n- 치유 보너스 %", inline=True)
        barbaraSetEmbed.set_thumbnail(url="attachment://barbara.jpg")
        await ctx.send(file=barbaraImage, embed=barbaraSetEmbed, delete_after=300.0)

    elif 이름 == "행추" :
        xingqiuImage = discord.File(str(srcPath)+"src/character/xingqiu.png", filename="xingqiu.png")
        xingqiuSetEmbed = discord.Embed(title="의기충천 · 행추", color=0x3F6F8A)
        xingqiuSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 검 / 제례검", inline=False)
        xingqiuSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 2세트 + 몰락 2세트 / 왕실 4세트", inline=False)
        xingqiuSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        xingqiuSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        xingqiuSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물 원소 피해 %", inline=True)
        xingqiuSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        xingqiuSetEmbed.set_thumbnail(url="attachment://xingqiu.png")
        await ctx.send(file=xingqiuImage, embed=xingqiuSetEmbed, delete_after=300.0)

    elif 이름 == "치치" :
        qiqiImage = discord.File(str(srcPath)+"src/character/qiqi.jpg", filename="qiqi.jpg")
        qiqiSetEmbed = discord.Embed(title="차가운 환혼의 밤 · 치치", color=0x99B5EE)
        qiqiSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 제례검", inline=False)
        qiqiSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 소녀 4세트", inline=False)
        qiqiSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 원소 충전 효율 %", inline=False)
        qiqiSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        qiqiSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        qiqiSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치유 보너스 %", inline=True)
        qiqiSetEmbed.set_thumbnail(url="attachment://qiqi.jpg")
        await ctx.send(file=qiqiImage, embed=qiqiSetEmbed, delete_after=300.0)

    elif 이름 == "케이아" :
        kaeyaImage = discord.File(str(srcPath)+"src/character/kaeya.png", filename="kaeya.png")
        kaeyaSetEmbed = discord.Embed(title="한풍의 검사 · 케이아", color=0x5782A8)
        kaeyaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 매의 검 / 천공의 검 / 페보니우스 검 / 부식의 검", inline=False)
        kaeyaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 얼음 2세트 + 왕실 2세트", inline=False)
        kaeyaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        kaeyaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        kaeyaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 얼음 원소 피해 %", inline=True)
        kaeyaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %", inline=True)
        kaeyaSetEmbed.set_thumbnail(url="attachment://kaeya.png")
        await ctx.send(file=kaeyaImage, embed=kaeyaSetEmbed, delete_after=300.0)

    elif 이름 == "감우" :
        ganyuImage = discord.File(str(srcPath)+"src/character/ganyu.jpg", filename="ganyu.jpg")
        ganyuSetEmbed = discord.Embed(title="리월의 수호자 · 감우", color=0x77BCFF)
        ganyuSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 아모스의 활 / 천공의 날개 / 청록의 사냥활", inline=False)
        ganyuSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 얼음 4세트 / 얼음 2세트 + 검투사 2세트 / 악단 4세트", inline=False)
        ganyuSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 공격력 % / 원소 충전 효율 %", inline=False)
        ganyuSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        ganyuSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 얼음 원소 피해 %", inline=True)
        ganyuSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %\n(악단세트 적용)", inline=True)
        ganyuSetEmbed.set_thumbnail(url="attachment://ganyu.jpg")
        await ctx.send(file=ganyuImage, embed=ganyuSetEmbed, delete_after=300.0)

    elif 이름 == "디오나" :
        dionaImage = discord.File(str(srcPath)+"src/character/diona.png", filename="diona.png")
        dionaSetEmbed = discord.Embed(title="캐츠라인 칵테일 · 디오나", color=0xFEAB9D)
        dionaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 제례활", inline=False)
        dionaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 4세트 / 소녀 4세트", inline=False)
        dionaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 원소 충전 효율 %", inline=False)
        dionaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 원소 충전 효율 %", inline=True)
        dionaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n- 원소 충전 효율 %", inline=True)
        dionaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- HP %", inline=True)
        dionaSetEmbed.set_thumbnail(url="attachment://diona.png")
        await ctx.send(file=dionaImage, embed=dionaSetEmbed, delete_after=300.0)

    elif 이름 == "중운" :
        chongyunImage = discord.File(str(srcPath)+"src/character/chongyun.png", filename="chongyun.png")
        chongyunSetEmbed = discord.Embed(title="얼어붙은 정열 · 중운", color=0x99B5EE)
        chongyunSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 늑대의 말로 / 천공의 긍지 / 제례 대검 / 설장의 성은", inline=False)
        chongyunSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 얼음 2세트 + 왕실 2세트 / 얼음 4세트", inline=False)
        chongyunSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        chongyunSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        chongyunSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 얼음 원소 피해 %", inline=True)
        chongyunSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        chongyunSetEmbed.set_thumbnail(url="attachment://chongyun.png")
        await ctx.send(file=chongyunImage, embed=chongyunSetEmbed, delete_after=300.0)

    elif 이름 == "로자리아" :
        rosariaImage = discord.File(str(srcPath)+"src/character/rosaria.png", filename="rosaria.png")
        rosariaSetEmbed = discord.Embed(title="가시관의 은혜 · 로자리아", color=0x93050C)
        rosariaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 화박연 / 호마의 지팡이 / 천공의 마루 / 관홍의 창 / 유월창", inline=False)
        rosariaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 검투사 4세트 / 얼음 4세트 / 왕실 4세트", inline=False)
        rosariaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 / 공격력 % / 치명타 확률 % / 치명타 피해 %\n- 원소 충전 효율 % (왕실 세트 적용)", inline=False)
        rosariaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력%\n- 원소 충전 효율 %\n(왕실 세트 적용)", inline=True)
        rosariaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %\n- 얼음 원소 피해 %\n(얼음 / 왕실 적용)", inline=True)
        rosariaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        rosariaSetEmbed.set_thumbnail(url="attachment://rosaria.png")
        await ctx.send(file=rosariaImage, embed=rosariaSetEmbed, delete_after=300.0)

    elif 이름 == "유라" :
        eulaImage = discord.File(str(srcPath)+"src/character/eula.jpg", filename="eula.jpg")
        eulaSetEmbed = discord.Embed(title="물보라의 선무 · 유라", color=0x8ECED4)
        eulaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 자료 없음", inline=False)
        eulaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 자료 없음", inline=False)
        eulaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 자료 없음", inline=False)
        eulaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 자료 없음", inline=True)
        eulaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 자료 없음", inline=True)
        eulaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 자료 없음", inline=True)
        eulaSetEmbed.set_thumbnail(url="attachment://eula.jpg")
        await ctx.send(file=eulaImage, embed=eulaSetEmbed, delete_after=300.0)

    elif 이름 == "아야카" :
        ayakaImage = discord.File(str(srcPath)+"src/character/ayaka.png", filename="ayaka.png")
        ayakaSetEmbed = discord.Embed(title="이명 · 카미사토 아야카", color=0x99B5EE)
        ayakaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 자료 없음", inline=False)
        ayakaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 자료 없음", inline=False)
        ayakaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 자료 없음", inline=False)
        ayakaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 자료 없음", inline=True)
        ayakaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 자료 없음", inline=True)
        ayakaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 자료 없음", inline=True)
        ayakaSetEmbed.set_thumbnail(url="attachment://ayaka.png")
        await ctx.send(file=ayakaImage, embed=ayakaSetEmbed, delete_after=300.0)

    elif 이름 == "각청" :
        keqingImage = discord.File(str(srcPath)+"src/character/keqing.jpg", filename="keqing.jpg")
        keqingSetEmbed = discord.Embed(title="질뢰쾌우 · 각청", color=0xB488CB)
        keqingSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 매의 검 / 반암결록 / 칠흑검 / 용의 포효", inline=False)
        keqingSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 뇌명 4세트 / 번분 2세트 + 검투사 2세트\n- 기사 2세트 + 검투사 2세트", inline=False)
        keqingSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        keqingSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        keqingSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 번개 원소 피해 %\n- 물리 피해 보너스 %\n(기 + 검 세트 적용)", inline=True)
        keqingSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        keqingSetEmbed.set_thumbnail(url="attachment://keqing.jpg")
        await ctx.send(file=keqingImage, embed=keqingSetEmbed, delete_after=300.0)

    elif 이름 == "피슬" :
        fischlImage = discord.File(str(srcPath)+"src/character/fischl.jpg", filename="fischl.jpg")
        fischlSetEmbed = discord.Embed(title="단죄의 황녀 · 피슬", color=0xFAE8B6)
        fischlSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 날개 / 아모스의 활", inline=False)
        fischlSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 번분 4세트 / 기사도 2세트 + 검투사 2세트 (아모스의 활)", inline=False)
        fischlSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        fischlSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        fischlSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 물리 피해 보너스 %\n- 번개 원소 피해 %\n(번분 세트 적용)", inline=True)
        fischlSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        fischlSetEmbed.set_thumbnail(url="attachment://fischl.jpg")
        await ctx.send(file=fischlImage, embed=fischlSetEmbed, delete_after=300.0)

    elif 이름 == "북두" :
        beidouImage = discord.File(str(srcPath)+"src/character/beidou.png", filename="beidou.png")
        beidouSetEmbed = discord.Embed(title="무관의 용왕 · 북두", color=0xB1A4B8)
        beidouSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로 / 제례대검", inline=False)
        beidouSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 번분 2세트 + 검투사 2세트", inline=False)
        beidouSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        beidouSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        beidouSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 번개 원소 피해 %", inline=True)
        beidouSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        beidouSetEmbed.set_thumbnail(url="attachment://beidou.png")
        await ctx.send(file=beidouImage, embed=beidouSetEmbed, delete_after=300.0)

    elif 이름 == "레이저" :
        razorImage = discord.File(str(srcPath)+"src/character/razor.png", filename="razor.png")
        razorSetEmbed = discord.Embed(title="늑대소년 · 레이저", color=0xA68FCD)
        razorSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 늑대의 말로 / 천공의 긍지", inline=False)
        razorSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 검투사 4세트", inline=False)
        razorSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        razorSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        razorSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %", inline=True)
        razorSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        razorSetEmbed.set_thumbnail(url="attachment://razor.png")
        await ctx.send(file=razorImage, embed=razorSetEmbed, delete_after=300.0)

    elif 이름 == "리사" :
        lisaImage = discord.File(str(srcPath)+"src/character/lisa.png", filename="lisa.png")
        lisaSetEmbed = discord.Embed(title="장미 마녀 · 리사", color=0x5339A6)
        lisaSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 두루마리 / 사풍원서", inline=False)
        lisaSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 번분 4세트", inline=False)
        lisaSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        lisaSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        lisaSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 번개 원소 피해 %", inline=True)
        lisaSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        lisaSetEmbed.set_thumbnail(url="attachment://lisa.png")
        await ctx.send(file=lisaImage, embed=lisaSetEmbed, delete_after=300.0)

    elif 이름 == "아이테르" :
        aetherImage = discord.File(str(srcPath)+"src/character/aether.jpg", filename="aether.jpg")
        aetherSetEmbed = discord.Embed(title="여행자 · 아이테르", color=0xF7F4E3)
        aetherSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 참봉의 칼날", inline=False)
        aetherSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 반암 2세트 + 검투사 2세트 / 반암 2세트 + 왕실 2세트", inline=False)
        aetherSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 / 치명타 피해", inline=False)
        aetherSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        aetherSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %\n- 바위 원소 피해 %", inline=True)
        aetherSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률\n- 치명타 피해", inline=True)
        aetherSetEmbed.set_thumbnail(url="attachment://aether.jpg")
        await ctx.send(file=aetherImage, embed=aetherSetEmbed, delete_after=300.0)

    elif 이름 == "노엘" :
        noelleImage = discord.File(str(srcPath)+"src/character/noelle.jpg", filename="noelle.jpg")
        noelleSetEmbed = discord.Embed(title="수여받지 못한 꽃 · 노엘", color=0xBFBFC0)
        noelleSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로 / 백영검 / 이무기 검", inline=False)
        noelleSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 유성 4세트", inline=False)
        noelleSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 방어력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        noelleSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 방어력 %", inline=True)
        noelleSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 방어력 %\n- 바위 원소 피해 %", inline=True)
        noelleSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        noelleSetEmbed.set_thumbnail(url="attachment://noelle.jpg")
        await ctx.send(file=noelleImage, embed=noelleSetEmbed, delete_after=300.0)

    elif 이름 == "응광" :
        ningguangImage = discord.File(str(srcPath)+"src/character/ningguang.png", filename="ningguang.png")
        ningguangSetEmbed = discord.Embed(title="엄월천권 · 응광", color=0xBFBFC0)
        ningguangSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 속세의 자물쇠 / 천공의 두루마리 / 일월의 정수 / 소심", inline=False)
        ningguangSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 반암 2세트 + 검투사 2세트", inline=False)
        ningguangSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 원소 충전 효율 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        ningguangSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        ningguangSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 바위 원소 피해 %", inline=True)
        ningguangSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        ningguangSetEmbed.set_thumbnail(url="attachment://ningguang.png")
        await ctx.send(file=ningguangImage, embed=ningguangSetEmbed, delete_after=300.0)

    elif 이름 == "알베도" :
        albedoImage = discord.File(str(srcPath)+"src/character/albedo.jpg", filename="albedo.jpg")
        albedoSetEmbed = discord.Embed(title="알베도 무기 & 성유물 세팅", color=0xE3D8BF)
        albedoSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 여명신검", inline=False)
        albedoSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 수호자 2세트 + 반암 2세트 / 반암 4세트 / 반암 2세트 + 왕실 2세트", inline=False)
        albedoSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 방어력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        albedoSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 방어력 %", inline=True)
        albedoSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 방어력 %\n- 바위 원소 피해 %", inline=True)
        albedoSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 방어력 %\n- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        albedoSetEmbed.set_thumbnail(url="attachment://albedo.jpg")
        await ctx.send(file=albedoImage, embed=albedoSetEmbed, delete_after=300.0)

    elif 이름 == "종려" :
        zhongliImage = discord.File(str(srcPath)+"src/character/zhongli.jpg", filename="zhongli.jpg")
        zhongliSetEmbed = discord.Embed(title="종려 무기 & 성유물 세팅", color=0xE3964C)
        zhongliSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 관흥의 창 / 천공의 마루 / 화박연", inline=False)
        zhongliSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 반암 2세트 + 왕실 2세트 / 반암 2세트 + 검투사 2세트", inline=False)
        zhongliSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        zhongliSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- HP %\n- 공격력 %", inline=True)
        zhongliSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n- 바위 원소 피해 %", inline=True)
        zhongliSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        zhongliSetEmbed.set_thumbnail(url="attachment://zhongli.jpg")
        await ctx.send(file=zhongliImage, embed=zhongliSetEmbed, delete_after=300.0)

    elif 이름 == "향릉" :
        xianglingImage = discord.File(str(srcPath)+"src/character/xiangling.png", filename="xiangling.png")
        xianglingSetEmbed = discord.Embed(title="만민백미 · 향릉", color=0xBF4F2D)
        xianglingSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 화박연 / 천공의 마루 / 페보니우스 장창 / 유월창", inline=False)
        xianglingSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 2세트 + 왕실 2세트 & 검투사 2세트 / 마녀 4세트", inline=False)
        xianglingSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        xianglingSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        xianglingSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 공격력 %\n- 불 원소 피해 %", inline=True)
        xianglingSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        xianglingSetEmbed.set_thumbnail(url="attachment://xiangling.png")
        await ctx.send(file=xianglingImage, embed=xianglingSetEmbed, delete_after=300.0)

    elif 이름 == "클레" :
        kleeImage = discord.File(str(srcPath)+"src/character/klee.jpg", filename="klee.jpg")
        kleeSetEmbed = discord.Embed(title="도망치는 태양 · 클레", color=0xB84E44)
        kleeSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 사풍원서", inline=False)
        kleeSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트", inline=False)
        kleeSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        kleeSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        kleeSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
        kleeSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        kleeSetEmbed.set_thumbnail(url="attachment://klee.jpg")
        await ctx.send(file=kleeImage, embed=kleeSetEmbed, delete_after=300.0)

    elif 이름 == "다이루크" :
        dilucImage = discord.File(str(srcPath)+"src/character/diluc.png", filename="diluc.png")
        dilucSetEmbed = discord.Embed(title="새벽의 어둠 · 다이루크", color=0xDC545C)
        dilucSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로", inline=False)
        dilucSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트", inline=False)
        dilucSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 %", inline=False)
        dilucSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        dilucSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
        dilucSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        dilucSetEmbed.set_thumbnail(url="attachment://diluc.png")
        await ctx.send(file=dilucImage, embed=dilucSetEmbed, delete_after=300.0)

    elif 이름 == "베넷" :
        bennettImage = discord.File(str(srcPath)+"src/character/bennett.png", filename="bennett.png")
        bennettSetEmbed = discord.Embed(title="운명의 시금석 · 베넷", color=0xF1E8D4)
        bennettSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 검 / 제례검", inline=False)
        bennettSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 왕실 4세트", inline=False)
        bennettSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 % (①)", inline=False)
        bennettSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 % (①)\n- 원소 충전 효율 %", inline=True)
        bennettSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n불 원소 피해 %", inline=True)
        bennettSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치유 보너스 %\n- 치명타 확률 % (①)", inline=True)
        bennettSetEmbed.set_thumbnail(url="attachment://bennett.png")
        await ctx.send(file=bennettImage, embed=bennettSetEmbed, delete_after=300.0)

    elif 이름 == "엠버" :
        amberImage = discord.File(str(srcPath)+"src/character/amber.png", filename="amber.png")
        amberSetEmbed = discord.Embed(title="비행 챔피언 · 엠버", color=0xA21730)
        amberSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 페보니우스 활", inline=False)
        amberSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 악단 4세트", inline=False)
        amberSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해 % / 원소 충전 효율 %", inline=False)
        amberSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %\n- 원소 충전 효율 %", inline=True)
        amberSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
        amberSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        amberSetEmbed.set_thumbnail(url="attachment://amber.png")
        await ctx.send(file=amberImage, embed=amberSetEmbed, delete_after=300.0)

    elif 이름 == "신염" :
        xinyanImage = discord.File(str(srcPath)+"src/character/xinyan.png", filename="xinyan.png")
        xinyanSetEmbed = discord.Embed(title="폭열 멜로디 · 신염", color=0x68544A)
        xinyanSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 천공의 긍지 / 늑대의 말로", inline=False)
        xinyanSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 기사도 4세트 / 기사도 2세트 + 왕실 2세트", inline=False)
        xinyanSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 % / 치명타 확률 % / 치명타 피해", inline=False)
        xinyanSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        xinyanSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 물리 피해 보너스 %", inline=True)
        xinyanSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        xinyanSetEmbed.set_thumbnail(url="attachment://xinyan.png")
        await ctx.send(file=xinyanImage, embed=xinyanSetEmbed, delete_after=300.0)

    elif 이름 == "호두" :
        hutaoImage = discord.File(str(srcPath)+"src/character/hutao.jpg", filename="hutao.jpg")
        hutaoSetEmbed = discord.Embed(title="눈 그친 뒤의 매화향 · 호두", color=0xECAAA7)
        hutaoSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 호마의 지팡이 / 화박연 / 흑술창", inline=False)
        hutaoSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트", inline=False)
        hutaoSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- HP % / 치명타 확률 % / 치명타 피해", inline=False)
        hutaoSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- HP %", inline=True)
        hutaoSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- HP %\n- 불 원소 피해 %", inline=True)
        hutaoSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        hutaoSetEmbed.set_thumbnail(url="attachment://hutao.jpg")
        await ctx.send(file=hutaoImage, embed=hutaoSetEmbed, delete_after=300.0)

    elif 이름 == "연비" :
        yanfeiImage = discord.File(str(srcPath)+"src/character/yanfei.jpg", filename="yanfei.jpg")
        yanfeiSetEmbed = discord.Embed(title="지명무사 · 연비", color=0xE79EAF) 
        yanfeiSetEmbed.add_field(name="🗡️ │ 추천 무기", value="- 사풍 원서 / 속세의 자물쇠 / 일월의 정수 / 인동의 열매", inline=False)
        yanfeiSetEmbed.add_field(name="🌸 │ 성유물 조합", value="- 마녀 4세트 / 악단 4세트", inline=False)
        yanfeiSetEmbed.add_field(name="🔧 │ 보조 옵션", value="- 공격력 / 원소 마스터 / 치명타 확률 % / 치명타 피해 %", inline=False)
        yanfeiSetEmbed.add_field(name="⌛ │ 시간의 모래", value="- 공격력 %", inline=True)
        yanfeiSetEmbed.add_field(name="🍸 │ 공간의 성배", value="- 불 원소 피해 %", inline=True)
        yanfeiSetEmbed.add_field(name="👑 │ 이성의 왕관", value="- 치명타 확률 %\n- 치명타 피해 %", inline=True)
        yanfeiSetEmbed.set_thumbnail(url="attachment://yanfei.jpg")
        await ctx.send(file=yanfeiImage, embed=yanfeiSetEmbed, delete_after=300.0)




# ==========================================================================




@slash.slash(name="성유물",
             description="성유물과 관련된 데이터베이스를 보여줍니다.",
             options=[create_option(name="이름", description="해당하는 성유물의 효과와 획득처를 보여줍니다.", option_type=3, required=True)])

async def 이름(ctx, 이름: str) :

    if 이름 == "검투사" :
        finaleImage = discord.File(str(srcPath)+"src/artifacts/finale.png", filename="finale.png")
        finaleSetEmbed = discord.Embed(title="검투사의 피날레", color=0xFFE482)
        finaleSetEmbed.add_field(name="2세트 효과", value="공격력 +18%", inline=False)
        finaleSetEmbed.add_field(name="4세트 효과", value="해당 성유물 세트를 장착한 캐릭터가 한손검, 양손검, 장병기를 사용 시 캐릭터의 일반 공격으로 가하는 피해가 35% 증가한다.", inline=False)
        finaleSetEmbed.add_field(name="획득처", value="영역 토벌 - 바람 드래곤의 폐허로\n토벌 - 북풍의 왕랑, 울프의 영주 외 레진을 소모하는 모든 토벌", inline=False)
        finaleSetEmbed.set_thumbnail(url="attachment://finale.png")
        await ctx.send(file=finaleImage, embed=finaleSetEmbed, delete_after=300.0)

    elif 이름 == "악단" :
        troupeImage = discord.File(str(srcPath)+"src/artifacts/troupe.png", filename="troupe.png")
        troupeSetEmbed = discord.Embed(title="대지를 유랑하는 악단", color=0xFFE482)
        troupeSetEmbed.add_field(name="2세트 효과", value="원소 마스터리 +80pt", inline=False)
        troupeSetEmbed.add_field(name="4세트 효과", value="해당 성유물 세트를 장착한 캐릭터가 법구 또는 활을 사용시\n캐릭터의 강공격으로 가하는 피해가 35% 증가한다.", inline=False)
        troupeSetEmbed.add_field(name="획득처", value="영역 토벌 - 바람 드래곤의 폐허로\n토벌 - 북풍의 왕랑, 울프의 영주 외 레진을 소모하는 모든 토벌", inline=False)
        troupeSetEmbed.set_thumbnail(url="attachment://troupe.png")
        await ctx.send(file=troupeImage, embed=troupeSetEmbed, delete_after=300.0)

    elif 이름 == "번분" :
        furyImage = discord.File(str(srcPath)+"src/artifacts/fury.png", filename="fury.png")
        furySetEmbed = discord.Embed(title="번개 같은 분노", color=0xFFE482)
        furySetEmbed.add_field(name="2세트 효과", value="번개 원소 피해 +15%", inline=False)
        furySetEmbed.add_field(name="4세트 효과", value="과부하, 감전, 초전도 반응이 주는 피해가 40% 증가한다.\n원소 반응 발동 시 원소 스킬의 재사용 대기시간이 1초 줄어든다.\n해당 효과는 0.8초마다 1번 발동한다.", inline=False)
        furySetEmbed.add_field(name="획득처", value="비경 - 한 여름의 정원", inline=False)
        furySetEmbed.set_thumbnail(url="attachment://fury.png")
        await ctx.send(file=furyImage, embed=furySetEmbed, delete_after=300.0)

    elif 이름 == "뇌명" :
        thunderImage = discord.File(str(srcPath)+"src/artifacts/thunder.png", filename="thunder.png")
        thunderSetEmbed = discord.Embed(title="뇌명을 평정한 존자", color=0xFFE482)
        thunderSetEmbed.add_field(name="2세트 효과", value="번개 원소 내성 +40%", inline=False)
        thunderSetEmbed.add_field(name="4세트 효과", value="번개 원소의 영향을 받은 적에게 가하는 피해가 35% 증가한다.", inline=False)
        thunderSetEmbed.add_field(name="획득처", value="비경 - 한 여름의 정원", inline=False)
        thunderSetEmbed.set_thumbnail(url="attachment://thunder.png")
        await ctx.send(file=thunderImage, embed=thunderSetEmbed, delete_after=300.0)

    elif 이름 == "청록" :
        viridescentImage = discord.File(str(srcPath)+"src/artifacts/viridescent.png", filename="viridescent.png")
        viridescentSetEmbed = discord.Embed(title="청록색 그림자", color=0xFFE482)
        viridescentSetEmbed.add_field(name="2세트 효과", value="바람 원소 피해 +15%", inline=False)
        viridescentSetEmbed.add_field(name="4세트 효과", value="확산 반응이 가하는 피해가 60% 증가한다. 확산되는\n원소 타입에 따라 피해 범위 내 적의 해당 원소의 내성이 40% 감소한다.\n지속 시간 - 10초.", inline=False)
        viridescentSetEmbed.add_field(name="획득처", value="비경 - 각인의 골짜기", inline=False)
        viridescentSetEmbed.set_thumbnail(url="attachment://viridescent.png")
        await ctx.send(file=viridescentImage, embed=viridescentSetEmbed, delete_after=300.0)

    elif 이름 == "소녀" :
        belovedImage = discord.File(str(srcPath)+"src/artifacts/beloved.png", filename="beloved.png")
        belovedSetEmbed = discord.Embed(title="사랑받는 소녀", color=0xFFE482)
        belovedSetEmbed.add_field(name="2세트 효과", value="캐릭터가 주는 치유 효과 +15%", inline=False)
        belovedSetEmbed.add_field(name="4세트 효과", value="원소 전투 스킬 또는 원소폭발 발동 후 10초 동안\n파티 내 모든 캐릭터가 받는 치유 효과가 20% 증가한다.", inline=False)
        belovedSetEmbed.add_field(name="획득처", value="비경 - 각인의 골짜기", inline=False)
        belovedSetEmbed.set_thumbnail(url="attachment://beloved.png")
        await ctx.send(file=belovedImage, embed=belovedSetEmbed, delete_after=300.0)

    elif 이름 == "반암" :
        petraImage = discord.File(str(srcPath)+"src/artifacts/petra.png", filename="petra.png")
        petraSetEmbed = discord.Embed(title="유구한 반암", color=0xFFE482)
        petraSetEmbed.add_field(name="2세트 효과", value="바위 원소 피해 보너스를 15% 획득한다.", inline=False)
        petraSetEmbed.add_field(name="4세트 효과", value="바위 원소 반응으로 만들어진 결정을 획득 시 파티 내\n모든 캐릭터는 해당 원소 피해 보너스를 35% 획득한다. 지속 시간: 10초.\n이러한 효과로 1가지의 원소 피해 보너스만 획득할 수 있다.", inline=False)
        petraSetEmbed.add_field(name="획득처", value="비경 - 하늘을 찌르는 땅", inline=False)
        petraSetEmbed.set_thumbnail(url="attachment://petra.png")
        await ctx.send(file=petraImage, embed=petraSetEmbed, delete_after=300.0)

    elif 이름 == "유성" :
        bolideImage = discord.File(str(srcPath)+"src/artifacts/bolide.png", filename="bolide.png")
        bolideSetEmbed = discord.Embed(title="날아오르는 유성", color=0xFFE482)
        bolideSetEmbed.add_field(name="2세트 효과", value="보호막 강화 효과가 35% 상승한다.", inline=False)
        bolideSetEmbed.add_field(name="4세트 효과", value="보호막이 존재 시 추가로\n일반 공격과 강공격 보너스를 40% 획득한다.", inline=False)
        bolideSetEmbed.add_field(name="획득처", value="비경 - 하늘을 찌르는 땅", inline=False)
        bolideSetEmbed.set_thumbnail(url="attachment://bolide.png")
        await ctx.send(file=bolideImage, embed=bolideSetEmbed, delete_after=300.0)

    elif 이름 == "마녀" :
        witchImage = discord.File(str(srcPath)+"src/artifacts/witch.png", filename="witch.png")
        witchSetEmbed = discord.Embed(title="불타오르는 화염의 마녀", color=0xFFE482)
        witchSetEmbed.add_field(name="2세트 효과", value="불 원소 피해 +15%", inline=False)
        witchSetEmbed.add_field(name="4세트 효과", value="과부하, 연소 반응이 적에게 주는 피해가 40% 증가하고\n증발, 융해 반응의 보너스 계수가 15% 증가한다.\n원소 전투 스킬 발동 후 10초 동안\n2세트의 효과가 50% 증가한다. 최대 중첩수 - 3회", inline=False)
        witchSetEmbed.add_field(name="획득처", value="비경 - 무망 인구 밀궁", inline=False)
        witchSetEmbed.set_thumbnail(url="attachment://witch.png")
        await ctx.send(file=witchImage, embed=witchSetEmbed, delete_after=300.0)

    elif 이름 == "현인" :
        walkerImage = discord.File(str(srcPath)+"src/artifacts/walker.png", filename="walker.png")
        walkerSetEmbed = discord.Embed(title="불 위를 걷는 현인", color=0xFFE482)
        walkerSetEmbed.add_field(name="2세트 효과", value="불 원소 내성 +40%", inline=False)
        walkerSetEmbed.add_field(name="4세트 효과", value="불 원소의 영향을 받은 적에게 가하는 피해가 35% 증가한다.", inline=False)
        walkerSetEmbed.add_field(name="획득처", value="비경 - 무망 인구 밀궁", inline=False)
        walkerSetEmbed.set_thumbnail(url="attachment://walker.png")
        walkerSetEmbed.set_footer(text=str(ctx.message.author))
        await ctx.message.delete()
        await ctx.send(file=walkerImage, embed=walkerSetEmbed, delete_after=300.0)

    elif 이름 == "기사도" :
        chivalryImage = discord.File(str(srcPath)+"src/artifacts/chivalry.png", filename="chivalry.png")
        chivalrySetEmbed = discord.Embed(title="피에 물든 기사도", color=0xFFE482)
        chivalrySetEmbed.add_field(name="2세트 효과", value="가하는 물리 피해가 25% 증가한다.", inline=False)
        chivalrySetEmbed.add_field(name="4세트 효과", value="적을 처치한 후 10초 동안 강공격 사용 시\n스태미나를 소모하지 않고 강공격으로 가하는 피해가 50% 증가한다.", inline=False)
        chivalrySetEmbed.add_field(name="획득처", value="비경 - 화지 산굴", inline=False)
        chivalrySetEmbed.set_thumbnail(url="attachment://chivalry.png")
        await ctx.send(file=chivalryImage, embed=chivalrySetEmbed, delete_after=300.0)

    elif 이름 == "왕실" :
        noblesseImage = discord.File(str(srcPath)+"src/artifacts/noblesse.png", filename="noblesse.png")
        noblesseSetEmbed = discord.Embed(title="옛 왕실의 의식", color=0xFFE482)
        noblesseSetEmbed.add_field(name="2세트 효과", value="원소폭발로 가하는 피해가 20% 증가한다.", inline=False)
        noblesseSetEmbed.add_field(name="4세트 효과", value="원소폭발 후 파티 내 모든 캐릭터의 공격력이 20% 증가한다.\n지속 시간 - 12초. 해당 효과는 중첩되지 않는다.", inline=False)
        noblesseSetEmbed.add_field(name="획득처", value="비경 - 화지 산굴", inline=False)
        noblesseSetEmbed.set_thumbnail(url="attachment://noblesse.png")
        await ctx.send(file=noblesseImage, embed=noblesseSetEmbed, delete_after=300.0)

    elif 이름 == "왕실" :
        blizzardImage = discord.File(str(srcPath)+"src/artifacts/blizzard.png", filename="blizzard.png")
        blizzardSetEmbed = discord.Embed(title="얼음바람 속에서 길잃은 용사", color=0xFFE482)
        blizzardSetEmbed.add_field(name="2세트 효과", value="얼음 원소 피해 보너스 +15%", inline=False)
        blizzardSetEmbed.add_field(name="4세트 효과", value="얼음 원소의 영향을 받은 적을 공격 시\n치명타 확률이 20% 증가한다.\n만약 적이 빙결 상태라면 치명타 확률이 추가로 20% 증가한다.", inline=False)
        blizzardSetEmbed.add_field(name="획득처", value="비경 - 빈다그니르의 정상", inline=False)
        blizzardSetEmbed.set_thumbnail(url="attachment://blizzard.png")
        blizzardSetEmbed.set_footer(text=str(ctx.message.author))
        await ctx.send(file=blizzardImage, embed=blizzardSetEmbed, delete_after=300.0)

    elif 이름 == "몰락" :
        depthImage = discord.File(str(srcPath)+"src/artifacts/depth.png", filename="depth.png")
        depthSetEmbed = discord.Embed(title="몰락한 마음", color=0xFFE482)
        depthSetEmbed.add_field(name="2세트 효과", value="물 원소 피해 +15%", inline=False)
        depthSetEmbed.add_field(name="4세트 효과", value="원소전투 스킬 발동 후 15초 동안\n일반 공격과 강공격으로 가하는 피해가 30% 증가한다.", inline=False)
        depthSetEmbed.add_field(name="획득처", value="비경 - 빈다그니르의 정상", inline=False)
        depthSetEmbed.set_thumbnail(url="attachment://depth.png")
        await ctx.send(file=depthImage, embed=depthSetEmbed, delete_after=300.0)

    elif 이름 == "천암" :
        tenacityImage = discord.File(str(srcPath)+"src/artifacts/depth.png", filename="depth.png")
        tenacitySetEmbed = discord.Embed(title="견고한 천암", color=0xFFE482)
        tenacitySetEmbed.add_field(name="2세트 효과", value="HP +20%", inline=False)
        tenacitySetEmbed.add_field(name="4세트 효과", value="원소 전투 스킬로 적 명중 시 파티 내 주변 모든 캐릭터의\n공격력이 20% 증가하고 보호막 강화 효과가 30% 증가한다.\n지속 시간 - 3초. 이 효과는 0.5초마다 최대 1번 발동한다.\n성유물을 장착한 캐릭터가 대기 상태일 때도 효과가 발동된다.", inline=False)
        tenacitySetEmbed.add_field(name="획득처", value="비경 - 산등성이의 파수꾼", inline=False)
        tenacitySetEmbed.set_thumbnail(url="attachment://depth.png")
        await ctx.send(file=tenacityImage, embed=tenacitySetEmbed, delete_after=300.0)

    elif 이름 == "창백" :
        paleImage = discord.File(str(srcPath)+"src/artifacts/depth.png", filename="depth.png")
        paleSetEmbed = discord.Embed(title="창백의 화염", color=0xFFE482)
        paleSetEmbed.add_field(name="2세트 효과", value="가하는 물리 피해가 25% 증가한다", inline=False)
        paleSetEmbed.add_field(name="4세트 효과", value="원소 전투 스킬로 적 명중 시 공격력이 9% 증가한다.\n지속 시간 - 7초. 최대 중첩 수: 2회.\n해당 효과는 0.3초마다 1번 발동한다.\n최대 중첩 시 2세트 효과가 100% 상승한다.", inline=False)
        paleSetEmbed.add_field(name="획득처", value="비경 - 산등성이의 파수꾼", inline=False)
        paleSetEmbed.set_thumbnail(url="attachment://depth.png")
        await ctx.send(file=paleImage, embed=paleSetEmbed, delete_after=300.0)

# ====================================================================================================

@bot.command()
async def 지워(ctx):
    await ctx.channel.purge(limit=10)

@bot.command()
async def 튀어(ctx):
    await ctx.channel.purge(limit=100)

bot.run(token)
