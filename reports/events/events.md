### Resumo da analise do dataset Events
#### A analise abaixo corresponde a dados extraídos dos 18/07/2024.

##### Dicionário de colunas
> Este dicionário foi gerado via IA, favor validar, pois necessitaremos para futura documentação.

- TotalOccurances: Número total de ocorrências do evento.
- TotalTimeSeconds: Tempo total em segundos que o evento durou.
- EventTypeId: Identificador único do tipo de evento.
- EventId: Identificador único do evento.
- DriverId: Identificador único do motorista associado ao evento.
- AssetId: Identificador único do ativo (veículo, equipamento) associado ao evento.
- Value: Valor associado ao evento, possivelmente representando uma métrica ou medição específica.
- EndDateTime: Data e hora de término do evento.
- StartOdometerKilometres: Quilometragem do odômetro no início do evento.
- EndOdometerKilometres: Quilometragem do odômetro no final do evento.
- EndPosition_Latitude: Latitude da posição final do evento.
- EndPosition_Longitude: Longitude da posição final do evento.
- EndPosition_NumberOfSatellites: Número de satélites utilizados para determinar a posição final.
- EndPosition_OdometerKilometres: Quilometragem do odômetro na posição final.
- EndPosition_Pdop: Diluição da precisão (PDOP) da posição final.
- EndPosition_PositionId: Identificador único da posição final.
- EndPosition_Source: Fonte dos dados da posição final (por exemplo, GPS).
- EndPosition_SpeedKilometresPerHour: Velocidade em km/h na posição final.
- EndPosition_SpeedLimit: Limite de velocidade na posição final.
- EndPosition_Timestamp: Timestamp da posição final.
- StartDateTime: Data e hora de início do evento.
- StartPosition_Latitude: Latitude da posição inicial do evento.
- StartPosition_Longitude: Longitude da posição inicial do evento.
- StartPosition_NumberOfSatellites: Número de satélites utilizados para determinar a posição inicial.
- StartPosition_OdometerKilometres: Quilometragem do odômetro na posição inicial.
- StartPosition_Pdop: Diluição da precisão (PDOP) da posição inicial.
- StartPosition_PositionId: Identificador único da posição inicial.
- StartPosition_Source: Fonte dos dados da posição inicial (por exemplo, GPS).
- StartPosition_SpeedKilometresPerHour: Velocidade em km/h na posição inicial.
- StartPosition_SpeedLimit: Limite de velocidade na posição inicial.
- StartPosition_Timestamp: Timestamp da posição inicial.
- FuelUsed: Quantidade de combustível utilizada durante o evento.
- FuelEconomy: Economia de combustível durante o evento.
- IdleTimeSeconds: Tempo de ociosidade em segundos durante o evento.
- DistanceTravelledKilometres: Distância percorrida em quilômetros durante o evento.
- AverageSpeedKilometresPerHour: Velocidade média em km/h durante o evento.
- MaxSpeedKilometresPerHour: Velocidade máxima atingida em km/h durante o evento.
- MinSpeedKilometresPerHour: Velocidade mínima atingida em km/h durante o evento.
- DurationSeconds: Duração total do evento em segundos.
- HarshBrakingCount: Contagem de frenagens bruscas durante o evento.
- HarshAccelerationCount: Contagem de acelerações bruscas durante o evento.
- OverSpeedCount: Contagem de vezes que o limite de velocidade foi ultrapassado durante o evento.
- IdlingCount: Contagem de eventos de ociosidade durante o evento.
- FuelEfficiencyRating: Classificação de eficiência de combustível durante o evento.
- DriverScore: Pontuação do motorista com base no evento.
- SafetyScore: Pontuação de segurança com base no evento.
- ComplianceScore: Pontuação de conformidade com base no evento.
- EnvironmentalScore: Pontuação ambiental com base no evento.
- OperationalScore: Pontuação operacional com base no evento.
- MaintenanceScore: Pontuação de manutenção com base no evento.

#### Observações
1. API teve alterações em sua composição de colunas, com ascrescimos de colunas e mudanças no formato do dado. Se faz necessário o compromisso de manter uma comunicação por parte do fornecedor para que todas as mudanças sejam previamente comunicadas.
2. Abaixo está relacionado a quantidade de dados nulos ou ausentes em cada coluna acima de 50% no dia especificado (18/07/2024). Como estamos em eminente mudança de frota, verificar se estes dados passarão a ser coletados.

Percentual de Nulos
1. LocationId	99.38%
2. EndPosition_AltitudeMetres	99.38%
3. StartPosition_AltitudeMetres	99.38%
4. FuelUsedLitres	80.90%
5. EndPosition_SpeedLimit	61.23%
6. StartPosition_SpeedLimit	51.57%

> Nossa sugestão até o presente momento é a retirada das colunas ['EndPosition_AltitudeMetres e StartPositions_AltitudeMetres'] estas colunas estão presente na "lista" nas colunas Endposition e StartPositions e possuem ambos mais de 90% de dados nulos.