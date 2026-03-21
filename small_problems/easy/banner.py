class Banner:
    PADDING = 2
    
    def __init__(self, message):
        self.message = message

    def _content_width(self):
        return len(self.message) + self.PADDING

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"|{' ' * self._content_width()}|"

    def _horizontal_rule(self):
        return f"+{'-' * self._content_width()}+"

    def _message_line(self):
        return f"| {self.message} |"
    

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

print(Banner('All that glitters is not gold.'))
print(Banner(''))