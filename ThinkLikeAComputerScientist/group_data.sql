create external table if not exists group_data(
account_id,
channel_id,
client_id,
createdat,
id,
is_system,
member_id,
name,
created_at,
open_id,
properties,
unique_id,
updated_at
)
PARTITIONED by (dt string);
