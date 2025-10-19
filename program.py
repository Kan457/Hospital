class Hospital:
  def __init__(self, name , adress, guide):
    self.name = name
    self.adress = adress
    self.guide = guide #руководство
  def add_patient():
    ...
  def add_doctor():
    ...
  def Json_add(object): #добавление обекта в json
    json_data = json.dumps(object.__dict__, ensure_ascii=False)
    return json_data
    
class Administration:
  def __init__(self,chief_medical,telephone,mail,hospital):#агрегация больница - администрация
    self.chief_medical = chief_medical
    self.telephone = telephone
    self.mail = mail
  def Biography():
    ...
  def DF_doctor()
    
    
  
