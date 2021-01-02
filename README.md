# Sudoku_Solver
Artificial Intelligence Nanodegree Program - Udacity

Resolva Sudoku com IA	

## Sinopse

Neste projeto, você vai estender o agente de resolução de Sudoku desenvolvido nas aulas em sala de aula para resolver quebra-cabeças _diagonal_ de Sudoku e implementar uma nova estratégia de restrição chamada "gêmeos nus". Um quebra-cabeça Sudoku diagonal é idêntico aos quebra-cabeças Sudoku tradicionais com a restrição adicional de que as caixas nas duas diagonais principais do tabuleiro também devem conter os dígitos 1-9 em cada célula (assim como as linhas, colunas e blocos 3x3). A estratégia dos gêmeos nus diz que se você tiver duas ou mais caixas não alocadas em uma unidade e houver apenas dois dígitos que podem entrar nessas duas caixas, então esses dois dígitos podem ser eliminados das possíveis atribuições de todas as outras caixas na mesma unidade .


## Guia rápido

** VOCÊ SÓ PRECISA ESCREVER O CÓDIGO EM `solution.py`. **

1. Siga as instruções na lição em sala de aula para instalar e configurar o ambiente `aind` [Anaconda] (https://www.continuum.io/downloads) que inclui vários pacotes importantes que são usados para o projeto. Os usuários do OS X ou Unix / Linux podem ativar o ambiente aind executando o seguinte (os usuários do Windows simplesmente executam `activate aind`):
    
    `$ source activate aind`

2. Você pode executar um pequeno conjunto de casos de teste usando o conjunto de testes local.

    `(aind) $ python -m unittest -v`

3. Copie seu código da sala de aula para a pesquisa e estratégias básicas, então adicione as unidades diagonais no topo do arquivo solutions.py e complete a função `naked_twins ()`. O pseudocódigo para a função `naked_twins ()` está disponível [aqui] (https://github.com/udacity/artificial-intelligence/blob/master/Projects/1_Sudoku/pseudocode.md).

4. Execute o conjunto de testes novamente para verificar seu progresso. Depois de passar em todos os casos de teste no pacote de teste local, você pode enviar o projeto para executar testes mais abrangentes com o pacote de teste remoto:

    `(aind) $ udacity submit`

5. Você pode executar o código com visualização (consulte a última seção do leia-me para obter mais informações)

    `(aind) $ python solution.py`


### Notas

- Você não receberá crédito pelo projeto até que envie o arquivo zip criado por `udacity submit` em sua sala de aula.

- Você deve enviar _exatamente_ o arquivo zip criado pela CLI na etapa 3 para a sala de aula; se você fizer alguma alteração no arquivo, receberá uma mensagem de erro ao tentar enviar em sala de aula.


## Instruções

Você deve completar as funções necessárias no arquivo 'solution.py' (copiar o código da sala de aula onde indicado e adicionar ou estender com o novo código conforme descrito abaixo). O arquivo `test_solution.py` inclui alguns testes de unidade para teste local, mas o mecanismo principal para testar seu código é o utilitário de linha de comando Udacity Project Assistant descrito na próxima seção.

VOCÊ DEVE ESPERAR MODIFICAR OU ESCREVER SEUS TESTES DE UNIDADE COMO PARTE DA CONCLUSÃO DESTE PROJETO. Não há nenhum requisito para escrever casos de teste, mas o conjunto de testes do Assistente de Projeto não é compartilhado com os alunos, portanto, escrever seus próprios testes pode ser necessário para encontrar e resolver quaisquer erros que surjam.

1. Adicione as duas novas unidades diagonais à `unitlist` no topo de solution.py. Execute novamente os testes locais com `python -m unittest` para confirmar sua solução.

1. Copie seu código da sala de aula para `eliminar ()`, `only_choice ()`, `reduce_puzzle ()` e `search ()` para as funções correspondentes no arquivo `solution.py`.

1. Implemente a função `naked_twins ()` (veja o pseudocódigo [aqui] (https://github.com/udacity/artificial-intelligence/blob/master/Projects/1_Sudoku/pseudocode.md) para obter ajuda) e atualize `reduz_puzzle ()` para chamá-lo (junto com as outras estratégias existentes). Execute novamente os testes locais com `python -m unittest -v` para confirmar sua solução.

1. Execute os testes remotos com `udacity submit` para confirmar sua solução. Se qualquer um dos casos de teste remoto falhar, use o feedback para escrever seus próprios casos de teste locais para depuração.


## Submissão

Para enviar seu código, execute `udacity submit` em um terminal no diretório de nível superior deste projeto. Será solicitado um nome de usuário e uma senha na primeira vez que o script for executado. Se você fizer login usando o Google ou o Facebook, visite [este link] (https://project-assistant.udacity.com/auth_tokens/jwt_login) para obter instruções de login alternativas.

A ferramenta Udacity-PA CLI é instalada automaticamente com o ambiente AIND conda fornecido na sala de aula, mas você também pode instalá-lo manualmente executando `pip install udacity-pa`. Você pode enviar seu código para pontuação executando `udacity submit`. O servidor do assistente de projeto tem uma coleção de testes de unidade que executará em seu código e fornecerá feedback sobre quaisquer sucessos ou falhas. Você deve passar em todos os casos de teste no assistente de projeto para ser aprovado no projeto.

Depois que seu projeto passar em todos os casos de teste no Assistente de projeto, envie o arquivo zip criado pelo comando `udacity submit` na sala de aula para receber automaticamente o crédito pelo projeto. NOTA: Você não receberá feedback personalizado para este projeto sobre os envios que passarem em todos os testes cases no Assistente de Projeto, envie o arquivo zip criado pelo comando `udacity submit` na sala de aula para receber automaticamente o crédito pelo projeto. NOTA: Você não receberá feedback personalizado para este projeto sobre os envios que passarem em todos os casos de teste, no entanto, todos os outros projetos no prazo fornecem feedback personalizado sobre os envios de aprovação e reprovação.


## Visualização

** Observação: ** A biblioteca `pygame` é necessária para visualizar sua solução - entretanto, o módulo` pygame` pode ser problemático para instalar e configurar. Deve ser instalado por padrão com o ambiente AIND conda, mas não é confiável em todos os sistemas operacionais ou versões. Consulte a documentação do pygame [aqui] (http://www.pygame.org/download.shtml), ou discuta com seus colegas do grupo slack se precisar de ajuda.

Executar `python solution.py` tentará automaticamente visualizar sua solução, mas você deve usar a função` assign_value` fornecida (definida em `utils.py`) para rastrear o progresso da solução do quebra-cabeça para reconstrução durante a visualização.
