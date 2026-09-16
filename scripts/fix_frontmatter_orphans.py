import yaml, glob

bad = []
for f in glob.glob('content/posts/*.md'):
    try:
        text = open(f).read()
        if not text.startswith('---'):
            continue
        fm = text.split('---')[1]
        yaml.safe_load(fm)
    except Exception:
        bad.append(f)

print('files to fix:', bad)

for f in bad:
    text = open(f).read()
    parts = text.split('---', 2)
    lines = parts[1].split('\n')
    cleaned = []
    i = 0
    removed = 0
    while i < len(lines):
        line = lines[i]
        if (line.strip().startswith('a:') or line.strip().startswith('q:')) and not line.startswith((' ', '\t', '-')):
            # orphaned key at column 0 — not valid inside the faqs list
            prev = lines[i - 1] if i > 0 else ''
            if not prev.lstrip().startswith(('-', 'a:', 'q:')):
                i += 1
                removed += 1
                continue
        cleaned.append(line)
        i += 1
    parts[1] = '\n'.join(cleaned)
    newtext = '---'.join(parts)
    try:
        yaml.safe_load(newtext.split('---')[1])
        open(f, 'w').write(newtext)
        print(f'{f}: fixed ({removed} orphan line(s) removed)')
    except Exception as e:
        print(f'{f}: still broken after cleanup — {str(e)[:60]}')
