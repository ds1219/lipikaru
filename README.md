# lipikaru (ලිපිකරු)
An romanization script for python, currently supports Sinhala
(hope to extend language support in the future! PRs appreciated)

## Examples

* ආයුබෝවන් - āyubōvan
* ශ්‍රී ලංකා ප්‍රජාතාන්ත්‍රික සමාජවාදී ජනරජය - shrī langkā prajāthānthrika samājavādī janarajaya
* කොළඹ - kolamba
* ශ්‍රී ජයවර්ධනපුර කෝට්ටේ - shrī jayavardhnapura kōttē
* මහනුවර - mahanuvara
* යාපනය - yāpanaya
* මඩකලපුව - madakalapuva
* ඥාන වීර්ය වඩවමින රැගෙන - gnāna vīrya vadavamina rægena
* මඤ්ඤොක්කා - maññokkā

# if you want to remove the diacritics (accent marks) from the output, then you can convert in from unicode to ASCII.
https://stackoverflow.com/a/7782177
```python
unicodedata.normalize("NFKD", "input text").encode("ascii", "ignore")
```
