class myConfig:
    APP_NAME = 'snmp_interface'
    creator = 'CJM'
    contributor = 'baltop'


class DevelopmentConfig(myConfig):
    oidDefault = "1.3.6.1.4.1.30960.2.1.5.1.1.9."


class TestConfig(myConfig):
    oidDefault = "1.3.6.1.4.1.30960.2.1.5.1.1.10."


class ProductionConfig(myConfig) :
    oidDefault = "1.3.6.1.4.1.30960.2.1.5.1.1.11."
