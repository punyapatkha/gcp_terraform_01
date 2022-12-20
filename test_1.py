
import pandas as pd
from datetime import datetime
import sqlalchemy
import mysql.connector 
import datetime
from binance.client import Client

def extract_binance_api(maxdate):
    timestamp = datetime.datetime.timestamp(maxdate)
    bars = client.get_historical_klines('BTCUSDT', '1d', str(timestamp), limit=1000)
    btc_df = pd.DataFrame(bars, columns=['open time','open','high','low','close','volume','close time','quote asset volume','number of trades','taker buy base asset volume','taker buy quote asset volume','ignore'])
    btc_df.set_index('open time', inplace=True)
    btc_df.reset_index(inplace= True)
    btc_df['open time'] = pd.to_datetime(btc_df['open time'],unit='ms')
    btc_df['close time'] = pd.to_datetime(btc_df['close time'],unit='ms')
    # (D,s,ms,us,ns)
    btc_df['update time']= datetime.datetime.now()
    return btc_df

if __name__ == '__main__':
    
#    config these variable <>

#    client = Client('example_iypbDmDLObSoajenxQQogZu22Scg7EROGmSb4KWWfkqIwSyoEl7GfMHrYmdESoUN', 'example_dQ1X8cz9gr1V10WFPdNzmoOy1RFRDw4ZcegEvPzRtcBrHV0QIy99efPFUH4uLPGl')
    client = Client('<>', '<>')
    
#    engine = sqlalchemy.create_engine('example_mysql://root:binance@34.126.75.181/crypto')
    engine = sqlalchemy.create_engine('<>')
    
    db = mysql.connector.connect(
#    host="example_34.126.75.181",
    host= <>,
    user="root",
    passwd="binance",
    db="crypto",
    autocommit=True)
    
    querystring = '''SELECT max(`open time`) from `test_3`'''
    cursor = db.cursor()
    cursor.execute(querystring)
    result = cursor.fetchall()
    master = pd.DataFrame(result)
    if master.empty:
        print("no lasted datetime in datawarehouse")
        b=datetime.datetime.strptime('2000-01-01 01:01:01','%Y-%m-%d %H:%M:%S')

    else:
        a = str(master.loc[0,0])
        print("lasted datetime in datawarehouse is "+a)
        b=datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    c=extract_binance_api(b+datetime.timedelta(days=1))
    c.to_sql(con=engine, name='test_3', if_exists='append',index=False)
    querystring2 = '''DELETE FROM test_3 ORDER BY `open time` DESC LIMIT 1'''
    cursor.execute(querystring2)
    cursor.close
