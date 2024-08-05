### Resumo da analise do dataset Geodata
Tabela geodata registra todo o percurso de um veículo no período.
##### Dicionário de colunas
> Parte deste dicionário foi gerado via IA, favor validar, pois necessitaremos para futura documentação.

- registration: Identificador único ou código de registro para cada ponto geoespacial. Este campo é usado para
  diferenciar e identificar cada entrada no dataset.
- description: Descrição textual do ponto geoespacial. Pode incluir informações sobre o local, características
  específicas ou qualquer outro detalhe relevante.
- geometry_type: Tipo de geometria associada ao ponto geoespacial. Exemplos comuns incluem "Point" (ponto), "
  LineString" (linha), "Polygon" (polígono), entre outros. Este campo ajuda a entender a natureza da representação
  geoespacial.
- coordinates: Coordenadas geoespaciais do ponto, geralmente no formato [latitude, longitude]. Este campo é essencial
  para mapear o ponto em um sistema de coordenadas geográficas.
- execution_date: Data e hora em que o registro foi criado ou atualizado. Este campo está geralmente no formato de data
  e hora (por exemplo, "2024-08-05 14:30:00"), permitindo rastrear quando os dados foram coletados ou modificados. Este
  campo não está presente no endpoint, se fez necessário para podermos armazenar estes dados.
- hash: Valor hash gerado a partir dos dados do registro. Este campo é usado para verificar a integridade e
  autenticidade dos dados, garantindo que não foram alterados. Este campo não está presente no endpoint original. Ele
  é necessário para controlarmos duplicidade e integridade.
