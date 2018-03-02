from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Ration(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()

    def __str__(self):
        return '(Ration-%s-%s-%s)' % (self.timestamp, self.person, self.value)

    def __unicode__(self):
        return '(Ration-%s-%s-%s)' % (self.timestamp, self.person, self.value)


class BarPurchase(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()

    def __str__(self):
        return '(BarPurchase-%s-%s-%s)' % (self.timestamp, self.person, self.value)

    def __unicode__(self):
        return '(BarPurchase-%s-%s-%s)' % (self.timestamp, self.person, self.value)


class RichPerson(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    value = models.IntegerField()

    def __str__(self):
        return '(RichPerson-%s-%s-%s)' % (self.timestamp, self.person, self.value)

    def __unicode__(self):
        return '(RichPerson-%s-%s-%s)' % (self.timestamp, self.person, self.value)
