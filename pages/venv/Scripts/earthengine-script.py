#!"C:\Users\GUNEET SINGH\PycharmProjects\summer\hackathon\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'earthengine-api==0.1.164','console_scripts','earthengine'
__requires__ = 'earthengine-api==0.1.164'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('earthengine-api==0.1.164', 'console_scripts', 'earthengine')()
    )
