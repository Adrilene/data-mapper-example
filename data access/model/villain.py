from ...main import engine


class Vilao(engine.Model):
    __tablename__ = "vilao"

    id = engine.Column(engine.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = engine.Column(engine.String(50), nullable=False)
    vida = engine.Column(engine.Integer, nullable=False)
