import sys
from config import myConfig


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 1 else 'dev'

    if env == 'dev':
        config = myConfig.DevelopmentConfig
        print(config.oidDefault)
    if env == 'test':
        config = myConfig.TestConfig
        print(config.oidDefault)
    if env == 'prd':
        config = myConfig.ProductionConfig
        print(config.oidDefault)

