import requests, json, numpy as np
from datetime import date
from .nomina import * 
# from a.payroll import *

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

vacaciones =  []
paid_vacation =  []
service_bonus =  []
severance =  []
work_disabilities =  []
maternity_leave =  []
paid_leave = []
non_paid_leave =  []
bonuse =  []
aid = []
legal_strike = []
compensations = []
epctv_bonuses =  []
commissions =  []
third_party_payments =  []
advances =  []
endowment =  ""
sustenance_support =  ""
telecommuting =  ""
withdrawal_bonus =  ""
compensation =  ""

labor_union =  []
sanctions =  []
orders=  []
third_party_payments =  []       
advances =  []
other_deductions =  []
voluntary_pension =  ""
withholding_at_source =  ""
afc =  ""
cooperative =  ""
tax_liens =  ""
supplementary_plan =  ""
education =  ""
refund =  ""
debt =  ""


class Totals:
    def __init__(self,document,path):
        self.sp = SendPayroll(document,path)
        self.pr = PayRollCustom(path,document)
        self.totalD = 0
        self.totalDeducciones = 0

    def result(self,obj,position):
        try:
            for i in range(len(obj)):
                self.totalD += obj[i][position]
        except Exception as e:
            self.totalD += 0

    def result2(self,obj,position):
        try:
            for i in range(len(obj)):
                self.totalDeducciones += obj[i][position]
        except Exception as e:
            self.totalDeducciones += 0
        

    def devengado(self):
        self.totalD = float(self.pr.SalaryMensual())
        self.result(self.pr.ExtraHour(),'payment')
        self.result(self.pr.ExtraNightTime(),'payment')
        self.result(self.pr.ExtraHourNightSurcharge(),"payment")
        self.result(self.pr.SundayExtraDaytime(),"payment")
        self.result(self.pr.ExtraHourDaytimeSurcharge(),"payment")
        self.result(self.pr.SundayExtraNightTime(),"payment")
        self.result(self.pr.ExtraHourNightSurchargeSun(),"payment")
        self.result(self.pr.ServiceBonus(),"payment")
        self.result(self.pr.ServiceBonus(),"paymentNS")
        self.result(self.pr.WorkDisabilities(),"payment")
        self.result(self.pr.MaternityLeave(),"payment")
        self.result(self.pr.PaidLeave(),"payment")
        self.result(self.pr.BonusSocial(),"salary_bonus")
        self.result(self.pr.BonusSocial(),"non_salary_bonus")
        self.result(self.pr.SalaryAssistant(),'payment')
        self.result(self.pr.SalaryAssistant(),'non_salary_assistance')
        self.result(self.pr.LegalStrike(),"payment")
        self.result(self.pr.Compensations(),"ordinary_compensation")
        self.result(self.pr.Compensations(),"extraordinary_compensation")
        self.result(self.pr.ThirdPartyPayments(),"third_party_payment")
        self.result(self.pr.EpctvBonuses(),"paymentS")
        self.result(self.pr.EpctvBonuses(),"paymentNS")
        self.result(self.pr.EpctvBonuses(),"salary_food_payment")
        self.result(self.pr.EpctvBonuses(),"non_salary_food_payment")
        self.result(self.pr.Commissions(),"commission")
        self.totalD += float(self.pr.SustenanceSupport())
        try:
            self.totalD += float(self.pr.ServiceBonus()[0]["interest_payment"])
        except Exception as e:
            self.totalD += 0
        self.totalD += float(self.pr.Telecommuting())
        self.totalD += float(self.pr.WithdrawalBonus())
        self.totalD += float(self.pr.Compensation())
        self.totalD += float(self.pr.OtherValues()[0])
        return "{:.2f}".format(self.totalD)

    def Deduccion(self):
        self.totalDeducciones += float(self.pr.EPSDeduction())
        print(self.pr.PensionDeduction())
        self.totalDeducciones += float(self.pr.PensionDeduction())
        self.result2(self.pr.LaborUnion(),'deduction')
        self.result2(self.pr.Sanctions(),'public_sanction')
        self.result2(self.pr.Sanctions(),'private_sanction')
        self.result2(self.pr.Orders(),"deduction")
        self.result2(self.pr.ThirdPartyPaymentsD(),"third_party_payment")
        self.result2(self.pr.AdvancesD(),"advance")
        self.totalDeducciones += float(self.pr.VoluntaryPension())
        self.totalDeducciones += float(self.pr.WithholdingAtSource())
        self.totalDeducciones += float(self.pr.AFC())
        self.totalDeducciones += float(self.pr.Cooperative())
        self.totalDeducciones += float(self.pr.TaxLiens())
        self.totalDeducciones += float(self.pr.SupplementaryPlan())
        self.totalDeducciones += float(self.pr.Education())
        self.totalDeducciones += float(self.pr.Fefund())
        self.totalDeducciones += float(self.pr.Debt())
        return "{:.2f}".format(self.totalDeducciones)

