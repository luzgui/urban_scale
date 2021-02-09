import calliope
import os

DIR=os.getcwd()

calliope.set_log_verbosity('INFO')

model = calliope.Model(DIR + '/model.yaml', scenario='milp')

model.run()


# model.results
