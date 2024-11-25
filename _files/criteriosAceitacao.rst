Critérios de aceitação
======================

Os critérios de aceitação são utilizados para verificar se a informação é entregue de forma adequada. De acordo com a cláusula 5.2.1 c) da EN ISO 19650-2, existem quatro recursos que fornecem regras para a forma como os requisitos de informação são definidos, entregues e verificados para todo o projeto, nomeadamente: (a) as normas de informação do projeto; (b) os métodos e procedimentos de produção de informação do projeto; (c) as informações de referência; e (d) os recursos partilhados.

Normas de informação do projeto
-------------------------------

As normas de informação do projeto visam descrever os critérios que irão dar suporte e consistência à informação que irá ser desenvolvida ao longo do projeto. De acordo com a cláusula 5.1.4 da EN ISO 19650-2, na sua definição há que ter em conta como serão efetuadas as trocas de informação, qual a estrutura e classificação da informação, qual o método usado para especificar o nível de informação necessário e o uso da informação em fases posteriores ao projeto e para operação do ativo.

Normas
^^^^^^

``Série de normas EN ISO 19650 e norma EN ISO 7817-1:2024``

Nomenclatura dos blocos de informação - Ficheiros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Os blocos de informação devem ser nomeados com o uso de oito campos, separados por um delimitador, de acordo com a seguinte convenção:``

.. image:: ../_static/Imagens/CamposNomenclatura.svg
    :alt: Campos da nomenclatura

**a) Projeto**

Código único e representativo do projeto.

.. parsed-literal::
    
    Código:
    OBG

**b) Originador**

Variável de acordo com a organização autora do bloco de informação.

Os códigos devem ser definidos por cada Entidade Fornecedora e fazer alusão ao nome da empresa. A entidade requerente fará a aprovação dos códigos propostos.

O código deve estar definido no Plano de Execução BIM e conter três caracteres.

.. parsed-literal::
    
    O código referente ao dono de obra é BSP.

**c) Estrutura de desagregação funcional**

Variável, refere-se às subdivisões relacionadas com a função, podendo ser desagregadas em volumes e sistemas.

A definição destes códigos é de responsabilidade de cada Entidade Fornecedora e pode ter até quatro caracteres.

Os códigos definidos devem estar listados juntos às suas definições no Plano de Execução BIM.

.. parsed-literal::
    
    Códigos:

    - XX - Não se aplica
    - ZZ - Todos

**d) Estrutura de desagregação espacial**

Variável, refere-se aos pisos do projeto ou outros tipos de desagregação espacial.

A listagem abaixo pode ser expandida pela Entidade Fornecedora caso se considere necessário.

Os novos códigos definidos devem estar listados juntos às suas definições no Plano de Execução BIM.

.. parsed-literal::
    
    Códigos:
    
    - XXX - Não se aplica
    - ZZZ - Diversos pisos
    - S02 - Subsolo 02
    - S01 - Subsolo 01
    - P00 - Rés do chão
    - P01 - Piso 01
    - P02 - Piso 02
    - P03 - Piso 03
    - P04 - Piso 04
    - C05 - Cobertura

**e) Forma**

Variável, refere-se à forma em que as informações são apresentadas. Cada bloco de informação deve conter um único tipo de informação.

A listagem pode ser expandida pela Entidade Fornecedora caso se considere necessário.

Os novos códigos definidos devem estar listados juntos às suas definições no Plano de Execução BIM.

.. parsed-literal::
    
    Códigos:
    
    Os códigos propostos estão listados na :ref:`ref-tabela-A1` do Apêndice A deste documento.

**f) Especialidade**

Variável de acordo com especialidade à qual o bloco de informação está relacionado.

.. parsed-literal::
    
    Códigos:
    
    Os códigos propostos estão listados na :ref:`ref-tabela-A2` do Apêndice A deste documento.

**g) Fase**

Variável de acordo com a fase à qual o bloco de informação está relacionado.

.. parsed-literal::
    
    Códigos:
    
    Os códigos propostos estão listados na :ref:`ref-tabela-A3` do Apêndice A deste documento.

**h) Número**

Variável e ordenado, aplicável a blocos de informação que façam parte de uma série de blocos e para os quais não há distinção em nenhum dos outros campos.

Os códigos devem conter o máximo de quatro dígitos composto por números inteiros.

.. parsed-literal::
    
    Códigos:
    
    - 0001 - Primeiro bloco de informação
    - 0002 - Segundo bloco de informação
    - nnnn - Numeração crescente

**h) Exemplo**

