enhanceLimit = 100
enhanceLevel = 0
enhanceLevelMax = 43
enhanceLevelMaxUser = "(discord username)#(tag number)"
enhanceUseUser = ""
enhanceLimitUp = 0
enhanceProtect = 3
enhanceCount = 411

@bot.command()
async def 강화(ctx):
    global enhanceLimit
    global enhanceLevel
    global enhanceLevelMax
    global enhanceLevelMaxUser
    global enhanceUseUser
    global enhanceLimitUp
    global enhanceProtect
    global enhanceCount

    enhanceRandom = random.randint(0,100)
    enhanceRandomUp = random.randint(1,25)
    enhanceUseUser = ctx.message.author
    enhanceCount += 1
    
    if enhanceRandom <= enhanceLimit :
        enhanceLevel += 1
        enhanceLimit = round(enhanceLimit*0.99, 3)

        if enhanceLevelMax < enhanceLevel :
            enhanceLevelMax += 1
            enhanceLevelMaxUser =  ctx.message.author

        if enhanceRandomUp == 17 :
            enhanceLimitUp = random.randint(1,5)
            enhanceEmbed = discord.Embed(title=str(enhanceUseUser) + "님, 강화 대성공 ! [ Lv." + str(enhanceLevel) + " ]", color=0xFFA47D, description="다음 확률 ─ " + str(enhanceLimit) + "% + " + str(enhanceLimitUp) + "%(보너스)\n실패 방어 ─ " + str(enhanceProtect) + " + 1회(보너스) 남음\n\n총 강화 횟수 ─ "+ str(enhanceCount) +"회\n마지막 최고 레벨 ─ Lv." + str(enhanceLevelMax) + " @ " + str(enhanceLevelMaxUser))
            enhanceProtect += 1


        else :
            enhanceEmbed = discord.Embed(title=str(enhanceUseUser) + "님, 강화 성공 ! [ Lv." + str(enhanceLevel) + " ]", color=0xFFD373, description="다음 확률 ─ " + str(enhanceLimit) + "%\n실패 방어 ─ " + str(enhanceProtect) + "회 남음\n\n총 강화 횟수 ─ " + str(enhanceCount) + "회\n마지막 최고 레벨 ─ Lv." + str(enhanceLevelMax) + " @ " + str(enhanceLevelMaxUser))

    else :
        if enhanceProtect > 0 :
            enhanceProtect -= 1
            enhanceEmbed = discord.Embed(title=str(enhanceUseUser) + "님, 강화 실패 방어 ! [ Lv." + str(enhanceLevel) + " ]", color=0xAFFF7D, description="다음 확률 ─ " + str(enhanceLimit) + "%\n실패 방어 ─ " + str(enhanceProtect) + "회 남음\n\n총 강화 횟수 ─ " + str(enhanceCount) + "회\n마지막 최고 레벨 ─ Lv." + str(enhanceLevelMax) + " @ " + str(enhanceLevelMaxUser))

            
        else : 
            enhanceLevel = 0
            enhanceLimit = 100
            enhanceEmbed = discord.Embed(title=str(enhanceUseUser) + "님, 강화 실패 ! [ Lv." + str(enhanceLevel) + " ]", color=0xA67DFF, description="다음 확률 ─ " + str(enhanceLimit) + "%\n실패 방어 ─ " + str(enhanceProtect) + "회 남음\n\n총 강화 횟수 ─ " + str(enhanceCount) + "회\n마지막 최고 레벨 ─ Lv." + str(enhanceLevelMax) + " @ " + str(enhanceLevelMaxUser))
            enhanceProtect = 3
            
    await ctx.message.delete()
    await ctx.send(embed=enhanceEmbed)
