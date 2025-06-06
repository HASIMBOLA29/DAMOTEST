import math

# Définition de la classe Surface
class Surface:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface_sphere(self):
        # Formule : 4 * π * r²
        return 4 * math.pi * self.rayon ** 2

# Création d’un objet ma_surface
rayon = float(input("Entrez le rayon de la sphère en cm : "))
ma_surface = Surface(rayon)

# Calcul et affichage
surface = ma_surface.calculer_surface_sphere()
print(f"La surface de la sphère de rayon {rayon} cm est : {surface:.2f} cm²")