Um ficheiro PDF desenvolvido pela entidade fornecedora “Gabinete de Projetos de Portugal” (GPP), responsável pelo projeto de estabilidade, contendo o primeiro desenho 2D do projeto de fundações do edifício, para o qual não se aplica a definição de pisos.

.. parsed-literal::
    
    OBG-GPP-EST-DS-FUN-XXX-PP-0001.pdf

Metadados dos blocos de informação - Ficheiros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Metadados são atributos adicionais ao bloco de informação, que facilitam a localização, o uso e a gestão do mesmo.

Os blocos de informação devem conter metadados, separados por um delimitador, de acordo com a seguinte convenção:

.. image:: ../_static/Imagens/CamposMetadados.svg
    :alt: Campos dos metadados

**a) Estado**

A definição dos estados é apresentada, a propósito do CDE. Os respectivos códigos estão listados na :ref:`ref-tabela-B1` do Apêndice B deste documento.

**b) Revisão**

O código de revisão deve ser composto por três campos de acordo com a seguinte definição:

.. parsed-literal::
    <Campo1>.<Campo2>.<Campo3>

- ``Campo1`` - Letra única indicando se a revisão é Preliminar (P) ou Contratual (C)
- ``Campo2`` - Dois caracteres numéricos indicando o número da revisão primária.
- ``Campo3`` - Dois caracteres numéricos indicando a versão da revisão primária, exclusivamente utilizado para o “Trabalho em Curso”.

**c) Classificação**

Classificação de acordo com a `Tabela PM` (Project Management) do sistema `SECClasS`. Podem ser utilizadas outras tabelas do sistema de classificação se forem consideradas mais adequadas, desde que acordado com a Entidade Requerente.

**d) Descrição**

Descrição breve do conteúdo do bloco de informação.

**e) Data**

Data da última edição do bloco de informação.

**f) Outros**

Os blocos de informação podem incluir metadados adicionais caso sejam entendidos como necessários pela Entidade Fornecedora. Os novos códigos definidos devem estar listados juntos às suas definições no Plano de Execução BIM.


Nomenclatura dos blocos de informação - IFC: Objetos e informação alfanumérica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Não se prescreve. No entanto, recomenda-se a utilização das nomenclaturas da proposta de especificação técnica de "Regras de modelação de objetos" disponível no manual de objetos BIM `SECClass <https://bit.ly/secclass_manual_objetos_bim>`_. A entidade fornecedora líder deverá explanar os princípios adotados para a nomenclatura no BEP.

Sistema de unidades
^^^^^^^^^^^^^^^^^^^

``Sistema de Unidades Internacional`` em coerência com a Diretiva 80/181/EEC e respectivas adendas. EN ISO 80000-1:2022. A unidade monetária é o ``€``.

Sistema de coordenadas
^^^^^^^^^^^^^^^^^^^^^^

Será utilizado o sistema de coordenadas ``PT-TM06/ETRS89`` (EPSG: 3763), seguindo as especificações da `DGT <https://www.dgterritorio.gov.pt/geodesia/sistemas-referencia/portugal-continental/PT-TM06-ETRS89>`_.


Classificação da informação
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sistema de classificação `SECClasS <https://secclass.pt/pesquisa/>`_ na versão em vigor à data de emissão deste documento.

Formato e tamanho dos blocos de informação
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Documentos e folhas de cálculo editáveis seguindo a norma ISO/IEC 29500-1:2016 (sendo válidos por exemplo os formatos XLSX e DOCX).

Ficheiros de levantamento em nuvens de pontos em ASTM E57.

Desenhos em formato editável DWG.

Documentos, folhas de cálculo e desenhos não editáveis em formato PDF seguindo a norma ISO 32000-2:2020.

Modelos no formato proprietário da plataforma utilizada, a entregar no final de cada fase.

Modelos em IFC 4.0.2.1 (IFC4 ADD2 TC1) ISO 16739-1:2018. Máximo de 300 MB por bloco de informação independente.

Imagens em formato JPG ou PNG (resolução 1080p ou 4K).

Vídeos em formato MP4 (resolução 1080p ou 4K).

Trocas de pedidos de informação nos modelos em BCF.


Software - entidades fornecedoras
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Não há requisitos para os software a utilizar pelas entidades fornecedoras. Os software a usar serão validados em fase de aprovação do BEP.

Plataformas e software da entidade requerente
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Entidade Requerente irá utilizar o software ``<NomeDoSoftwareDeVizualização/VerificaçãoIFC>`` para visualizar, verificar e validar blocos de informação IFC. A entidade fornecedora líder deverá verificar o bom desempenho dos blocos de informação IFC nesta plataforma e informar de antemão sobre potenciais problemas na interpretação dos IFCs submetidos.

