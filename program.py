import json
class Guide:
  def __init__(self,chief_medical,phone,mail):
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

class Hospital:
  def __init__(self, name , adress, guide , to_dict):
    self.name = name
    self.adress = adress
    self.guide = Guide()
  #для более корректного получения значений
  def set(self,name,adress,guide):
    self.name = name
    self.adress = adress
    self.guide = Guide()
  #словарь для работы с json
  def to_dict(self):
    return {
      'Название' : self.name,
      'Адресс': self.adress,
      'Руководство': self.guide.guide_dict()
    }
  
  #добавление обекта в json
  def Json_add(object): 
    json_data = json.dumps(object.__dict__, ensure_ascii=False)
    return json_data
    
class Administration:
  def __init__(self,chief_medical,telephone,mail,hospital):#Компазиция больница - администрация
    self.chief_medical = chief_medical
    self.telephone = telephone
    self.mail = mail
  def Biography():
    ...
  def DF_doctor():
    ...
class Doctor:#
  def __init__(self,name,specialty, work_experience):
    self.name = name
    self.specialty = specialty
    self.work_experience = work_experience
  def retuer():
    ...


Hospital1 = Hospital('Поликлиника 109','ул.Пушкинская д.12','Петрова А.Н')
    
  
