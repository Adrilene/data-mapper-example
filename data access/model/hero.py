from ...main import engine
import city

class Heroi(engine.Model):  
    __tablename__ = "heroi"

    id = engine.Column(engine.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = engine.Column(engine.String(50), nullable=False)
    cidade_id = engine.Column(engine.Integer, engine.ForeignKey("cidade.id"), nullable=False)
    forca = engine.Column(engine.Integer, nullable=False)
