# MONITORAMENTO DE SERVICOS PYTHON

Monitoramento criado via python com envio de mail via Gmail para serviços que não estao ativos

Para utilizar basta colocar o login e senha de uma conta de email do Gmail e uma conta de email para recebimento.

No servidor que será nonitorado instalar o serviço via crontab abaixo indicando o local do arquivo de configuração;


No comando abaixo o monitoramento será rodado a cada 30 minutos

*/30 * * * * python /var/services.py

