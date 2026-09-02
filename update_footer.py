import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the entire Real-Time GitHub Analytics section and everything below it
content = re.sub(r'<h2 align="center">📊 Real-Time GitHub Analytics</h2>.*', '', content, flags=re.DOTALL)

# Add a professional 'Let\'s Connect' section at the bottom
new_footer = '''<h2 align="center">📬 Let's Connect & Collaborate</h2>

<div align="center">
  <p>I am currently open for new opportunities in <b>Data Engineering</b>, <b>BI</b>, and <b>AI Automation</b>.</p>
  
  <a href="https://linkedin.com/in/saeed-saad-abdo">
    <img src="https://img.shields.io/badge/LinkedIn-Connect_with_me-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:saeedsad821@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-Send_me_an_email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</div>
'''

content += new_footer

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
