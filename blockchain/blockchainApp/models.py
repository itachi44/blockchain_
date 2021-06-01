from djongo import models

"""
class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    identifiant = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)
    cni = models.CharField(max_length=100)
    paiement_accepte = models.ArrayField(models.ArrayField(models.CharField()))
    

class Propriete(models.Model):
     vendeur = models.CharField(max_length=100)
     position_geographique = models.CharField(max_length=100)
     prix= models.CharField(max_length=100)
     superfie = models.CharField(max_length=100)
     type_propriete = models.CharField(max_length=100)
     diagnostique = models.CharField(max_length=100)
     date_obtention=models.DateField()
     gps=models.CharField(max_length=100)

     Proprietaire = models.EmbeddedField(
        model_container=Proprietaire
    )


class Client(models.Model):
     nom = models.CharField(max_length=100)
     prenom = models.CharField(max_length=100)
     adresse= models.CharField(max_length=100)
     telephone = models.CharField(max_length=100)
     numero_compte = models.CharField(max_length=100)
     cni = models.CharField(max_length=100)


class transaction(models.Model):
    Propriete= models.EmbeddedField(
        model_container=Propriete
    )    
    Proprietaire = models.EmbeddedField(
        model_container=Proprietaire
    )    
    Client = models.EmbeddedField(
        model_container=Client
    )  
    date_obtention=models.DateField()
    justificatif=models.FileField(upload_to="images/justificatifs")






    

"""