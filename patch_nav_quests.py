import glob

html_files = glob.glob('*.html')
quest_nav_item = '<a href="quests.html" class="nav-link">📜 <span class="vi-text">Nhiệm Vụ</span><span class="en-text">Quests</span></a>'

for h in html_files:
    if h == 'quests.html':
        continue

    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add quest nav link right after Home link if not present
    if 'href="quests.html"' not in content and 'href="index.html" class="nav-link' in content:
        # Match home nav link
        home_tag = '<a href="index.html" class="nav-link'
        idx = content.find(home_tag)
        if idx != -1:
            end_tag_idx = content.find('</a>', idx) + 4
            content = content[:end_tag_idx] + '\n        ' + quest_nav_item + content[end_tag_idx:]

    with open(h, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Patched navigation in {h}")

print("All navigation bars successfully updated with Quests link!")
