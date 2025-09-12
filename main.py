import discord
import os
from dotenv import load_dotenv

# --- SETTINGS ---
# This is the only line you'll need to edit if the rate changes!
DEVEX_RATE = 0.0038 
# -----------------
BUXTAX_URL = "https://bux.tax"

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Success! {bot.user} is online and ready!")

@bot.slash_command(name="devex", description="Calculate Robux to USD at the latest rate.")
async def devex(ctx, robux: int):
    # Perform the calculations
    official_usd = robux * DEVEX_RATE
    
    # This is a placeholder to show the value of your main BuxTax app.
    # We're just estimating a 15% difference for now.
    true_take_home_usd = official_usd * 0.85 

    # Create a professional-looking response (an "embed")
    embed = discord.Embed(
        title="BuxTax DevEx Calculation",
        url=BUXTAX_URL, # This makes the title clickable
        description=f"Showing the value for **R$ {robux:,}**.",
        color=discord.Color.from_rgb(11, 168, 224) # A nice blue color
    )
    embed.add_field(name="Official DevEx Payout", value=f"**${official_usd:,.2f} USD**", inline=False)
    embed.add_field(name="BuxTax 'True Take-Home' (Est.)", value=f"~${true_take_home_usd:,.2f} USD", inline=False)
    embed.add_field(name="🚀 Full Features", value=f"[Click Here to Visit BuxTax]({BUXTAX_URL})", inline=False)
    embed.set_footer(text="For full tracking, CSV uploads, and goal setting, visit BuxTax.")

    # Send the response
    await ctx.respond(embed=embed)

bot.run(os.getenv('DISCORD_TOKEN'))