import json
#------------------Больница-------------------1
class Hospital:
  def __init__(self, name : str , adress : str, 
               staff : Staff , doctor : Doctor, patient : Patient, 
               attachment : Attachment, diagnosis : Diagnosis, work_schedule : Work_schedule, 
               referral : Referral, tests : Tests, medical_record : Medical_record, record : Record):
  self.name = name
  self.adress = adress
  self.staff = sraff
  self.doctor = doctor
  self.patient = patient
  self.attachment = attachment
  self.diagnosis = diagnosis
  self.work_schedule = work_schedule
  self.referral = Referral
  self.tests = tests
  self.medical_record = medical_record
  self.record = record
  #Корректное получение значений
  def set(self,name,adress,guide):
    self.name = name
    self.adress = adress
    self.staff = sraff
  #Словарь Поликлиника
  def to_dict(self):
    return {
      'Название' : self.name,
      'Адресс': self.adress,
      'Руководство': self.guide.guide_dict()
    }
#------------------Персонал-------------------2
class Staff:
  def __init__(self , chief_medical : string , phone : string , mail : string):
    self.chief_medical = chief_medical
    self.phone = phone
    self.mail = mail
  def set(self,chief_medical,phone,mail):
    self.chief_medical = chief_medical
    self.phone = phone
    self.mail = mail 
  def guid_dict(self):
    return {
      'Главный врая' : self.chief_medical,
      'Телефон': self.phone,
      'mail.ru': self.mail
    }
#------------------Врачи-------------------3  
class Doctor:#
  def __init__(self,name,specialty, work_experience):
    self.name = name
    self.specialty = specialty
    self.work_experience = work_experience
  def retuer():
    ...
#------------------Пациенты-------------------3
#------------------Прикрепление-------------------5
#------------------Диагноз-------------------6
#------------------График работы-------------------7
#------------------Направление-------------------8
#------------------Анализы-------------------9
#------------------Медицинская карта-------------------10
#------------------Запись-------------------11
Hospital1 = Hospital('Поликлиника 109','ул.Пушкинская д.12','Петрова А.Н')
    
  
