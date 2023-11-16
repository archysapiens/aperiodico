# This class will contain all models for master de socios tables
class ModelAutomotriz:

    # Gets the schema for master de socios file for each layer of the DataWarehouse
    # @param master_product<str>: The master product
    # @param dwh_layer<str>: The DataWarehouse layer we want to work with
    # return: The json schema for that table
    def get_schema(self, master_product, dwh_layer):
        json_schema = None

        if master_product == 'CUIDADOS':
            if dwh_layer == 'LANDING':
                json_schema = self.get_schema_cuidados()

        return json_schema

    # Gets the table name for the desired product and layer
    # @param master_product<str>: The master product
    # @param dwh_layer<str>: The DataWarehouse layer we want to work with
    # return: The table name for that layer
    def get_tablename(self, master_product, dwh_layer):
        if master_product == 'CUIDADOS':
            if dwh_layer == 'LANDING':
                return 'tbl_master_cuidados'

    def get_from_filename_to_tablename(self):
        # Sets the equivalence between the names of the files and the tables
        json_names = {
            'Cuidados': 'tbl_msb_cuidados',
            'CuidadosOB': 'tbl_msb_cuidados_ob',
            'ProteccionFinanciera': 'tbl_msb_proteccion_financiera',
            'Proteccion': 'bl_msb_proteccion_financiera',
            'Valor': 'tbl_msb_valor_factura',
            'VALORA': 'tbl_msb_valora',
            'VIDA': 'tbl_msb_vida',
            'VitalPlusOB': 'tbl_msb_vital_plus_ob'
        }
        # Returns the json
        return json_names

    # Creates the schema for the master socios product
    # Product: Scotiabank Cuidados
    # Layer: Landing
    # return: A list with all the fields on the table
    def get_schema_cuidados(self):
        json_schema = [
            {
                'column_name': 'id_recording',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_ref_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'policy_number',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'effective_start_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'effective_end_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'purchase_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'hour_sales',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_status',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'net_premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'iva',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'selected_pkg',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_type',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'territory_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cancellation_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'cancellation_reason',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_frequency',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name_maternal',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'first_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'rfc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'product',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'phone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'streetname',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'neighborhood',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'delegation',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'state',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'postalcode',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_address',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'regulatory_code',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'initial_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'final_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_of_birth',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_mark',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'healthy_practices',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'modify_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'call_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cifkey',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'tel_contact',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_doc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_pay',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'status_documentacion',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'tipo_seguro',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cobertura',
                'data_type': 'STRING',
                'nullable': True
            }
        ]

        return json_schema

    # Creates the schema for the master socios product
    # Product: Valor factura y robo de autopartes Sucursal
    # Layer: Landing
    # return: A list with all the fields on the table
    def get_schema_valor_factura(self):
        json_schema = [
            {
                'column_name': 'quote_ref_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'policy_number',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'effective_start_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'effective_end_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'modify_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'purchase_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'hour_sales',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_status',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'territory_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'initial_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'final_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'year',
                'data_type': 'INTEGER',
                'nullable': True
            },
            {
                'column_name': 'selected_pkg',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'net_premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'iva',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'premium',
                'data_type': 'INTEGER',
                'nullable': True
            },
            {
                'column_name': 'payment_frequency',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name_maternal',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'first_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'rfc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'phone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_mark',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_doc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'streetname',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'neighborhood',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'delegation',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'state',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'postalcode',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_address',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'make',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'model',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'linea',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'vin',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'credit_term',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'check_de_uso_particular',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_type',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_pay',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'flow',
                'data_type': 'STRING',
                'nullable': True
            }
        ]

        return json_schema

    # Creates the schema for the master socios product
    # Product: Valor factura y robo de autopartes Sucursal
    # Layer: Landing
    # return: A list with all the fields on the table
    def get_schema_proteccion_financiera(self):
        json_schema = [
            {
                'column_name': 'id_recording',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_ref_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'policy_number',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'effective_start_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'effective_end_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'purchase_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'hour_sales',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_status',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'net_premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'iva',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'premium',
                'data_type': 'INTEGER',
                'nullable': True
            },
            {
                'column_name': 'selected_pkg',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_type',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'territory_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cancellation_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'cancellation_reason',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_frequency',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name_maternal',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'first_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'rfc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'product',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'phone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'streetname',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'neighborhood',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'delegation',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'state',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'postalcode',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_address',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'regulatory_code',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'send_sms',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'send_email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'initial_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'final_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_of_birth',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_mark',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'healthy_practices',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'modify_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'call_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cifkey',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'tel_contact',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'status_documentacion',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'agent',
                'data_type': 'STRING',
                'nullable': True
            }
        ]

        return json_schema

    # Creates the schema for the master socios product
    # Product: Vida Scotiabank
    # Layer: Landing
    # return: A list with all the fields on the table
    def get_schema_vida(self):
        json_schema = [
            {
                'column_name': 'id_recording',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_ref_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'policy_number',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'effective_start_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'effective_end_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'purchase_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'hour_sales',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_status',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'net_premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'iva',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'premium',
                'data_type': 'INTEGER',
                'nullable': True
            },
            {
                'column_name': 'selected_pkg',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_type',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'territory_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cancellation_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'cancellation_reason',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_frequency',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name_maternal',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'first_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'rfc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'product',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'phone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'streetname',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'neighborhood',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'delegation',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'state',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'postalcode',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_address',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'regulatory_code',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'initial_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'final_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_of_birth',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_mark',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'healthy_practices',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'modify_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'call_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cifkey',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'tel_contact',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'type_call',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'kit',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'medio',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_doc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_pay',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'status_documentacion',
                'data_type': 'STRING',
                'nullable': True
            }
        ]

        return json_schema

    # Creates the schema for the master socios product
    # Product: Scotiabank Cuidados
    # Layer: Landing
    # return: A list with all the fields on the table
    def get_schema_vital_plus_ob(self):
        json_schema = [
            {
                'column_name': 'id_recording',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_ref_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'policy_number',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'effective_start_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'effective_end_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'purchase_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'hour_sales',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_status',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'net_premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'iva',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'premium',
                'data_type': 'INTEGER',
                'nullable': True
            },
            {
                'column_name': 'selected_pkg',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_type',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'territory_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cancellation_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'cancellation_reason',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_frequency',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name_maternal',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'first_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'rfc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'product',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'phone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'streetname',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'neighborhood',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'delegation',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'state',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'postalcode',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_address',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'regulatory_code',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'initial_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'final_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_of_birth',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_mark',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'healthy_practices',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'modify_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM-dd-yyyy HH:mm:ss'
            },
            {
                'column_name': 'call_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cifkey',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'tel_contact',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'kit',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'medio',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_doc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_pay',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'status_documentacion',
                'data_type': 'STRING',
                'nullable': True
            }
        ]

        return json_schema

    # Creates the schema for the master socios product
    # Product: Scotiabank Cuidados
    # Layer: Landing
    # return: A list with all the fields on the table
    def get_schema_valora(self):
        json_schema = [
            {
                'column_name': 'id_recording',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_ref_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'policy_number',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'effective_start_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM/dd/yyyy'
            },
            {
                'column_name': 'effective_end_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM/dd/yyyy'
            },
            {
                'column_name': 'purchase_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM/dd/yyyy'
            },
            {
                'column_name': 'hour_sales',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_status',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'net_premium',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'iva',
                'data_type': 'FLOAT',
                'nullable': True
            },
            {
                'column_name': 'premium',
                'data_type': 'INTEGER',
                'nullable': True
            },
            {
                'column_name': 'selected_pkg',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_type',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'territory_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'branch',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'id_zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'zone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'user_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cancellation_date',
                'data_type': 'DATE',
                'nullable': True,
                'date_format': 'MM-dd-yyyy'
            },
            {
                'column_name': 'cancellation_reason',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'payment_frequency',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'last_name_maternal',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'first_name',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'rfc',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'product',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'phone',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'streetname',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'neighborhood',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'delegation',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'state',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'postalcode',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_address',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'regulatory_code',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'send_sms',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'send_email',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'initial_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'final_channel',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'country_of_birth',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'auth_mark',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'healthy_practices',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'quote_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM/dd/yyyy HH:mm:ss'
            },
            {
                'column_name': 'modify_date',
                'data_type': 'TIMESTAMP',
                'nullable': True,
                'date_format': 'MM/dd/yyyy HH:mm:ss'
            },
            {
                'column_name': 'call_id',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'cifkey',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'tel_contact',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'status_documentacion',
                'data_type': 'STRING',
                'nullable': True
            },
            {
                'column_name': 'agent',
                'data_type': 'STRING',
                'nullable': True
            }
        ]

        return json_schema
