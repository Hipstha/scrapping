class Casa:

  #Constructor
  def __init__(self, color):
    self.color = color
    self.consumo_de_luz = 0
    self.consumo_de_agua = 0

  # todas los métodos deben tener self
  def pintar(self, color):
    self.color = color

  def prender_luz(self):
    self.consumo_de_luz += 10

  def abrir_ducha(self):
    self.consumo_de_agua += 10

  def tocar_timbre(self):
    print("RIIIING")
    self.consumo_de_luz += 2

# herencia
class Mansion(Casa):

  def prender_luz(self):
    self.consumo_de_luz += 50

mansion = Mansion("blanco")
mansion.prender_luz()
print(mansion.consumo_de_luz)