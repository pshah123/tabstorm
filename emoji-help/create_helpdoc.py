import json
import os

data = json.load(open('emoji.json'))
print("%d emojis loaded" % len(data))
colon_codes = []
for emoji_data in data:
    for colon_code in emoji_data["short_names"]:
        if len(colon_code) < 13:
            colon_codes.append(
                {"code": colon_code, "image": emoji_data["image"]})
emoji_img_url = "https://github.com/iamcal/emoji-data/raw/340e3b897f71ca985ceccbd6b753e37776734f26/img-apple-64/"
_out = ["`:{c}:` | ![{c}]({l})".format(
    c=code["code"], l=emoji_img_url + code["image"]) for code in colon_codes]


def chunks(l, n):
    for i in range(0, len(l), n):
        yield ' | '.join(l[i:i + n])


md_table = ' | '.join(['Colon Code | Emoji'] * 4) + '\n' + \
    ' | '.join(['--- | ---'] * 4) + '\n' + '\n'.join(list(chunks(_out, 4)))
with open('README.md', 'w') as f:
    f.write(md_table)
