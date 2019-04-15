from odoo import models, fields, api,_,exceptions
from odoo.exceptions import UserError, AccessError, ValidationError
import erppeek
import xmlrpclib
from django.template.defaultfilters import default
from Crypto.Util.number import size



############# AJOUT DUNE INSTANCE ####################

class Firststep(models.Model):
    _name = 'step.step'
    _description = 'First step'
    
    

    

    
    db_name = fields.Char(required=True,string="Nom de la base")  
    db_password = fields.Char(required=True,string="Mot de passe")
    db_login = fields.Char(required=True,string="Pseudo")


   

  

    
    @api.multi
    def db_create(self): 
        SERVER = 'http://localhost:8073'
        client = erppeek.Client(server=SERVER)
        if self.db_name in client.db.list():
            raise UserError(_('Database exist!!!')) 
        else:         
            if self.db_name and self.db_login and self.db_password:
                ra = client.create_database('admin', self.db_name, demo=False, lang='en_US', user_password=self.db_password, login=self.db_login)
         
        return ra


 



class Secondste(models.Model):
    _name = 'scnd_step'
    _description = 'Second step'
    
         
   
   
   
    @api.multi
    def get_db_list(self):
        res =[]
       
        SERVER = 'http://localhost:8073'
        client = erppeek.Client(server=SERVER)
        db_list = client.db.list()
        for dbb in db_list:
            aa = (dbb,dbb)
            res.append(aa)
       
        return res 
      
        
    @api.multi
    def db_restore(self):
        aa = self.db_liste
        SERVER = 'http://localhost:8073'
        client = erppeek.Client(server=SERVER)
        client.db.restore('admin', aa)  
        return True       
       
   
   
   
    @api.multi
    def db_delete(self):
        aa = self.db_liste
        SERVER = 'http://localhost:8073'
        client = erppeek.Client(server=SERVER)
        client.db.drop('admin', aa)  
        return True 
        
    name = fields.Char(string='Base 1',default='Enn')   
    db_liste = fields.Selection(selection=get_db_list, string= 'Liste des bases',type='string',size=256)
    
    
   
    
    
class Thirdstep(models.Model):
    _name = 'third.step'
    _description = 'Third step'
    
    
    
    
    
    
   
    @api.multi
    def get_db_list(self):
        res =[]
       
        SERVER = 'http://localhost:8073'
        client = erppeek.Client(server=SERVER)
        db_list = client.db.list()
        for dbb in db_list:
            aa = (dbb,dbb)
            res.append(aa)
       
        return res     
    
         


    @api.multi
    def connect_server(self):
        SERVER = 'http://localhost:8073'
        if self.login and self.pass_word and self.db_liste:
            client = erppeek.Client(SERVER,self.db_liste,self.login,self.pass_word)
        return client
    
   
   
    @api.multi
    def get_unistalled_list(self):
        res =[]
       
        SERVER = 'http://localhost:8073'
        if self.login and self.pass_word and self.db_liste:
            client = erppeek.Client(SERVER,self.db_liste,self.login,self.pass_word)
            
            installed_modules = client.modules(installed=True)
            
            for dbb in installed_modules['installed']:
                aa = (dbb,dbb)
                
                res.append(aa)

        print(res)
       
        return  res
    
    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id,record.asshole))
        print(result)
        return result 


 
    
    

  
    db_liste = fields.Selection(selection=get_db_list, string= 'Liste des bases',type='string',size=256)
    login = fields.Char(String='Login')
    pass_word = fields.Char(String='Pass word')
    uninstalled_modules = fields.Selection(get_unistalled_list,string='liste modules non installe',type='string',track_visibility='onchange')
    asshole = fields.Char(string='asshole')
    Modules_ni = fields.One2many('fourth.step','base_id')


class Fourthstep(models.Model):
    _name = 'fourth.step'
    
    
    
    
    @api.multi
    def get_unistalled_list(self):
        res =[]
       
        SERVER = 'http://localhost:8073'
        if self.base_id :
            client = erppeek.Client(SERVER,self.base_id.db_liste,self.base_id.login,self.base_id.pass_word)
            
            installed_modules = client.modules(installed=True)
            
            for dbb in installed_modules['installed']:
                aa = (dbb,dbb)
                
                res.append(aa)
        return res 
    
    
    
    name = fields.Char(string='name')
    base_id = fields.Many2one('third.step',string='base id',track_visibility='onchange')
    allo = fields.Selection(get_unistalled_list,string='liste modules non installe',type='string',track_visibility='onchange')
  
 
    
    
    
