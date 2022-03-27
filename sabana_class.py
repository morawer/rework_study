class Sabana:
    def __init__(sabana, order, date, mo, model, inspector, lines, tags):
        sabana.date = date
        sabana.order = order
        sabana.mo = mo
        sabana.model = model
        sabana.inspector = inspector
        sabana.lines = lines
        sabana.tags = tags
    
    def __repr__(self):
        return (f'>>{self.order} MODELO: {self.model} LINEAS: {self.lines}')    
