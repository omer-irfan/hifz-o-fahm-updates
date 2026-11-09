import json, os, subprocess, sys
os.makedirs('out', exist_ok=True)
subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'edge-tts'], check=True)
for sid, text in json.load(open('tts/script.json')):
    subprocess.run(['edge-tts', '--voice', 'ur-PK-AsadNeural', '--rate=+2%', '--text', text, '--write-media', f'out/{sid}.mp3'], check=True)
print(os.listdir('out'))
