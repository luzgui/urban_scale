import pandas as pd

demand_power = pd.read_csv('demand_power.csv')
demand_heat = pd.read_csv('demand_heat.csv')
export_power = pd.read_csv('export_power.csv')
pv_resource = pd.read_csv('pv_resource.csv')

#option = 'v2'
option = 'v3'

demand_power['X4'] = demand_power['X1']
demand_power['X5'] = demand_power['X2']
demand_power['X6'] = demand_power['X3']

demand_heat['X4'] = demand_power['X1']
demand_heat['X5'] = demand_power['X2']
demand_heat['X6'] = demand_power['X3']

export_power['X4'] = export_power['X1']

if option == 'v3':
    demand_power['X7'] = demand_power['X1']
    demand_power['X8'] = demand_power['X2']
    demand_power['X9'] = demand_power['X3']

    demand_heat['X7'] = demand_power['X1']
    demand_heat['X8'] = demand_power['X2']
    demand_heat['X9'] = demand_power['X3']

    export_power['X7'] = export_power['X1']

if option == 'v2':
    demand_power.rename(columns={'Unnamed: 0': ''}).to_csv('demand_power_v2.csv', index = False)
    demand_heat.rename(columns={'Unnamed: 0': ''}).to_csv('demand_heat_v2.csv', index = False)
    export_power.rename(columns={'Unnamed: 0': ''}).to_csv('export_power_v2.csv', index = False)
    pv_resource.rename(columns={'Unnamed: 0': ''}).to_csv('pv_resource_v2.csv', index = False)
elif option == 'v3':
    demand_power.rename(columns={'Unnamed: 0': ''}).to_csv('demand_power_v3.csv', index = False)
    demand_heat.rename(columns={'Unnamed: 0': ''}).to_csv('demand_heat_v3.csv', index = False)
    export_power.rename(columns={'Unnamed: 0': ''}).to_csv('export_power_v3.csv', index = False)
    pv_resource.rename(columns={'Unnamed: 0': ''}).to_csv('pv_resource_v3.csv', index = False)