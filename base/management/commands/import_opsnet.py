import MySQLdb
from MySQLdb.cursors import DictCursor
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import data from OPS Net Site'

    def __init__(self):
        super(Command, self).__init__()

        self.db = MySQLdb.connect(db="ops_net",
                                  passwd="302010", host='127.0.0.1', port=3306, user='root')

    def _perform(self):
        db_cursor = self.db.cursor(cursorclass=DictCursor)
        db_cursor.execute("""
                            SELECT `cf_deputado`.`id`,
                                `cf_deputado`.`id_cadastro` as deputado_camara_id,
                                `cf_deputado`.`id_parlamentar`,
                                `estado`.`sigla`,
                                `partido`.`sigla` as partido_sigla,
                                `partido`.`nome` as partido_nome,
                                `cf_deputado`.`nome_parlamentar`,
                                `cf_deputado`.`nome_civil`,
                                `cf_deputado`.`url_foto`,
                                `cf_deputado`.`sexo`,
                                `cf_deputado`.`profissao`,
                                `cf_deputado`.`nascimento`,
                                `cf_deputado`.`matricula`,
                                `cf_deputado`.`valor_total_ceap`,
                                `cf_deputado`.`quantidade_secretarios`,
                                `cf_deputado`.`website`
                            
                            FROM `cf_deputado` 
                            
                            INNER JOIN `estado` on `estado`.`id` = `cf_deputado`.`id_estado`
                            INNER JOIN `partido` on `partido`.`id` = `cf_deputado`.`id_partido`
                            
                            WHERE `cf_deputado`.`falecimento` IS NULL
                            ORDER BY `cf_deputado`.`situacao` DESC""")

        row_count = 1
        for item in db_cursor:
            print(item)
            break

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("OPS - OPS NET Importer"))

        self._perform()  # DONE
