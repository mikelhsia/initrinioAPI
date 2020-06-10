from sqlalchemy import create_engine
import yaml
import logging
log = logging.getLogger(__name__)

def get_database():
    try: 
        engine = get_connection_from_profile()
        log.info("Connected to SQL database!")
    except IOError:
        log.exception("Failed to get database connection!")
        return None, "fail"
    return engine

def get_connection_from_profile(config_file_name="setup_db_environment.yaml"):
    '''
    Sets up database connection from config file.
    Input:
    config_file_name: File containing HOST, USER, PASSWORD, DATABASE, PORT, which are the credentials for the database
    '''
    with open(config_file_name, 'r') as f:
        vals = yaml.safe_load(f)
    
    if not ('HOST' in vals.keys() and
            'USER' in vals.keys() and
            'PASSWORD' in vals.keys() and
            'DATABASE' in vals.keys() and
            'PORT' in vals.keys()):
        raise Exception("Bad config file: " + config_file_name)
    return get_engine(
        vals['DATABASE'],
        vals['USER'],
        vals['HOST'],
        vals['PORT'],
        vals['PASSWORD']
    )

def get_engine(db, user, host, port, passwd):
    '''
    Get SQLalchemy engine using credentials
    Input: 
    db: database name
    user: Username
    host: Hostname of the database server
    port: Port number
    passwd: Password for the database
    '''
    url = 'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=user, 
        passwd=passwd, 
        host=host, 
        port=port, 
        db=db
    )
        
    engine = create_engine(
        url, 
        encoding='utf-8', 
        pool_pre_ping=True,
        pool_size=50, 
        echo=True)
    return engine