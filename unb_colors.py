import matplotlib as mpl
from cycler import cycler

unb_colors = {
    'VerdeEscuro': '#005a1c', 
    'VerdeEscuro50': '#63a370', 
    'VerdeEscuro25': '#abceac', 
    'VerdeUnB': '#00822e',
    'VerdeUnB50': '#74bf83',
    'VerdeUnB25': '#b7deb9', 
    'VerdeMedio': '#98c000', 
    'VerdeMedio50': '#bfe588', 
    'VerdeMedio25': '#dff2c1', 
    'VerdeClaro': '#bad266', 
    'VerdeClaro50': '#d3eda9', 
    'VerdeClaro25': '#e9f6d3', 
    'AmareloMedio': '#fdca00', 
    'AmareloMedio50': '#fee17c', 
    'AmareloMedio25': '#fff0bc', 
    'AmareloPuro': '#ffed00', 
    'AmareloPuro50': '#fff980', 
    'AmareloPuro25': '#fffcbf', 
    'AzulUnB': '#003a7a', 
    'AzulUnB50': '#7080b4', 
    'AzulUnB25': '#b1b7d8', 
    'AzulMedio': '#0068b4', 
    'AzulMedio50': '#83a7dd', 
    'AzulMedio25': '#bfcfee', 
    'CianoPuro': '#00a6eb', 
    'CianoPuro50': '#80d6f7', 
    'CianoPuro25': '#bfebfb', 
    'AzulVioleta': '#2e1d86', 
    'AzulVioleta50': '#8677c3', 
    'AzulVioleta25': '#bfb3e0', 
    'AzulEsverdeado': '#00a0a7', 
    'AzulEsverdeado50': '#80d4ce', 
    'AzulEsverdeado25': '#bfeae4', 
    'Concreto1': '#7e7e65', 
    'Concreto2': '#adad98', 
    'Concreto3': '#d9d9ce', 
    'Concreto4': '#ededdf', 
    'PretoPreto': '#000000', 
    'Preto': '#1d1d1d', 
    'Preto75': '#5d5d5d', 
    'Preto50': '#989898', 
    'Preto25': '#d0d0d0', 
    'Preto10': '#eeeeee', 
    'Preto05': '#f6f6f6', 
    'Branco': '#ffffff'
}

def update_colors():
    mpl.rcParams['axes.prop_cycle'] = cycler(color=[
        unb_colors['VerdeUnB'],
        unb_colors['AzulMedio'],
        unb_colors['AmareloMedio'],
        unb_colors['VerdeMedio'],
        unb_colors['AzulUnB'],
        unb_colors['AmareloPuro'],
        unb_colors['VerdeEscuro'],
        unb_colors['AzulEsverdeado'],
        unb_colors['Concreto2'],
        unb_colors['VerdeClaro50'],
        unb_colors['CianoPuro'],
        unb_colors['Preto50']
    ])