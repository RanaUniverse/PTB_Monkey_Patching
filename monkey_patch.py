

import html
import telegram

class CustomUser(telegram.User):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    @property
    def full_name_html(self) -> str:
        """
        This will use full name as a HTML escaped so that if any < > will be present in the
        user name, it will use it as a normal string.
        """
        real_name = self.full_name
        escaped_name = html.escape(real_name)
        return escaped_name

    @property
    def full_name_cap(self):
        real_name = self.full_name_html
        cap_name = real_name.upper()
        cap_name = cap_name[::-1]
        return cap_name
    
    @property
    def name_double(self):
        real_name = self.full_name_html
        dob = 2 * real_name
        return dob
    
    @property
    def name_char_count(self):
        real_name = self.full_name_html
        leng = len(real_name)
        return leng
    
    @property
    def full_name_cap(self):
        real_name = self.full_name
        real_name = real_name.upper()
        real_name = html.escape(real_name)
        return real_name
    
    @property
    def double_string(self):
        """
        - "Rana" becomes "RRaannaa"
        """
        input_string = self.full_name
        doubled_characters = [char * 2 for char in input_string]
        doubled_string = ''.join(doubled_characters)
        doubled_string = html.escape(doubled_string)
        return doubled_string

# Apply the monkey patch
telegram._message.User = CustomUser