count = 0
def SendPayrollNomi(document,path,number):
    print("Soy nomina")
    
    sp = SendPayroll(document,path)
    pr = PayRollCustom(path,document)

    t = Totals(document,path)
    print(pr.WorkedDays())
    devengado = [
        30,pr.SalaryMensual(),pr.OtherValues()[1],
        pr.ExtraHour(),pr.ExtraNightTime(),pr.ExtraHourNightSurcharge(),pr.SundayExtraDaytime(),pr.ExtraHourDaytimeSurcharge(),pr.SundayExtraNightTime(),pr.ExtraHourNightSurchargeSun(),
        pr.ExtraLegalNonSalaryPremium(),
        pr.ServiceBonus(),pr.WorkDisabilities(),pr.MaternityLeave(),pr.PaidLeave(),pr.PaidNotLeave(),pr.BonusSocial(),pr.SalaryAssistant(),pr.LegalStrike(),
        pr.Compensations(),pr.EpctvBonuses(),pr.Commissions(),pr.ThirdPartyPayments(),pr.SustenanceSupport(),pr.Telecommuting(),pr.WithdrawalBonus(),pr.Compensation(),t.devengado()
    ]
    name = [
    "worked_days","salary","transportation_allowance",
        "HEDs","HENs","HRNs","HEDDFs","HRDDFs","HENDFs","HRNDFs",'service_bonus',
        "severance","work_disabilities","maternity_leave","paid_leave","non_paid_leave","bonuses",
        "aid","legal_strike","compensations","epctv_bonuses","commissions","third_party_payments",
        "sustenance_support","telecommuting","withdrawal_bonus","compensation","accrued_total"
    ]
    acurred = {}
    n = 0
    for i in devengado:
        if i != 0:
            acurred[name[n]] = i
        n += 1

    deduction = [
        1,pr.EPSDeduction(),5,pr.PensionDeduction(),pr.LaborUnion(),pr.Sanctions(),pr.Orders(),pr.ThirdPartyPaymentsD(),
        pr.AdvancesD(),pr.OtherDeductions(),pr.VoluntaryPension(),pr.WithholdingAtSource(),pr.AFC(),pr.Cooperative(),pr.TaxLiens(),
        pr.SupplementaryPlan(),pr.Education(),pr.Fefund(),pr.Debt(),t.Deduccion()
    ]
    name_deductions = [
        "eps_type_law_deductions_id","eps_deduction","pension_type_law_deductions_id","pension_deduction","labor_union","sanctions","orders",
        "third_party_payments","advances","other_deductions","voluntary_pension","withholding_at_source","afc",
        "cooperative","tax_liens","supplementary_plan","education","refund","debt","deductions_total"
    ]
    n_d = 0
    deduction_list = {}
    for j in deduction:
        if j != 0:
            deduction_list[name_deductions[n_d]] = j
        n_d += 1    
    url = "http://localhost/api/public/api/ubl2.1/payroll"

    payload = json.dumps({
      "type_document_id": 9,
      "establishment_name": "Inversiones Casa Colonial",
      "establishment_address": "Calle 50 No. 40 03",
      "establishment_phone": "4443016",
      "establishment_municipality": 1,
      "novelty": {
        "novelty": False,
        "uuidnov": ""
      },
      "period": {
        "admision_date": "2023-03-01",
        "settlement_start_date": "2023-02-01",
        "settlement_end_date": "2023-02-28",
        "worked_time": 30,
        "issue_date": "2023-03-01"
      },
      "worker_code": "0001",
      "prefix": "NI",
      "consecutive": number,
      "payroll_period_id": 5,
      "worker": pr.Worker(),
      "payment": pr.PaymentMethod(),
      "payment_dates": [
        {
          "payment_date": "2023-03-01"
        }
      ],
      "accrued": acurred,
      "deductions": deduction_list
    },cls=NpEncoder)
    print(payload)
    import time
    global count
    count += 1
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer fbcaff08718a4625e4885e76ac190d6cade6c001480ef6977994ece1829496f7'
    }

    # Payroll_NomiApp(
    #     number = number,
    #     nombre  = str(pr.Worker()['surname'])+' '+str(pr.Worker()['first_name']),
    #     total = float(t.devengado()) - float(t.Deduccion())
    # ).save()

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)



# pages = pd.ExcelFile("C:/Users/David/Desktop/Escritorio_2/Escritorio/gentelella_2/media/Document/NE_12_2021_colonial.xlsx") 
# list_pages = pages.sheet_names
# data = pd.read_excel("C:/Users/David/Desktop/Escritorio_2/Escritorio/gentelella_2/media/Document/NE_12_2021_colonial.xlsx", sheet_name=list_pages[0]).dropna()
# import time
# start = time.time()
# n = 47
# SendPayrollNomi(1000747641,"C:/Users/David/Desktop/Escritorio_2/Escritorio/gentelella_2/media/Document/NE_12_2021_colonial.xlsx",n)#1017175610 TOKEN ----> 77c8eb1f20281c1f744eb01a4446ae8cf1405a40612872a68f9a329c913bcad0
# for i in range(len(data)):
#     cc = int(data['Cedula Empleado'].values[i])
#     # print(cc)
#     SendPayrollNomi(cc,"NE_12_2021_colonial.xlsx",n)
#     n += 1
#     print(n)
# print(time.time() - start)