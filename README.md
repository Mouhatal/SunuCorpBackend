# BACKEND

# AUTEUR
* Mouhmadou TALL

## NOTEZ BIEN
* Avant de démarrer l'application veuillez mettre à jour crée la base de donnée et renseigner les information de connection à au niveau de DataBase : ./suncorp/settings.py
* Crée un environnement virtuel avec : virtualenv env  assurer vous d'abord d'installer virtualenv  avec pip install virtual env
* Activer l'environnement virtuel avec source env/Scripts/activate

##  CRUD API
* `GET - http://localhost/citypod/categories/` Récuperer la liste des categorie
* `GET - http://localhost/categorybyname/?categoryName=''` un enregistrement de category selon le nom
* `POST - http://localhost/addcategory/` Insert un category
* `PUT - http://localhost/updatecategory/?id=''` Mettre à jour un enregistrement de category
* `DELETE - http://localhost/deletecategory/?id=''` Supprimer un enregistrement de category

* `GET - http://localhost/citypod/subcategories/` Récuperer la liste des subcategory
* `GET - http://localhost/categorybyname/?subcategoryName=''` un enregistrement de subcategory selon le nom
* `POST - http://localhost/addsubcategory/` Insert un subcategory
* `PUT - http://localhost/updatesubcategory/?id=''` Mettre à jour un enregistrement de subcategory
* `DELETE - http://localhost/deletesubcategory/?id=''` Supprimer un enregistrement de subcategory

* `GET - http://localhost/citypod/elements/` Récuperer la liste des element
* `GET - http://localhost/elementbyname/?elementName=''` un enregistrement de category selon le nom
* `POST - http://localhost/addelement/` Insert un element
* `PUT - http://localhost/updateelement/?id=''` Mettre à jour un enregistrement de element
* `DELETE - http://localhost/deleteelement/?id=''` Supprimer un enregistrement de element


* `GET - http://localhost/citypod/pages/` Récuperer la liste des page
* `GET - http://localhost/pagebyname/?pageName=''` un enregistrement de category selon le nom
* `POST - http://localhost/addpage/` Insert un page
* `PUT - http://localhost/updatepage/?id=''` Mettre à jour un enregistrement de page
* `DELETE - http://localhost/deletepage/?id=''` Supprimer un enregistrement de page

