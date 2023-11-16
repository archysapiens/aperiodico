import syslog 

# Adds a new entry to the syslog
# @param meesage<str>: The message to be saved
# @param level<syslog>: The level of the log
def add_syslog_entry(message, level=syslog.LOG_INFO):
    """
    Agrega un mensaje al sistema de log nativo de Red Hat (Syslog).
    
    Args:
        message (str): El mensaje a agregar al log.
        level (int): El nivel de severidad del log. Los valores posibles son:
            - syslog.LOG_EMERG: Mensaje de emergencia.
            - syslog.LOG_ALERT: Mensaje de alerta.
            - syslog.LOG_CRIT: Mensaje crítico.
            - syslog.LOG_ERR: Mensaje de error.
            - syslog.LOG_WARNING: Mensaje de advertencia.
            - syslog.LOG_NOTICE: Mensaje de aviso.
            - syslog.LOG_INFO: Mensaje de información (valor predeterminado).
            - syslog.LOG_DEBUG: Mensaje de depuración.
    """
    # Opens the log
    syslog.openlog()
    # Adds a new entry
    syslog.syslog(level, message)
    # Closes the log
    syslog.closelog()
