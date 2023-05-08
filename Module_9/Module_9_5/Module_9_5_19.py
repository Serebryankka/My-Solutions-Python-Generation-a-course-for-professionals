def date_formatter(country_code):
    def formate(date):
        code = {
            'ru': '%d.%m.%Y',
            'us': '%m-%d-%Y',
            'ca': '%Y-%m-%d',
            'br': '%d/%m/%Y',
            'fr': '%d.%m.%Y',
            'pt': '%d-%m-%Y'
        }
        return date.strftime(code[country_code])
    return formate
