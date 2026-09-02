import sys

with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
in_stats = False
for line in lines:
    if 'Real-Time GitHub Analytics' in line:
        in_stats = True
        out.append(line)
        out.append('\n<div align="center">\n\n')
        out.append('[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=saeedsad821-ux&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&title_color=38bdf8&icon_color=38bdf8)](https://github.com/saeedsad821-ux)\n')
        out.append('[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=saeedsad821-ux&theme=tokyonight&hide_border=true&title_color=38bdf8&icon_color=38bdf8)](https://github.com/saeedsad821-ux)\n')
        out.append('\n[![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=saeedsad821-ux&layout=compact&theme=tokyonight&hide_border=true&title_color=38bdf8)](https://github.com/saeedsad821-ux)\n')
        out.append('\n</div>\n')
    elif in_stats and '<br>' in line and len(line) < 10:
        continue
    elif in_stats and '<div align="center">' in line:
        continue
    elif in_stats and '<img src=' in line:
        continue
    elif in_stats and '</div>' in line:
        in_stats = False
    else:
        out.append(line)

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(out)
