""" Programme principal pour la manipulation de mots de la langue française"""
#### Imports et définition des variables globales

import random

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires

def read_data(filename):
    """ Lit un fichier et retourne une liste de mots """
    with open(filename, mode='r', encoding='utf8') as f:
        l= [line.strip() for line in f]
    return l

def ensemble_mots(filename):
    """ Lit un fichier et retourne un ensemble de mots sous forme de set """
    mots=set(read_data(filename))
    return mots


def mots_de_n_lettres(mots, n):
    """ Retourne un sous-ensemble de mots de longueur n """
    sous_ensemble=set()
    for mot in mots:
        if len(mot)==n:
            sous_ensemble.add(mot)
    return sous_ensemble


def mots_avec(mots, s):
    """ Retourne un sous-ensemble de mots contenant s """ 
    sous_ensemble=set()
    for mot in mots:
        if s in mot:
            sous_ensemble.add(mot)
    return sous_ensemble

def cherche1(mots, start, stop, n):
    """ Retourne un ensemble de mots de n lettres 
    commençant par start et finissant par stop """
    sous_ensemble=set()
    mots_n=mots_de_n_lettres(mots,n) #set de mots de n lettres
    for mot in mots_n:
        if mot.startswith(start) and mot.endswith(stop):
            sous_ensemble.add(mot)
    return sous_ensemble


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    """ recherche plus complexe"""
    sous_ensemble=set()
    if lstart==[] or lstop==[] or lmid==[]:
        return sous_ensemble
    for mot in mots:
        for start in lstart:
            for stop in lstop:
                if mot.startswith(start) and mot.endswith(stop) and  nmin <= len(mot) <= nmax :
                    mil = mot[len(start):len(mot)-len(stop)]
                    for mid in lmid:
                        if mid in mil:
                            sous_ensemble.add(mot)
                            break
    return sous_ensemble


def main():
    """fonction principale"""
    mots = read_data(FILENAME)
    ens = ensemble_mots(FILENAME)
    print( [ mot for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"] if mot in ens ] )
    m17 = mots_de_n_lettres(ens, 17)
    print(len(m17))
    if len(m17) >= 10:
        print( random.sample(list(m17), 10) )
    mk = mots_avec(ens, 'k')
    print(len(mk))
    if len(mk) >= 5:
        print( random.sample(list(mk), 5) )
    moo = mots_avec(ens, 'oo')
    print(len(moo))
    if len(moo) >= 5:
        print( random.sample(list(moo), 5) )
    mz14 = cherche1(ens, 'z', '', 14)
    print(mz14)
    m21z = cherche1(ens, '', 'z', 18)
    print(m21z)
    m_z = cherche1(mots, 'z', 'z', 7)
    print(m_z)
    mab17ez = mots_avec(cherche1(ens, 'sur', 'ons', 17), 'x')
    print(mab17ez)
    mab17ez = cherche2(mots, 'a', 'b', 'z', 16, 16)
    print(mab17ez)


if __name__ == "__main__":
    main()
