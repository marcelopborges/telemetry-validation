### Resumo da analise do dataset Positions

#### A analise abaixo corresponde a dados extraídos dos dias 02/02/2024 a 8/06/2024.

* Latitude e Longitude: A precisão utilizada nos dados de geolocalização são de 15 casas decimais, o que é um exagero para a finalidade que estamos utilizando que é monitoramento de veículo. Segundo pesquisas (vide fonte), 8 casas é o recomendável para níveis considerados de precisão como agricultura de precisão ou estudo cientificos. 5 casas decimais (precisão de ~1,11 m) e 6 casas decimais (precisão de 11 cm) são mais do que suficiente para nossa finalidade. Ao final demontrarei uma tendencia de ocupação de espaço em disco, juntamente com outras medidas que serã sugeridas.
links: 
1. https://rapidlasso.de/england-releases-national-lidar-dem-with-insane-vertical-resolution/ 
2. https://en.wikipedia.org/wiki/Decimal_degrees


* **AgeOfReadingSeconds:** É o tempo de intervalo entre os dados, a média está em 4 segundos, acho que podemos agrupar estas informações para um tempo maior a não que cause algum evento, a finalidade é reduzir informações repetidas sem valor.
* **Pdop:** É um campo que possui informações zeradas, verificar se com os novos veículos estas informações serão preenchidas.
* **Hdop:** É um campo que possui informações, dentre estas informações temo 0,25% das informações com o valor zero, 96,19% com valor 1, registros que vão de 2 a 9 com baixa representatividade (menor que 1%) e o valor 25 que presenta 3,45% dos registros.
* **NumberOfSatellites:** Número de satelites identificados, realmente esta informação é necessária?
* **Heading:** Verificar o significado
* **SpeedKilometresPerHour:** Velocidade do veículo, possui algumas informações zeradas, mas normais no processo.
* **FormattedAddress:** Possui perto de 50% de valores nulo, de certa forma este campo é redundante com a geolocalização, podendo caso necessário ser obtido posteriormente, nas camadas de transformação (cleaned) ou de fornecimento (trusted), após agregação, motivo: Dados em string ocupam muito espaço em memória.
* **AltitudeMetres:** Possui 61% (1.707.800) de valores zerados, estas informações são relevantes? Os novos carros passarão a fornecer estes dados?
* **OdometerKilometres:** Está fornecendo informações nulas em alguns casos 2536, precisamos aplicar alguma regra de negócio nestes casos.

#### Proposta
1. Trucagem nas casas decimais
2. Retirada das colunas ['Pdop','NumberOfSatellites','FormattedAddress','AltitudeMetres']
3. Agrupamento dos campos calculados, principalmente devido a truncagem das geolocalizações
##### Comparação
Foi selecionado um dia aleatóriamente ('2024-04-08') para comparar os resultados.

**Dados originais**
>Memória total usada pelo DataFrame: 6.49 MB

**Dados tratados**
>Memória total usada pelo DataFrame: 1.90 MB

**Resultado**
>Obtenção de 70% na redução do tamanho do arquivo.

Notebook de estudo se encontra em reports/positions.ipynb