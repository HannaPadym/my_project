class SplitConverter:
    regex = r'(\w+,)+\w+'

    def to_python(self, value: str):
        return value.split(',')

    def to_url(self, value: list):
        return ','.join(value)