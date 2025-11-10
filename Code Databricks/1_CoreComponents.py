import dlt
#create streaming table
@dlt.table(
    name="first_Stream_table"
)
def first_stream_table():
       df = spark.readStream.table("dtprashant.source.orders")
       return df

#create Materalized View
@dlt.table(
    name="first_mat_view"
)
def first_mat_view():
       df = spark.read.table("dtprashant.source.orders")
       return df
#create Batch View
@dlt.view(
    name="first_batch_view"
)
def first_batch_view():
       df = spark.read.table("dtprashant.source.orders")
       return df
#create streaming View
@dlt.view(
    name="first_steam_view"
)
def first_batch_view():
       df = spark.readStream.table("dtprashant.source.orders")
       return df
