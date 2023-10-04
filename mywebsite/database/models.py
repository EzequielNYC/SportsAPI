from django.db import models

class MetsData(models.Model):
    date = models.DateField(db_column='date', blank=True, null=True)
    opponent = models.TextField(db_column='opponent', blank=True, null=True)
    result = models.TextField(db_column='result', blank=True, null=True)
    mets_score = models.IntegerField(db_column='mets_score', blank=True, null=True)
    opponent_score = models.IntegerField(db_column='opponent_score', blank=True, null=True)
    location = models.TextField(db_column='location', blank=True, null=True)
    total_wins = models.IntegerField(db_column='total_wins', blank=True, null=True)
    total_losses = models.IntegerField(db_column='total_losses', blank=True, null=True)
    divisional_wins = models.IntegerField(db_column='divisional_wins', blank=True, null=True)
    divisional_losses = models.IntegerField(db_column='divisional_losses', blank=True, null=True)

    class Meta:
        db_table = 'mets_data'



class YankeesData(models.Model):
    date = models.DateField(db_column='date', blank=True, null=True)
    opponent = models.TextField(db_column='opponent', blank=True, null=True)
    result = models.TextField(db_column='result', blank=True, null=True)
    yankees_score = models.IntegerField(db_column='yankees_score', blank=True, null=True)
    opponent_score = models.IntegerField(db_column='opponent_score', blank=True, null=True)
    location = models.TextField(db_column='location', blank=True, null=True)
    total_wins = models.IntegerField(db_column='total_wins', blank=True, null=True)
    total_losses = models.IntegerField(db_column='total_losses', blank=True, null=True)
    divisional_wins = models.IntegerField(db_column='divisional_wins', blank=True, null=True)
    divisional_losses = models.IntegerField(db_column='divisional_losses', blank=True, null=True)

    class Meta:
        db_table = 'yankees_data'


class KnicksData(models.Model):
    date = models.DateField(db_column='date', blank=True, null=True)
    opponent = models.TextField(db_column='opponent', blank=True, null=True)
    result = models.TextField(db_column='result', blank=True, null=True)
    knicks_score = models.IntegerField(db_column='knicks_score', blank=True, null=True)
    opponent_score = models.IntegerField(db_column='opponent_score', blank=True, null=True)
    location = models.TextField(db_column='location', blank=True, null=True)
    total_wins = models.IntegerField(db_column='total_wins', blank=True, null=True)
    total_losses = models.IntegerField(db_column='total_losses', blank=True, null=True)
    divisional_wins = models.IntegerField(db_column='divisional_wins', blank=True, null=True)
    divisional_losses = models.IntegerField(db_column='divisional_losses', blank=True, null=True)
    
    class Meta:
        db_table = 'knicks_data'


class NetsData(models.Model):
    date = models.DateField(db_column='date', blank=True, null=True)
    opponent = models.TextField(db_column='opponent', blank=True, null=True)
    result = models.TextField(db_column='result', blank=True, null=True)
    nets_score = models.IntegerField(db_column='nets_score', blank=True, null=True)
    opponent_score = models.IntegerField(db_column='opponent_score', blank=True, null=True)
    location = models.TextField(db_column='location', blank=True, null=True)
    total_wins = models.IntegerField(db_column='total_wins', blank=True, null=True)
    total_losses = models.IntegerField(db_column='total_losses', blank=True, null=True)
    divisional_wins = models.IntegerField(db_column='divisional_wins', blank=True, null=True)
    divisional_losses = models.IntegerField(db_column='divisional_losses', blank=True, null=True)
     

    class Meta:
        db_table = 'nets_data'


class GiantsData(models.Model):
    date = models.DateField(db_column='date', blank=True, null=True)
    opponent = models.TextField(db_column='opponent', blank=True, null=True)
    result = models.TextField(db_column='result', blank=True, null=True)
    giants_score = models.IntegerField(db_column='giants_score', blank=True, null=True)
    opponent_score = models.IntegerField(db_column='opponent_score', blank=True, null=True)
    location = models.TextField(db_column='location', blank=True, null=True)
    total_wins = models.IntegerField(db_column='total_wins', blank=True, null=True)
    total_losses = models.IntegerField(db_column='total_losses', blank=True, null=True)
    divisional_wins = models.IntegerField(db_column='divisional_wins', blank=True, null=True)
    divisional_losses = models.IntegerField(db_column='divisional_losses', blank=True, null=True)

    class Meta:
        db_table = 'giants_data'


class JetsData(models.Model):
    date = models.DateField(db_column='date', blank=True, null=True)
    opponent = models.TextField(db_column='opponent', blank=True, null=True)
    result = models.TextField(db_column='result', blank=True, null=True)
    jets_score = models.IntegerField(db_column='jets_score', blank=True, null=True)
    opponent_score = models.IntegerField(db_column='opponent_score', blank=True, null=True)
    location = models.TextField(db_column='location', blank=True, null=True)
    total_wins = models.IntegerField(db_column='total_wins', blank=True, null=True)
    total_losses = models.IntegerField(db_column='total_losses', blank=True, null=True)
    divisional_wins = models.IntegerField(db_column='divisional_wins', blank=True, null=True)
    divisional_losses = models.IntegerField(db_column='divisional_losses', blank=True, null=True)  

    class Meta:
        db_table = 'jets_data'