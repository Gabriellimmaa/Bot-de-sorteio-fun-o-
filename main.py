@client.command(pass_context=True)
@has_permissions(administrator=True)
async def sorteio(ctx, *, channel: discord.TextChannel):
    cor = 0x2f3136
    user = ctx.message.author
    var = client.get_channel(id=channel.id)
    channel1 = var
    embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                             description="\n**>>> Cole o link da Thumbnail:**\n\n", color=cor)
    await ctx.send(embed=embed001)

    def check(m):
        return m.author == user

    try:
        r00 = await client.wait_for('message', check=check, timeout=60.0)
        msg = r00.content
        embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                 description="\n**>>> Cole o link da Imagem:**\n\n", color=cor)
        embed001.set_footer(text="Você tem a opção de não colocar imagem - digite 'pular'")
        await ctx.send(embed=embed001)

        r01 = await client.wait_for('message', check=check, timeout=60.0)
        msg2 = r01.content
        if msg2 == "pular":
            embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                     description="\n**>>> Digite o Titulo do anuncio:**\n\n", color=cor)
            await ctx.send(embed=embed001)
            r02 = await client.wait_for('message', check=check, timeout=60.0)
            msg3 = r02.content

            embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                     description="\n**>>> Digite a mensagem que quer divulgar:**\n\n", color=cor)
            await ctx.send(embed=embed001)
            r03 = await client.wait_for('message', check=check, timeout=60.0)
            msg4 = r03.content

            embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                     description="\n**>>> Digite o tempo do sorteio em segundos:**\n\n", color=cor)
            await ctx.send(embed=embed001)
            r04 = await client.wait_for('message', check=check, timeout=60.0)
            time = r04.content

            embed001 = discord.Embed(title=f"{msg3}",
                                     description=f"{msg4}",
                                     color=cor)
            embed001.set_thumbnail(url=msg)
            aaa = await ctx.send(embed=embed001)
            for emoji in ('✅', '❌'):
                await aaa.add_reaction(emoji)

            def check3(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['✅', '❌']

            reaction, user = await client.wait_for('reaction_add', check=check3, timeout=40.0)
            if reaction.emoji == '✅':
                embed001 = discord.Embed(title=f"{msg3}",
                                         description=f"{msg4}", color=cor)
                embed001.set_thumbnail(url=f"{msg}")
                embed001.set_footer(text="Bot Desenvolvido por - [ALC]RD#8566")
                sorteio = await channel1.send(embed=embed001)
                await sorteio.add_reaction("🎉")

                time = int(time)

                await asyncio.sleep(time)

                msg = await sorteio.channel.fetch_message(sorteio.id)
                winner = None

                for reaction in msg.reactions:
                    if reaction.emoji == "🎉":
                        users = await reaction.users().flatten()
                        users.remove(client.user)
                        winner = random.choice(users)

                if winner is not None:
                    endembed = discord.Embed(
                        title="Sorteio finalizado!",
                        description="**Vencedor:** {}\n\n{}".format(winner.mention, msg4), color=cor)
                    endembed.set_footer(text="🎉 Parabéns ")

                    await msg.edit(embed=endembed)
            elif reaction.emoji == '❌':
                embed = discord.Embed(title="", description="Ação cancelada {}".format(user.mention),
                                      color=cor)
                await ctx.send(embed=embed)
        else:
            embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                     description="\n**>>> Digite o Titulo do anuncio:**\n\n", color=cor)
            await ctx.send(embed=embed001)
            r02 = await client.wait_for('message', check=check, timeout=60.0)
            msg3 = r02.content

            embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                     description="\n**>>> Digite a mensagem que quer divulgar:**\n\n", color=cor)
            await ctx.send(embed=embed001)
            r03 = await client.wait_for('message', check=check, timeout=60.0)
            msg4 = r03.content

            embed001 = discord.Embed(title="**DIVULGAÇÃO**",
                                     description="\n**>>> Digite o tempo do sorteio em segundos:**\n\n", color=cor)
            await ctx.send(embed=embed001)
            r04 = await client.wait_for('message', check=check, timeout=60.0)
            time = r04.content

            embed001 = discord.Embed(title=f"{msg3}",
                                     description=f"{msg4}",
                                     color=cor)
            embed001.set_thumbnail(url=msg)
            embed001.set_image(url=msg2)
            aaa = await ctx.send(embed=embed001)
            for emoji in ('✅', '❌'):
                await aaa.add_reaction(emoji)

            def check2(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['✅', '❌']

            reaction, user = await client.wait_for('reaction_add', check=check2, timeout=40.0)
            if reaction.emoji == '✅':
                embed001 = discord.Embed(title=f"{msg3}",
                                         description=f"{msg4}",
                                         color=cor)
                embed001.set_thumbnail(url=f"{msg}")
                embed001.set_image(url=f"{msg2}")
                embed001.set_footer(text="Bot Desenvolvido por - [ALC]RD#8566")
                await channel1.send(embed=embed001)
                sorteio = await channel1.send(embed=embed001)
                await sorteio.add_reaction("🎉")

                time = int(time)

                await asyncio.sleep(time)

                msg = await sorteio.channel.fetch_message(sorteio.id)
                winner = None

                for reaction in msg.reactions:
                    if reaction.emoji == "🎉":
                        users = await reaction.users().flatten()
                        users.remove(client.user)
                        winner = random.choice(users)

                if winner is not None:
                    endembed = discord.Embed(
                        title="Sorteio finalizado!",
                        description="Vencedor: {}".format(winner, msg4), color=cor)
                    endembed.set_footer(text="🎉 Parabéns ")

                    await msg.edit(embed=endembed)
            elif reaction.emoji == '❌':
                embed = discord.Embed(title="", description="Ação cancelada {}".format(user.mention),
                                      color=cor)
                await ctx.send(embed=embed)
    except asyncio.TimeoutError:
        await ctx.send('Seu tempo esgotou ...')
