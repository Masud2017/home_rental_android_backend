# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session
import traceback
from services.WalletService import WalletService
import base64

from utils import util

class HomeDao:
    def __init__(self,db:Session):
        self.db = db


    def create_home(self, home : schemas.HomeModel,current_user:tables.User) -> schemas.HomeModelResponse:
        home_obj = tables.Home(**home.model_dump())

        home_obj.user = current_user    

        self.db.add(home_obj)
        self.db.commit()
        self.db.refresh(home_obj)

        return home_obj


    def get_homes(self) ->list[schemas.HomeModelResponse]:
        home_list = self.db.query(tables.Home).all()

        for item in home_list:
            print(item.image)
            img_bytes = util.get_image_from_disk(item.image)
            base = base64.b64encode(img_bytes)
            item.image = base

        return home_list
    
    def get_user_created_homes(self,current_user:tables.User)-> list[schemas.HomeModelResponse]:
        home_list = self.db.query(tables.Home).filter(tables.Home.user_id == current_user.id).all()


        for home_item in home_list:
            img_bytes = util.get_image_from_disk(home_item.image)
            base = base64.b64encode(img_bytes)
            home_item.image = base

        return home_list
    
    def delete_home(self,home_id:int,current_user:tables.User) -> schemas.HomeModelResponse:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()

        if len(res) == 0:
            return None
        else:
            if res[0].user.id == current_user.id:
                try:
                    self.db.delete(res[0])
                    self.db.commit()
                    return res[0]
                except Exception:
                    print(traceback.format_exc())
                    return None
            else:
                return None
            
    def get_home(self,home_id:int) -> schemas.HomeModelResponse:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()

        if len(res) == 0:
            return None
        else:
            home = res[0]
            img_bytes = util.get_image_from_disk(home.image)
            base = base64.b64encode(img_bytes)
            home.image = base
            return home
        

    def update_home(self,home_id:int,home : schemas.HomeModel, current_user : tables.User) -> bool :
        res = self.query(tables.Home).filter(tables.Home.id == home_id).all()

        if (len(res) == 0):
            return False
        else:
            home_obj = res[0]

            if home.name != "":
                home_obj.name = home.name
                
            if (home.desc != ""):
                home_obj.desc = home.desc
            if (home.price != 0):
                home_obj.price = home.price
            if (home.address != ""):
                home_obj.address = home.address

            if (home.flat_count != 0):
                home_obj.flat_count = home.flat_count

            home_obj.is_soled = home.is_soled

            self.db.commit()

            return True
        
    def buy_home(self,home_id:int, current_user:tables.User,flat_count :int  = 1)->bool:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()

        if (len(res) == 0):
            return False
        else:
            home = res[0]

            if (home.flat_count < flat_count):
                return False
            
            home_inventory = tables.HomeInventory()
            home_inventory.home = home
            home_inventory.image = home.image
            home_inventory.name = home.name
            home_inventory.flat_count = home.flat_count
            home_inventory.user = current_user
            home_inventory.flat_count = flat_count
            home.flat_count -= flat_count

            

            current_user.user_wallet.balance -= home.price
            home.user.user_wallet.balance += home.price

            self.db.add(home_inventory)
            self.db.commit()
            self.db.refresh(home_inventory)

            wallet_service = WalletService(self.db)
            transaction_history = schemas.TransactionHistory(user_id_second=home.user.id,msg = f"{home.name} flat count : = 1, price = {home.price}")
            transaction_history_owner = schemas.TransactionHistory(user_id_second=current_user.id,msg = f"Sold {home.name} flat count : = 1, price = {home.price}")
            


            wallet_service.add_transaction_history(transaction_history,current_user)
            wallet_service.add_transaction_history(transaction_history=transaction_history_owner,current_user=home.user)

            return True
        
    def cancel_home(self,inventory_id:int,current_user:tables.User) -> bool:
        res = self.db.query(tables.HomeInventory).filter(tables.HomeInventory.id == inventory_id).all()

        if (len(res) == 0):
            return False
        else:
            inventory = res[0]

            inventory.home.user.user_wallet.balance -= inventory.home.price
            current_user.user_wallet.balance += inventory.home.price

            inventory.home.flat_count += inventory.flat_count

            self.db.delete(inventory)
            self.db.commit()

            
            wallet_service = WalletService(self.db)
            transaction_history = schemas.TransactionHistory(user_id_second=inventory.home.user.id,msg = f"Got Refunded {inventory.home.name} flat count : = 1, price = {inventory.home.price}")
            transaction_history_owner = schemas.TransactionHistory(user_id_second=current_user.id,msg = f"Refunded {inventory.home.name} flat count : = 1, price = {inventory.home.price}")
            
            wallet_service.add_transaction_history(transaction_history,current_user)
            wallet_service.add_transaction_history(transaction_history=transaction_history_owner,current_user=inventory.home.user)
            
            return True
    
    def add_home_image(self, home_id, image,current_user : tables.User) -> bool:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()
        if (len(res) == 0):
            return False
        else:
            home = res[0]

            try:
                            
                home.image = util.save_file_to_disk(image,current_user.email)

                self.db.commit()
                return True
            except:
                import traceback
                print(traceback.format_exc())
                return False


    def get_inventory_list(self,current_user:tables.User) -> list[schemas.HomeInventory]:
        
        inventories:list[tables.HomeInventory]  = current_user.home_inventories
        for inven_item in inventories:
            img_bytes = util.get_image_from_disk(inven_item.image)
            base = base64.b64encode(img_bytes)
            inven_item.image = base

        return inventories