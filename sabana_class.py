class Sabana:
    def __init__(sabana, order, date, mo, model, inspector, lines, tags, url):
        sabana.date = date
        sabana.order = order
        sabana.mo = mo
        sabana.model = model
        sabana.inspector = inspector
        sabana.lines = lines
        sabana.tags = tags
        sabana.url = url
    
    def __repr__(self):
        return (f'>>{self.date} >> {self.order} MODELO: {self.model} URL: {self.url}')    
