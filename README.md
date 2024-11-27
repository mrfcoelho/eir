# eir

EIR - Requisitos de troca de informação

## Setup local

Para testar as alterações localmente usar o docker:

- Clonar este repo para uma directoria

- O comando seguinte permite lançar um container com acesso à directoria onde temos o repo

  ```
  docker run -it --rm -v <path_to_repo_directory>:/docs sphinxdoc/sphinx bash

  #exemplo
  docker run -it --rm -v "C:\Users\myname\Documents\myfolder\eir":/docs sphinxdoc/sphinx bash
  ```

- Intalar os packages necessários e que não constam na imagem docker do sphinx

  ```
  pip install --upgrade pip
  pip install sphinx sphinx-intl sphinx_rtd_theme sphinx-simplepdf linuxdoc
  ```

- Gerar a pagina html com o seguinte comando

  ```
  # usa a lingua default defina no ficheiro conf.py
  make html

  # para especificar a lingua a usar (neste caso en que é a outra opção que temos)
  make -e SPHINXOPTS="-D language='en'" html
  ```

- Gerar o pdf com o comando seguinte. O pdf vai estar em \_build/simplepdf

  ```
  make simplepdf
  ```

- Actualizar as traduções pode ter dois cenários distintos:

  - Se foi criado um novo ficheiro .rst é preciso gerar os ficheros .pot e .po correspondentes. Depois traduzir o .po. No final, gerar novamente o html para ver o resultado.

    ```
    ## criar os ficheiros .pot que vão aparecer em _build/gettext
    make gettext

    ## criar os ficheiros .po que vão aparecer em ./locale/en/LC_MESSAGES/
    sphinx-intl update -p _build/gettext -l en
    ```

  - Se apenas foi adicionado conteudo a ficheiros .rst existentes então é preciso actualizar o .pot e o .po com os comando seguintes. Depois, há que traduzir as novas entradas no .po. No final, gerar novamente o html para ver o resultado.

    ```
    ## actualiza os ficheiros .pot que estavam em _build/gettext
    make gettext

    ## actualiza os ficheiros .po que estavam em ./locale/en/LC_MESSAGES/
    sphinx-intl update -p _build/gettext
    ```

  - Se apenas foram atualizadas as traduções no ficheiro .po então basta o comando para gerar a página html.
