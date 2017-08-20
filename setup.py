# coding: utf-8
"""
Script de instalação de ambiente Django

Valida versão Python instalada e faz setup do ambiente.
"""
import os
import sys
import venv


def instalar():
    version_major = sys.version_info.major
    version_minor = sys.version_info.minor
    print('Sua versão de Python atual é {}.{}'.format(
        version_major,
        version_minor))

    if version_major < 3 or (version_major == 3 and version_minor < 6):
        print('Instale a versão 3.6 do Python antes!')
        input()
        exit()
    else:
        print('Versão 3.6')
        env_dir = os.path.dirname(os.path.abspath(__file__))
        print('Criando Virtualenv {}/.venv'.format(env_dir))
        env_builder = venv.EnvBuilder(
            system_site_packages=True,
            with_pip=True
        )
        env_builder.create(os.path.join(env_dir, '.venv'))
        text = """
        Criada Virtualenv com sucesso!
        Execute agora o comando para ativá-la:
            - No Linux:
            $ source .venv/bin/activate

            - No Windows:
            > .venv\Scripts\\activate
        """
        print(text)

if __name__ == '__main__':
    instalar()
