CREATE TABLE dwh_lnd.tbl_master_cuidados
(
    id_recording VARCHAR2(250 CHAR),
    quote_ref_id VARCHAR2(250 CHAR),
    policy_number VARCHAR2(250 CHAR),
    effective_start_date VARCHAR2(250 CHAR),
    effective_end_date VARCHAR2(250 CHAR),
    purchase_date VARCHAR2(250 CHAR),
    hour_sales VARCHAR2(250 CHAR),
    quote_status VARCHAR2(250 CHAR),
    net_premium VARCHAR2(250 CHAR),
    iva VARCHAR2(250 CHAR),
    premium VARCHAR2(250 CHAR),
    selected_pkg VARCHAR2(250 CHAR),
    payment_type VARCHAR2(250 CHAR),
    territory_name VARCHAR2(250 CHAR),
    id_branch VARCHAR2(250 CHAR),
    branch VARCHAR2(250 CHAR),
    id_zone VARCHAR2(250 CHAR),
    "ZONE" VARCHAR2(250 CHAR),
    user_id VARCHAR2(250 CHAR),
    user_name VARCHAR2(250 CHAR),
    cancellation_date VARCHAR2(250 CHAR),
    cancellation_reason VARCHAR2(250 CHAR),
    payment_frequency VARCHAR2(250 CHAR),
    last_name VARCHAR2(250 CHAR),
    last_name_maternal VARCHAR2(250 CHAR),
    first_name VARCHAR2(250 CHAR),
    rfc VARCHAR2(250 CHAR),
    product VARCHAR2(250 CHAR),
    phone VARCHAR2(250 CHAR),
    email VARCHAR2(250 CHAR),
    streetname VARCHAR2(250 CHAR),
    neighborhood VARCHAR2(250 CHAR),
    delegation VARCHAR2(250 CHAR),
    "STATE" VARCHAR2(250 CHAR),
    postalcode VARCHAR2(250 CHAR),
    country_address VARCHAR2(250 CHAR),
    regulatory_code VARCHAR2(250 CHAR),
    initial_channel VARCHAR2(250 CHAR),
    final_channel VARCHAR2(250 CHAR),
    country_of_birth VARCHAR2(250 CHAR),
    auth_mark VARCHAR2(250 CHAR),
    healthy_practices VARCHAR2(250 CHAR),
    quote_date VARCHAR2(250 CHAR),
    modify_date VARCHAR2(250 CHAR),
    call_id VARCHAR2(250 CHAR),
    cifkey VARCHAR2(250 CHAR),
    tel_contact VARCHAR2(250 CHAR),
    auth_doc VARCHAR2(250 CHAR),
    auth_pay VARCHAR2(250 CHAR),
    status_documentacion VARCHAR2(250 CHAR),
    tipo_seguro VARCHAR2(250 CHAR),
    cobertura VARCHAR2(250 CHAR),
	audittmload TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP
);
