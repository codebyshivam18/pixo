import os
from datetime import datetime
import discord
from discord import app_commands
from typing import Union, Optional
from discord.ext import commands
from discord.ext.commands import Context
import platform
import random
import aiohttp



class Info(commands.Cog, name="info"):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.hybrid_command(
        name="botinfo",
        description="Get Information About Bot And Their Owner",
    )
    async def botinfo(self, context: Context) -> None:
        embed = discord.Embed(
            description="",
            color=0xBEBEFE,
        )
        embed.set_author(name="Bot Information")
        embed.add_field(name="Owner:", value="code.with.shivam", inline=True)
        embed.add_field(
            name="Python Version:", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"/ (Slash Commands) or <@1302520601461919804> (mention) for normal commands",
            inline=True,
        )
        embed.add_field(
            name="Server:",
            value=f"Joint Support Server by clicking **[here]({self.bot.config['server_link']})**.",
            inline=False,
          )
        embed.add_field(
            name="**Invite:**",
            value=f"Invite Bot By Clicking **[here]({self.bot.config['invite_link']})**.",
            inline=False,
          )
        embed.set_footer(text=f"Requested by {context.author}")
        await context.send(embed=embed)
    
    @commands.hybrid_command(
            name="serverinfo",
            description="Get Information About Server/Guild",
        )
    async def serverinfo(self, context: Context) -> None:
            roles = [role.name for role in context.guild.roles]
            num_roles = len(roles)
            if num_roles > 50:
                roles = roles[:50]
                roles.append(f">>>> Displaying [50/{num_roles}] Roles")
            roles = ", ".join(roles)
    
            embed = discord.Embed(
                title="**Server Name:**", description=f"{context.guild}", color=0xBEBEFE
            )
            if context.guild.icon is not None:
                embed.set_thumbnail(url=context.guild.icon.url)
            embed.add_field(name="Server ID", value=context.guild.id)
            embed.add_field(name="Member Count", value=context.guild.member_count)
            embed.add_field(
                name="Text/Voice Channels", value=f"{len(context.guild.channels)}"
            )
            embed.add_field(name=f"Roles ({len(context.guild.roles)})", value=roles)
            embed.set_footer(text=f"Created at: {context.guild.created_at}, ")
            await context.send(embed=embed)
            
    @commands.hybrid_command(
        name="whois",
        description="Get Information About User",
    )
    async def whois(self, context: Context, user: Optional[Union[discord.Member, discord.User]]) -> None:
      
        if user==None: 
          user=context.author
        
        rlist = []
        for role in user.roles: 
          if role.name != "@everyone": 
            rlist.append(role.mention)
            
        b = ", ".join(rlist)
      
        embed = discord.Embed(
            color=user.color,
        )
        embed.set_author(
          name=f"User Info - {user}"
          )
        
        embed.set_thumbnail(
          url=user.avatar.url
          )
          
        embed.set_footer(
          text=f"Requested By {context.author}", 
          icon_url=context.author.avatar
          )
         
        embed.add_field(name="ID:", value=user.id, inline=False)
        embed.add_field(
            name="Name:", value=user.name, inline=False
        )
        embed.add_field(
            name="Created at:",
            value=user.created_at,
            inline=True,
        )
        embed.add_field(
            name="Joined at:",
            value=user.joined_at,
            inline=False,
          )
        embed.add_field(
            name="Bot?",
            value=user.bot,
            inline=False,
          )
        embed.add_field(
            name=f"Roles({len(rlist)}):",
            value="".join([b]),
            inline=True,
          )
        embed.add_field(
            name="Top Role:",
            value=user.top_role.mention,
            inline=False,
          )
          
        await context.send(embed=embed)
    
            
async def setup(bot) -> None:
    await bot.add_cog(Info(bot))