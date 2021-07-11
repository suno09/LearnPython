from typing import Final, final

'''
Final : const variable
'''

id_: Final = 1
id_ = 5  # Error id_ should be const


class Base:
    @final
    def done(self): ...


class Sub(Base):
    # Error because done is const on Base
    def done(self):
        ...
