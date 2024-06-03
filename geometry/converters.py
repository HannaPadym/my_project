class UpperConvertor:
    regex = r'\w+'

    def to_python(self, value: str):
        return value.upper()

    def to_url(self, value: str):
        return value.lower()
