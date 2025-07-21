class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER= 'root'
    MYSQL_PASSWORD= 'usbw'
    MYSQL_DB= 'bd_trabajadores_jyb'

config = {
    'development' : DevelopmentConfig
}