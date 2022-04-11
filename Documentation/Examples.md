# Examples

## Simple console example

```python
import uberduck

client = uberduck.UberDuck(YOUR_API_KEY, YOUR_API_SECRET)
voices = uberduck.get_voices(return_only_names = True)

speech = input('Enter speech: ')
voice = input('Enter voice or enter "LIST" to see list of voices: ')

if voice == 'LIST':
    print('Available voices:\n')
    for voice in sorted(voices): # sorting the voice list in alphabetical order
        print(voice)
    exit()

if voice not in voices:
    print('Invalid voice')
    exit()

client.speak(speech, voice, play_sound = True)
print('Spoke voice')
```

## TTS Discord bot using [discord.py](https://github.com/Rapptz/discord.py)

```python
import uberduck
import discord
from io import StringIO, BytesIO

bot = commands.Bot(
    command_prefix = '!',
    description = 'UberDuck Discord bot'
    strip_after_prefix = True,
    intents = discord.Intents.all()
)
uberduck_client = uberduck.UberDuck(YOUR_API_KEY, YOUR_API_SECRET)

@bot.command()
async def speak(ctx, voice, *, speech):
    if voice not in bot.uberduck_voices:
        return await ctx.reply('Invalid voice, please do `!voices` to see all the voices.')

    await ctx.send('Loading...')
    async with ctx.typing():
        try:
            result = await uberduck_client.speak_async(speech, voice, check_every = 0.5)
            file = discord.File(
                BytesIO(result),
                filename = 'audio.wav',
            )
        except uberduck.UberduckException as e:
            return await ctx.reply(f'Sorry, an error occured\n{e}')
        
        await ctx.send(file = file)

@bot.command()
async def voices(ctx):
    file = discord.File(
        StringIO(
            '\n'.join(
                await uberduck_client.speak_async(return_only_names = True)
            )
        ),
        filename = 'voices.txt'
    )
    await ctx.reply(file = file)

bot.run(TOKEN)
```

## Basic [tkinter](https://docs.python.org/3/library/tkinter.html) app

```python
import tkinter as tk
import uberduck

root = tk.Tk()
duck = uberduck.UberDuck(YOUR_API_KEY, YOUR_API_SECRET)

root.title('UberDuck')
root.geometry('400x400')
root['background'] = '#111119'

speech_textbox = tk.Entry(root)
speech_textbox.pack()

voices = uberduck.get_voices()
names = {
    v.display_name: v.name for v in voices
} # dictionary comprehension, here i made a dictionary with the display name as the key and the name as the value
# i'll show the display names to the user in a dropdown and use the linked name to send the request to the uberduck library
display_names = list(names.keys())
clicked = tk.StringVar()
clicked.set(display_names[0])

dropdown_menu = tk.OptionMenu(root, clicked, *display_names)
dropdown_menu.pack()

def speak():
    if text := speech_textbox.get():
        duck.speak(
            text, names[clicked.get()],
            return_bytes = False,
            play_sound = True
        )

button = tk.Button(root, text = 'Speak', command = speak)
button.pack()

root.mainloop()
```

## Basic webapp using [quart](https://pgjones.gitlab.io/quart/)

```python
from quart import Quart, redirect
import uberduck

app = Quart(__name__)
client = uberduck.UberDuck(YOUR_API_KEY, YOUR_API_SECRET)

@app.route('/')
async def index():
    return '''
    <h1>Welcome to the voice-inator!</h1>
    '''.strip()

@app.route('/<speech>/<voice>', methods=['GET'])
async def speak_route(speech: str, voice: str):
    try:
        url = await client.speak_async(speech, voice, return_bytes = False)
    except uberduck.InvalidVoice:
        return '''
        <h1>Invalid voice! Please go to <a href="/voicelist">the voicelist</a> to see all voices.</h1>
        '''.strip()

    return redirect(url, code = 300) # 300 meaning there can be multiple URLs to redirect to

@app.route('/voicelist', methods = ['GET'])
async def voicelist():
    voices = '<br>'.join(
        await uberduck.get_voices_async(return_only_names = True)
    )
    return f'''
<h1>Voicelist</h1>
<h2>
{voices}
</h2>
'''.strip()

app.run(host = '127.0.0.1', port = 8000, debug = True)
```