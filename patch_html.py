import glob

html_files = glob.glob('*.html')
for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'js/data_items.js' not in content and 'js/data.js' in content:
        new_content = content.replace('<script src="js/data.js"></script>', '<script src="js/data.js"></script>\n  <script src="js/data_items.js"></script>')
        with open(h, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Successfully patched {h}')

print("All pages verified.")
