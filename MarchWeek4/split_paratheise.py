import re
s1 ="item_number,item_name,specifications,bar_code,unit,warehouse,inventory_quantity,warehousing_application,issue_application,available_stock,channel_reservation,lock_pending,procurement_in_transit,transfer_in_transit,return_in_transit,production_in_transit,order_quantity,orderable_quantity,insertion_time"
split = s1.split(',')
for i in split:
    print(i)