O CDE a utilizar será mantido nos servidores da entidade requerente e consistirá na solução CDE ``R2U``\*.

Todos os BCFs serão geridos de forma centralizada no CDE ``R2U``.

\* CDE ``R2U`` é um software aberto e gratuito preparado pela Universidade do Minho

Informação para o período operacional de gestão de ativos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sem requisitos específicos na fase de projeto para além da classificação já requerida. Essa informação será requerida na fase de consulta da empreitada.

Métodos e procedimentos de produção de informação do projeto
------------------------------------------------------------

Os métodos e procedimentos de produção de informação do projeto definem as abordagens e técnicas que a entidade requerente utiliza para criar, gerir e aprovar a informação.

Captura de informação de ativos existentes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Não havendo qualquer tipo de construção prévia no local e estando disponível o levantamento topográfico atualizado nas Informações de Referência (e cumpridor das prescrições da Câmara Municipal de Lisboa), não se prevê a necessidade de nenhuma captura de informação deste tipo.

Há necessidade de levantamento da envolvente através de métodos que permitam uma acuidade de informação suficiente para o processo de licenciamento e para análises de sombreamentos e oclusões.

As entidades fornecedoras ficarão responsáveis pela definição dos requisitos a solicitar para elaboração do relatório geológico-geotécnico necessário ao projeto de estabilidade. A entidade requerente fará a adjudicação e contratação independente dos trabalhos relacionados com a elaboração do relatório geológico-geotécnico.

Criação, revisão e aprovação de nova informação
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**a) Criação de informação**

A produção de modelos nativos e dados associados devem permitir a criação de modelos em IFC. Não deverão ser usados objetos Proxy quando exista uma classe de objeto específica para o efeito no SCHEMA IFC.

A equipa de projeto deverá definir uma origem do referencial local de coordenadas do projeto que seja comum a todos os modelos.

O referencial local poderá ter rotação em relação ao Norte do sistema de coordenadas, estabelecendo-se essa rotação no Plano de Execução BIM com a respetiva justificação.

A origem do referencial local de coordenadas do projeto deve ser identificada com um elemento geométrico com designação “OrigemDeProjeto”: pirâmide quadrangular invertida com 0.5m de base e 1m altura, e vértice inferior coincidente com a origem.

Adicionalmente, poderá também existir um segundo ponto (com designação “Marco”) com as mesmas características e com coordenadas locais (1,1,0).

Todos os modelos, de todas as especialidades, devem seguir uma determinação comum de cotas e nomenclatura de pisos.

Os objetos de espaço deverão conter informação consistente sobre o tipo, a função e a numeração do compartimento.

Todas as instâncias de objetos deverão estar atribuídas ao piso correto do edifício conforme o andar em que estão localizadas.

Instâncias de objetos com propriedades diferentes, p. ex., propriedades externas/internas, estruturais/não estruturais, deverão ser divididas em diferentes instâncias. Por exemplo, uma parede que passa do interior para o exterior deverá ser dividida na envolvente do edifício.

Para a produção dos mapas de trabalhos e quantidades deve ser utilizado o sistema de classificação definido neste documento, contudo há a possibilidade da entidade fornecedora líder propor uma granularidade adicional do sistema de classificação no seu BEP.

Os modelos entregues em IFC não devem conter duplicações de elementos entre especialidades distintas. Situações excepcionais deverão ser devidamente enquadradas e justificadas no BEP.

A estrutura dos modelos IFC deverá ser uniforme entre todas as disciplinas, cumprindo a nomenclatura de acordo com a seguinte tabela:

.. flat-table::
    :header-rows: 1

    * - Entidade IFC
      - Nomenclatura
    
    * - IfcProject           
      - OpenBIMGarden

    * - -- IfcSite
      - Arroios

    * - ---- IfcBuilding
      - OpenBIMGarden01

    * - ------ IfcBuildingStorey
      - S02

    * - ------ IfcBuildingStorey
      - S01

    * - ------ IfcBuildingStorey
      - P00

    * - ------ IfcBuildingStorey
      - P01

    * - ------ IfcBuildingStorey
      - P02

    * - ------ IfcBuildingStorey
      - P02

    * - ------ IfcBuildingStorey
      - P03

    * - ------ IfcBuildingStorey
      - P04

    * - ------ IfcBuildingStorey
      - C05

Poderão ser efetuadas algumas alterações na fase de projeto, a ser proposta pela entidade fornecedora líder.

O BEP pós-contrato deverá indicar a cota de cada IfcBuildingStorey, assim como, a sua elevação em relação ao 0,00 do projeto. Todas as disciplinas deverão seguir estas mesmas altimetrias.

