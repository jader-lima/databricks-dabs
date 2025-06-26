from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType([
    StructField('CustomerId',IntegerType(), False),
    StructField('Fisrtname', StringType(), False),
    StructField('LastName', StringType(), False)
    ]
)

data = [
    (1000, 'Vlad', 'Tepez'),
    (1001, 'Count', 'Orlok'),
    (1002, 'Lestat', 'LionCourt')
]

vampires = spark.createDataframa(data, schema)
vampires.show()