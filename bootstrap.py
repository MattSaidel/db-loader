import sys, os
import argparse
from sqlalchemy import Column, String, MetaData, Table
import csv

sys.path.insert(0, os.path.dirname('/Users/matthewsaidel/Code/db-loader/*'))
#sys.path.insert(0, os.path.dirname('db-loader/etl/'))
#sys.path.insert(0, os.path.dirname('db-loader/datasource/'))

#alternatively

#sys.path.insert(0, os.path.dirname(os.getcwd()))
print sys.path


from datasource import engines
from etl import fec_dataloader as dl

dl.load_csv_into_memory(file_input) 
dl.create_fec_master(engine)
dl.load_to_db(data, table, engine)
dl.main(args)

if __name__ == '__main__':
    main(sys.argv[1:])