São admitidos pisos auxiliares de trabalho nos modelos nativos, mas estes não poderão ser exportados para os modelos em formato IFC.

Os modelos IFC deverão ter sempre os objetos alocados ao IfcBuildingStorey correspondente.

No caso de desenhos editáveis, deverão ter o formato DWG quando gerados em CAD. No caso de desenhos gerados a partir de plataformas BIM, esta exigência aplica-se apenas no final de cada fase, como entregável. Não se coloca exigência de fidedignidade ao nível da formatação dos DWG aos PDF dos desenhos, dado que são meros documentos de trabalho.

**b) Coordenação**

A coordenação dos modelos deve ser realizada regularmente. Cada equipa de trabalho deve realizar a coordenação dos seus próprios modelos como parte do seu processo de garantia da qualidade, antes de partilhar a informação com a equipa de desenvolvimento. As trocas de informação/esclarecimento relativas a modelos BIM entre a entidade requerente e a entidade fornecedora líder deveram preferencialmente ser efetuadas com recurso a ficheiros BCF no CDE.

Toda troca de informação entre equipas de trabalho da mesma especialidade deve ocorrer dentro da sua respetiva pasta no estado *Trabalho em Curso* do Ambiente Comum de Dados. A organização e periodicidade destas trocas é determinada pela Entidade Fornecedora Líder referente à sua equipa de desenvolvimento.

As informações produzidas por cada Entidade Fornecedora devem ser apenas partilhadas com outras Entidades Fornecedoras quando já coordenadas dentro de cada equipa de desenvolvimento. As trocas de informações entre diferentes entidades fornecedoras ocorrem no estado *Partilhado* do Ambiente Comum de Dados. Define-se a periodicidade máxima de 15 dias para atualização dos modelos no CDE, com pelo menos estado S2.

**c) Revisão e aprovação da informação**

Cada equipa de trabalho deve efetuar uma verificação da garantia de qualidade de cada bloco de informação, antes de efetuar a revisão da informação nele contida.

O processo de revisão e aprovação da informação segue o fluxo ilustrado na figura a seguir:

.. image:: ../_static/Imagens/RevisaoAprovacaoInformacao.svg
    :alt: Processo de revisão e aprovação da informação

Os itens a serem considerados na revisão, bem como KPI's e checklist estão detalhados na :ref:`ref-tabela-aceitacao`.

Entrega da informação à entidade requerente
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As entregas finais serão realizadas utilizando a solução CDE determinada anteriormente.

Os entregáveis finais devem passar ao estado S5 (:ref:`ref-tabela-B1`) quando se encontrarem finalizados dentro das datas determinadas na secção 5.


Segurança
^^^^^^^^^

Os métodos e tecnologias de trabalho digitais colaborativos utilizados no projeto, envolvem a partilha colaborativa de informação por um conjunto de atores independentes, surgindo, portanto, a necessidade de gerir as questões de vulnerabilidade inerentes à disponibilidade da informação de acordo com os requisitos da EN ISO 19650-5. Assim, a Entidade Requerente realizou a avaliação de sensibilidade, com vista à identificação da necessidade, ou não, de uma abordagem de segurança e aplicou o processo de triagem o qual conduziu à classificação ST4.

Esta classificação permitiu concluir que neste projeto, não haverá necessidade de desenvolver uma estratégia de segurança, respetivo plano de segurança, planos de gestão de falhas e incidentes e acordos de partilha de informação com entidades fornecedoras. No entanto, devem ser protegidas as informações comerciais e pessoais de acordo com a legislação em vigor, nomeadamente o RGPD. Devem, ainda, ser tomadas medidas adequadas para minimizar as ameaças decorrentes de atividades fraudulentas e outras atividades criminosas e incidentes de cibersegurança.

Tabela de aceitação
-------------------

.. _ref-tabela-aceitacao:

.. flat-table:: Tabela de aceitação
    :header-rows: 1
    
    * - Critério de aceitação\*
      - Nota
      - Descrição
      
    * - Não Aplicável
      - NA
      - Requisito não aplicável numa fase ou para um determinado projecto
      
    * - Não Cumpre
      - 0
      - Não cumpre critérios do BEP; Em alguns casos como os Levels, as Grids e a Orientação / Sistema de Coordenadas, não existem gradações intermédias: aplica-se apenas o 0 ou o 3
      
    * - Cumpre Parcialmente
      - 1
      - Maioria dos blocos de informação não está de acordo com o BEP; Classificação não é suficiente para aprovação
      
    * - Cumpre Substancialmente
      - 2
      - Maioria dos blocos de informação está de acordo com o BEP; Classificação suficiente para aprovação condicional
      
    * - Cumpre Totalmente
      - 3
      - Todos os blocos de informação estão de acordo com o BEP

