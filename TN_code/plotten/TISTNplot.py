#!/usr/bin/env python3

import matplotlib.ticker as mticker

"""
(c) 2018, D.D.Land <d.d.land@hhs.nl>

Module om figuren weer te geven zoals aangegeven in het Rapportage document
van de afdeling Technische Natuurkunde van de Haagse Hogeschool.

versie: 1.1

20190323: docstrings aangepast aan eisen programmeren.
20180317: herschreven naar class structuur om meerdere (sub)figuren hun eigen
aantal digits op de assen te kunnen geven.
"""


class TNFormatter(mticker.Formatter):
    """
    Class om een vast aantal significante getallen weer te geven in de
    assen van een figuur.

    Class wordt aangeroepen vanuit de axis formatter van een matplotlibfiguur.
    """

    def __init__(self, length=3):
        """
        Initialisatie van de TNFormatter class. Het aantal significante
        getallen (length) wordt gebruikt in andere functies om de getallen
        juist op te maken.

        argumenten:
            lengte: Geeft aan hoeveel significante getallen weergegeven
                    moeten worden.
        return:
            none
        """
        self.length = length

    def __call__(self, x, pos=None):
        """
        Functie die vanuit matplotlib aangeroepen wordt als een figuur
        gemaakt (of bekeken) wordt.

        argumenten:
            x: getal waarvan de opmaak aangepast moet worden
            pos: niet gebruikt argument vanuit matplotlib.
        return:
            string met daarin het juist opgemaakte getal.

        Herschrijft de getallen op de assen naar getallen met een vast aantal
        digits.
        """
        s = "%.10e" % x
        tup = s.split("e")
        signif = tup[0].rstrip(".")
        neg = ""
        if signif[0] == "-":
            neg = "-"
            signif = signif[1:]
        sign = tup[1][0].replace("+", "")  # verwijder +
        expo = tup[1][1:].lstrip("0")
        if expo:  # getal groter dan 10
            if self.length <= abs(int(expo)):  # schrijf als 10 macht
                expon = "10^{%s%s}" % (sign, expo)
                if self.length == 1:  # allen getal voor de . houden...
                    splt = signif.split(".")
                    signif = splt[0]
                else:  # meer dan 1 cijfer significant
                    signif = signif[: self.length + 1]
                    if len(signif) < self.length + 1:
                        signif += "0" * (self.length + 1 - len(signif))
                s = r"%s%s{\cdot}%s" % (neg, signif, expon)
            else:  # schrijf als getal
                s = "%.10f" % x
                extra0 = 0
                if s[0] == "-":
                    s = s[1:]
                if s[0] == "0":  # kleiner dan 1
                    splt = s.split(".")
                    zeros = splt[1].lstrip("0")
                    num = len(splt[1]) - len(zeros)
                    s = r"%s%s%s" % (neg, s[: self.length + 2], "0" * num)
                else:
                    s = r"%s%s" % (neg, s[: self.length + 1])
        else:  # exponent is 0
            if len(signif) >= self.length:
                if self.length == 1:
                    s = r"%s%s" % (neg, signif[: self.length])
                else:
                    s = r"%s%s" % (neg, signif[: self.length + 1])
            else:
                s = r"%s%s%s" % (neg, signif, "0" * (self.length - len(signif)))
        if s[-1] == ".":  # laatste teken een ., mag dus weg.
            s = s[:-1]
        # vervang punten door komma's.
        # Extra witruimte rond komma met {} uit string weggehaald.
        return "${}$".format(s.replace(".", "{,}"))

    def legenda(self, x, pos=None):
        """
        Functie aangeroepen vanuit matplotlib. Functie geeft aanroep naar
        __call__ terug.

        argumenten:
            x: getal waarvan de opmaak aangepast moet worden
            pos: niet gebruikt argument vanuit matplotlib.

        """
        return self.__call__(x, pos)


def label_x(grootheid, eenheid, ax, haak='[]', text='', fontsize=10):
    """
    Zet label van de as op een (relatief) makkelijke manier.

    argumenten:
        grootheid: grootheid van de waarden op de as.
        eenheid: eenheid van de waarden op de as.
        ax: matplotlib ax object waarin de x-as zicht bevindt.
        haak: standaard [], anders string met linker haak, rechter haak.
        text: eventuele tekst die voor de grootheid weergegeven moet worden.
        fontsize: eventuele fontsize voor de label-tekst, default 10pt.
    return:
        none
    """
    ax.xaxis.set_label_text(r'%s $\,%s \, %s\mathrm{%s}%s$' % (text,
                            grootheid, haak[0], eenheid, haak[1]),
                            fontsize=fontsize)


def label_y(grootheid, eenheid, ax, haak='[]', text='', fontsize=10):
    """
    Zet label van de as op een (relatief) makkelijke manier.

    argumenten:
        grootheid: grootheid van de waarden op de as.
        eenheid: eenheid van de waarden op de as.
        ax: matplotlib ax object waarin de x-as zicht bevindt.
        haak: standaard [], anders string met linker haak, rechter haak.
        text: eventuele tekst die voor de grootheid weergegeven moet worden.
        fontsize: eventuele fontsize voor de label-tekst, default 10pt.
    return:
        none
    """
    ax.yaxis.set_label_text(r'%s $\,%s \, %s\mathrm{%s}%s$' % (text,
                            grootheid, haak[0], eenheid, haak[1]),
                            fontsize=fontsize)


# Backwards compatiblity (fix_axis functie aanroep)

# Variabelen die na de import door de gebruiker aangepast kunnen worden.
# Variabelen geven het aantal significante getallen voor de x-, y-as.

PRECISION_X = 2
PRECISION_Y = 2


def fix_axis(ax):
    """
    Functie die de nieuwe Class implementatie beschikbaar houdt
    voor de oude functie definities.

    argumenten:
        ax: matplotlib ax object

    module argumenten:
        PRECISION_X: aantal significante getallen op de x-as
        PRECISION_Y: aantal significante getallen op de x-as
    """
    ax.yaxis.set_major_formatter(TNFormatter(length=PRECISION_Y))
    ax.xaxis.set_major_formatter(TNFormatter(length=PRECISION_X))


def _get_ticks(ticks):
    """
    Interne functie die de ticks aanpast aan de labels.

    argumenten:
        ticks:  lijst van ticklabels, gegenereerd met:
               ax.get_xticklabels() of ax.get_yticklabels()
    return:
        lijst met unieke tick-waarden.
    """
    values = []
    for tick in ticks[1:-1]:
        text = tick.get_text()
        text = text.replace("$", "")
        text = text.replace("{", "")
        text = text.replace("}", "")
        text = text.replace(r"\cdot10^", "E")
        text = text.replace(",", ".")
        num = float(text)
        if num not in values:
            values.append(num)
    if len(values) != len(ticks[1:-1]):
        print("Dubbele tick-waarden tegengekomen!\nControleer het figuur...")
    return values


def set_ticks(ax):
    """
    Zet de ticks op de x- en y-as.
    De tickwaarden worden gemaakt met behulp van de gevonden waarden
    in de labels.

    argumenten:
        ax: matplotlib ax object

    return:
        None
    """
    if ax.get_xticklabels()[0].get_text() == "":
        # no ticklabels, update layout!
        fig = ax.get_figure()
        fig.tight_layout()

    ticks_x = _get_ticks(ax.get_xticklabels())
    ticks_y = _get_ticks(ax.get_yticklabels())
    ax.set_xticks(ticks_x)
    ax.set_yticks(ticks_y)
