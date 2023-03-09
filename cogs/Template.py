from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name="template", description="Template", with_app_command=True)
    async def template(self, ctx):
        await ctx.defer(ephemeral=True)
        await ctx.send("Template")

async def setup(client):
    await client.add_cog(Template(client))