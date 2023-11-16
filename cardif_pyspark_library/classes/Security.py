import hashlib
import hvac
import urllib3
from urllib.parse import urlparse, parse_qs
import time

def md5_hash(clear_text):
    result = hashlib.md5(clear_text.encode())
    return result.hexdigest()

vault_url = 'https://cobranza-jboss-configvault2-mx-assurance.staging.echonet'
token = 'hvs.CAESIIYkuOPPMgaVB9tCIobT9SzjOkyist1pB7ZjelBeQ3MmGh4KHGh2cy42QTZBT3hZbEozalRxeWZGV0pHRzdvRkU'
mount_point = 'dwhphase02'
path = 'spark'

# Definition of the class Vault
class Vault:
    # Init method to instance one object of this class
    def __init__(self):
        # deshabilitar warnings
        #urllib3.disable_warnings()
        #self.client = hvac.Client(url=vault_url, verify=False, token=token)
        #self.secret = self.client.secrets.kv.v2.read_secret_version(path=path, mount_point=mount_point)['data']['data']

        self.secret = {
            "connectionString": "QA_DEV:D3v310pmt#OdSq7@latam-oracle-dw01-qamx.br.xcd.net.intra:1521/?service_name=datawarehouse.qa.mx",
            "eucConnectionString": "DWH_EUC:U2eDw$qA20Jul2023@latam-oracle-dw01-qamx.br.xcd.net.intra:1521/?service_name=datawarehouse.qa.mx",
            "kafkaServer": "saox1d1mkf01.br.xcd.net.intra:9092",
            "kafkaServerUAT": "172.17.89.220:9092",
            "lndConnectionString": "DWH_LND:DwL1Nd$uq22Feb2023@latam-oracle-dw01-qamx.br.xcd.net.intra:1521/?service_name=datawarehouse.qa.mx",
            "odsConnectionString": "DWH_ODS:DwO1Ds$uq22Feb2023@latam-oracle-dw01-qamx.br.xcd.net.intra:1521/?service_name=datawarehouse.qa.mx",
            "slyConnectionString": "DWH_SRV:DwS1Rv$uq22Feb2023@latam-oracle-dw01-qamx.br.xcd.net.intra:1521/?service_name=datawarehouse.qa.mx",
            "stgConnectionString": "DWH_STG:DwS1Tg$uq22Feb2023@latam-oracle-dw01-qamx.br.xcd.net.intra:1521/?service_name=datawarehouse.qa.mx"
        }

    # Gets the secret depending on the given name
    # @param secret_name<str>: The secret name saved on Vault
    # return: The value of the secret
    def get_secret(self, secret_name):
        # Lee un secreto de Vault
        return self.secret[secret_name]

    # Gets the connection from Vault
    # @param layer<str>: The layer in DWH
    # return: The user, password, host, port and service
    def getUPS(self, layer):
        if (self.secret[layer + 'ConnectionString']):
            conStr = self.secret[layer + 'ConnectionString']
            user, password, host, port, service, *_ = conStr.split('@')[0].split(':') + conStr.split('@')[1].split('/')[0].split(':') + [conStr.split('=')[1]]
        else:
            user = None
            password = None
            port = None
            host = None
            service = None
        return user, password, host, port, service
