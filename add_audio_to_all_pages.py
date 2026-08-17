import glob

html_files = glob.glob('*.html')
audio_button_html = '''        <button id="audio-toggle-btn" class="btn-lang" title="Bật/Tắt Âm Thanh & Nhạc Nền">
          <span>🔊</span>
          <span class="vi-text">Âm Thanh</span>
          <span class="en-text">Audio</span>
        </button>'''

audio_script_html = '<script src="js/audio.js"></script>\n  <script src="js/app.js"></script>'

for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add audio button if not present
    if 'id="audio-toggle-btn"' not in content and 'id="lang-toggle-btn"' in content:
        content = content.replace('<button id="lang-toggle-btn"', f'{audio_button_html}\n        <button id="lang-toggle-btn"')

    # Add audio script if not present
    if 'js/audio.js' not in content and 'js/app.js' in content:
        content = content.replace('<script src="js/app.js"></script>', audio_script_html)

    with open(h, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Audio added to {h}')

print("All 10 pages successfully equipped with Audio Engine!")