\* Nota mínima para aceitação é 2; Esta nota pode ser ponderada em função do contexto, fase de projecto ou especialidade e ser justificada nos comentários

Apreciação global
^^^^^^^^^^^^^^^^^

.. flat-table::
    :header-rows: 1

    * - Ref.
      - EIR
      - Título
      - Descrição
      
    * - A
      - EIR01
      - Levantamento de condicionantes
      - Entrega do resumo das condicionantes identificadas.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - B
      - EIR02
      - Levantamento do terreno e envolvente
      - Entrega da nuvem de pontos.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - C
      - EIR03
      - Estudo geológico-geotécnico
      - Entrega do relatório geológico-geotécnico.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - D
      - EIR04
      - Modelação
      - Entrega dos modelos nos formatos definidos nas normas de informação.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - E
      - EIR05
      - Coordenação dos modelos
      - Relatório de ausência de colisões (ou colisões com devida justificação).
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - F
      - EIR06
      - Coordenação BIM
      - Presença regular em reuniões de coordenação BIM e projeto coordenado com restantes especialidades.
        
        Colisões identificadas, comunicadas e resolvidas de acordo com processo descrito no EIR 06.
        
        Modelo federado com regularidade.
      
    * - G
      - EIR07
      - Peças Desenhadas
      - Entrega de peças desenhadas extraídas dos modelos.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - H
      - EIR08
      - Simulações energéticas e certificação
      - Entrega do relatório e certificado energético.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - I
      - EIR09
      - Análise de sustentabilidade BREEAM
      - Entrega do relatório da análise, garantindo a classificação final "Very Good".
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - J
      - EIR10
      - Estimativa de quantidades e custos
      - Entrega das estimativas de quantidades extraídas dos modelos.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - L
      - EIR11
      - Compilação de modelos
      - Entrega de todos os modelos e respetivas peças desenhadas e escritas.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - M
      - EIR12
      - Mapas de trabalhos e quantidades
      - Medições extraídas dos modelos / confirmar que medições são coerentes com o MQT.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.
      
    * - N
      - EIR13
      - Elaboração do plano de Segurança e Saúde e Compilação Técnica da Obra
      - Entrega do plano de Segurança e Saúde e início da Compilação Técnica da Obra.
        
        Informação fornecida de acordo com as normas e métodos e procedimentos de produção de informação do projeto.


Qualidade do Modelo
^^^^^^^^^^^^^^^^^^^

**a) Geometria**


.. flat-table::
    :header-rows: 1

    * - Ref.
      - Título
      - Descrição
      
    * - A
      - Apreciação geral
      - Modelo
      
    * - B
      - Origem / Sistema de Coordenadas
      - Coordenadas georeferenciadas e Prisma invertido presente no ficheiro
      
    * - C
      - Orientação
      - Orientado a Norte
      
    * - D
      - Eixos Estruturais
      - Eixos estruturais coordenados com ficheiro base (IfcGrid)
      
    * - E
      - Pisos
      - Níveis coordenados com ficheiro base (IfcBuidlingStorey)
      
    * - F
      - Duplicações
      - Não existem duplicações
      
    * - G
      - Requisitos minímos de informação geométrica
      - Detalhe, Dimensão, Localização, Aparência e Comportamento Paramétrico de acordo com Level of Information Need

**b) Informação não gráfica**

.. flat-table::
    :header-rows: 1

    * - Ref.
      - Título
      - Descrição
      
    * - H
      - Espaços / Areas
      - Cada compartimento identificado como IfcSpace
      
    * - I
      - Nomenclatura dos Blocos de Informação - Ficheiros
      - Ficheiros cumprem nomenclatura
      
    * - J
      - Blocos de Informação entregues na CDE
      - Todos os ficheiros foram colocados na CDE; incluí Ifc e ficheiros nativos
      
    * - K
      - Unidades
      - Sistema de unidades de acordo com definido no BEP
      
    * - L
      - Atributos (Ifc)
      - Objectos mapeados para as Class e Type IFC certas (evitar objectos classificados como IfcBuildingElementProxy)
      
    * - M
      - Propriedades (Ifc)
      - Modelo cumpre requisitos de informação do Level of Information Need
      
    * - N
      - Materiais
      - Materiais cumprem requisitos do Level of Information Need
      
    * - O
      - Classificação
      - Objectos classificados de acordo com sistema SECClasS
