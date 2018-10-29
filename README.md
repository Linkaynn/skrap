# Skrap - +2000 of tsunamis data spider
Puedes leer esto en [spanish](#español) o [english](#english).

//

You can read this in [spanish](#español) or [english](#english).

### **Español**

#### Descripción
Skrap es producto de la asignatura *Tipología y ciclo de vida de los datos* del Máster en Ciencia de Datos la Universidad Oberta de Catalunya. *Skrap* es capaz de recopilar información de tsunamis de la base de datos del *Institute of Computational Mathematics and Mathematical Geophysics
Siberian Division Russian Academy of Sciences*.

#### Código
La actividad ha sido desarrollada bajo la librería [Scrapy](https://doc.scrapy.org/en/latest/) así que se adapta a la arquitectura de esta. En cualquier caso explicaré lo necesario para ejecutar el script para recuperar información:

##### Preparando el entorno de ejecución
Previa a la ejecución hay que instalar Scrapy. Este se encuentra en el `requirements.txt`.
```bash
pip install -r requirements.txt
```

##### Ejecutando el script
El script que se debe ejecutar es el **run.py**, así que haciendo:

 ```bash
python run.py
```

Si todo ha ido bien, se generará un fichero .csv en la carpeta datasets con el siguiente formato: YY-mm-DD_HHmm.

##### Taxonomía del dataset

Puedes encontrar la taxonomía del dataset en el README dedicado a este, pulsa [aquí](datasets) para ir.

#### Autores
- Jesé Romero Arbelo

### **English**

#### Description
Skrap is the result of the subject *Tipología y ciclo de vida de los datos* of the master in Data Science of the Universidad Oberta de Catalunya. *Skrap* is capable of take information of tsunamies from the database of *Institute of Computational Mathematics and Mathematical Geophysics
Siberian Division Russian Academy of Sciences*.

#### Code
The activity was developed with the library [Scrapy](https://doc.scrapy.org/en/latest/) so it was adapted to the scrapy's architecture. In any case I will explain the necesary in order to execute the script to recover the information:

##### Setup the execution environment
Previous to the execution we need to install Scrapy. You can find it in the `requirements.txt`.
```bash
pip install -r requirements.txt
```

##### Executing the script
The script is the **run.py**, so:

 ```bash
python run.py
```

If everything is ok, it will generate a CSV file in the dataset folder with the pattern: YY-mm-DD_HHmm.

##### Dataset taxonomy

You can find the taxonomy of the dataset in the README dedicated to this, click here [aquí](datasets) to go.

#### Authors
- Jesé Romero Arbelo