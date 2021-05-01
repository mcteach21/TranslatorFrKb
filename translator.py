import os
import urllib.request as urllib2
from bs4 import BeautifulSoup, Comment

from termcolor import colored

import unidecode
import re

menu_color = 'blue'
dico_base_url = 'https://fr.glosbe.com/'


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def translate(case):
    source = 'fr' if case == 1 else 'kab'
    dest = 'kab' if case == 1 else 'fr'

    word_to_search = input('Mot à traduire (' + source + ') : ')
    url = dico_base_url + source + '/' + dest + '/' + slugify(word_to_search)



    try:

        request = urllib2.Request(url)
        request.add_header('Accept-Encoding', 'utf-8')

        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response, "html.parser")

        print(colored('*************************************************', 'yellow'))
        # result = [item.text.strip() for item in soup.find_all('h4', attrs={'data-cy': True})]
        result = [item.text.strip() for item in soup.find_all('span', attrs={'data-element': 'phrase'})]

        result = list(dict.fromkeys(result))
        # print(colored('Traduction "{}" [{}=>{}] : '.format(word_to_search, source, dest), 'yellow'))
        # print(colored('*************************************************', 'yellow'))
        print('Traduction "{}" [{}=>{}] : {}.'.format(word_to_search, source, dest, result))

        # if len(result) == 0:
        #     print('==================================')
        #     print('suggestions : ')
        #     print('==================================')
        #     maybe = [item.text.strip() for item in soup.find_all('div', {"class": "translate-intermediate-item-query"})]
        #     print(maybe)
        #     print('==================================')

        print(colored('*************************************************', 'yellow'))
        examples = [item.text.strip() for item in soup.find_all('div', {"class": "w-1/2"})]

        print('Exemples :')
        print('*************************************************')
        for i in range(0, len(examples) - 1):
            print(('' if i % 2 == 0 else '\t') + examples[i])

        print('*************************************************')

        # examples_fr = [item.text.strip() for item in soup.find_all('div', {"class": "translate-example-source"})]
        # examples_kab = [item.text.strip() for item in
        #                 soup.find_all('div', {"class": "translate-example-target ng-star-inserted"})]
        #
        # print('Autres Exemples :')
        # # print('*************************************************')
        #
        # for i in range(0, len(examples_fr) - 1):
        #     print(examples_fr[i])
        #     print('\t' + examples_kab[i])
        #     print()
        #
        # print('*************************************************')
    except :
        print('Aucun résultat trouvé :(')


def menu():
    print(colored("***************************************", menu_color))
    print(colored("************** Menu *******************", menu_color))
    print(colored("***************************************", menu_color))
    print(colored("1- Français => Kabyle", menu_color))
    print(colored("2- Kabyle => Français", menu_color))
    print(colored("3- Quitter!", menu_color))
    print(colored("***************************************", menu_color))

    nb = int(input("votre choix (1-3) : "))
    if nb == 1 or nb == 2:
        translate(nb)
        menu()
    else:
        print(colored('Thank you for using Translator :). Bye!', 'blue'))


def display():
    title = """
  _     _     _     _     _     _     _     _     _     _  
 / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
( T ) ( r ) ( a ) ( n ) ( s ) ( l ) ( a ) ( t ) ( o ) ( r )
 \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
    """
    os.system('color')

    # print(colored("***************************************", menu_color))
    print(colored(title, 'blue'))
    # print(colored("***************************************", menu_color))


display()
menu()
