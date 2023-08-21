'''
Costs money to get an API Key, so I haven't tried it yet.
'''
from modernmt import ModernMT
import pdb
mmt = ModernMT("YOUR_API_KEY")
language = mmt.detect_language("buongiorno")
pdb.set_trace()