import csv
import literales as lit


def valid_csvname():
    csv_name = input(lit.TXT_INPUT)
    if csv_name.count(lit.CSV_COUNT) != 1:
        csv_name = csv_name + lit.CSV
    return csv_name


def valid():
    num_regs = int(input(lit.NUM))
    if num_regs < 1:
        num_regs *= -1
    return num_regs

def file_exist():
    try:
       f =  open(lit.FILE+valid_csvname(),'r',encoding='utf-8',newline='')
       return True
    except FileNotFoundError:
        return False
    else:
        f.close()

def writeCSV():
    if file_exist() == False:
        f = open(lit.FILE+valid_csvname(),'a',encoding='utf-8',newline='')
        f.write('Nombre de la empresa','Nombre del projecto','Tecnologia','Responsable del projecto','Presupuesto','Fecha de inicio','Fecha final')
    with open(lit.FILE+valid_csvname(),'a',encoding='utf-8',newline=''):
        fieldnames = ['nmb_emp','nmb_prj','tec','rsp_prj','prsp','fch_in','fch_fin']
        regs = valid()
        for i in range(regs):


def insert_key():
    nbm_emp = input(NBM)
    nbm_prj = input(PRJ)
    tec = input(TEC)
    rsp = input(RSP)
    prsp = int(input(PRSP))

