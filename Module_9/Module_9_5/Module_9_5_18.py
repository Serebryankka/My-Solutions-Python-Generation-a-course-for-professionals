def sourcetemplate(url):
    def querystring(**kwargs):
        return f'{url}?{"&".join([f"{k}={v}" for k, v in kwargs.items()])}' if kwargs else url

    return querystring
