import os
import glob

admin_pw = os.environ.get('MKDOCS_PASSWORD', '')
user_pw = os.environ.get('MKDOCS_USER_PASSWORD', '')

if not admin_pw or not user_pw:
    print('ERROR: MKDOCS_PASSWORD or MKDOCS_USER_PASSWORD not set')
    exit(1)

count = 0
for f in glob.glob('docs/**/*.md', recursive=True):
    txt = open(f).read()
    if 'INJECT_ADMIN_PASSWORD' in txt or 'INJECT_USER_PASSWORD' in txt:
        txt = txt.replace('INJECT_ADMIN_PASSWORD', admin_pw)
        txt = txt.replace('INJECT_USER_PASSWORD', user_pw)
        open(f, 'w').write(txt)
        count += 1

print(f'Injected passwords into {count} files')
